import numpy as np
from chaoticKeyGen import KeyGen
import cv2
from flask import Flask, request, jsonify, render_template, send_file, abort, send_from_directory
import base64
from bifurcation import BifurcationDiagram
import matplotlib.pyplot as plt
from io import BytesIO
from werkzeug.serving import make_server
import os
#flask app
app = Flask(__name__)
app.config["DEBUG"] = True
class ChaoticCrypto:
    ''' encrypt and decrypt image by using Chaos Logistic Map(pseudo Random)'''

    def encrypt_img(self, initCond, controlPara, img):
        ''' encrypt an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter '''
        # Get the image dimensions
        height, width, ch = img.shape
        noOfPixels = width * height

        keys = KeyGen()
        keysList = keys.logisticMapKeyGen(initCond, controlPara, noOfPixels)

        # another blank image for store encrypted image
        z = 0  # for tracking each key in key list
        enImg = np.zeros(shape=(height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                for chnl in range(ch):
                    enImg[y, x, chnl] = img[y, x, chnl] ^ keysList[z]
                z += 1

        #saving the encrypted image 
        encrypted_image_path = r"./static/images/encrypted_image.jpg"
        # Save the encrypted image
        cv2.imwrite(encrypted_image_path, enImg)

        # Convert encrypted image to base64 for sending as JSON
        _, encImageBuffer = cv2.imencode(".jpg", enImg)
        encImageBase64 = base64.b64encode(encImageBuffer).decode("utf-8")

        return encImageBase64

    def decrypt_img(self, initCond, controlPara, enimg):
        ''' decryption an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter Note what aguments were passed to encryption is always same for decryption \n
        other wise decryption never will possible '''
        # take the image width and height
        # Get the image dimensions
        height, width, ch = enimg.shape
        noOfPixels = width * height

        keys = KeyGen()
        keysList = keys.logisticMapKeyGen(initCond, controlPara, noOfPixels)

        # another blank image for store decrypted image
        z = 0  # for tracking each key in key list
        decImg = np.zeros(shape=(height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                for chnl in range(ch):
                    decImg[y, x, chnl] = enimg[y, x, chnl] ^ keysList[z]
                z += 1
        #saving the encrypted image 
        decrypted_image_path = r"./static/images/decrypted.jpg"
        # Save the encrypted image
        cv2.imwrite(decrypted_image_path, decImg)
        
        # Convert decrypted image to base64 for sending as JSON
        _, decImageBuffer = cv2.imencode(".jpg", decImg)
        decImageBase64 = base64.b64encode(decImageBuffer).decode("utf-8")

        return decImageBase64

#Web routes 
@app.route("/")
def index():
    return render_template("index.html")

#Encryption 
@app.route("/encrypt", methods=["POST"])
def encrypt():
    """
    Endpoint for encrypting an image using the ChaoticCrypto algorithm.
    
    Request JSON Parameters:
    - initCond: Initial condition for the encryption algorithm (float)
    - controlPara: Control parameter for the encryption algorithm (float)
    - image: Base64-encoded image data (string)
    
    Returns:
    - JSON response containing the encrypted image in Base64 format
    """
    initCond = float(request.json["initCond"])
    controlPara = float(request.json["controlPara"])
    imgData = base64.b64decode(request.json["image"])

    nparr = np.frombuffer(imgData, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    imgSecure = ChaoticCrypto()
    encryptedImageBase64 = imgSecure.encrypt_img(initCond, controlPara, img)

    bifurcationMap = BifurcationDiagram()
    bifurcationResultX, bifurcationResultR = bifurcationMap.calBifucation(
        min_r=3.0, max_r=4.0, step_r=0.0001, max_iters=1000, skip_iters=100
    )

    # Filter the bifurcation diagram data based on the initial condition and control parameter
    filteredResultX = bifurcationResultX[
        (bifurcationResultR >= initCond) & (bifurcationResultR <= controlPara)
    ]
    filteredResultR = bifurcationResultR[
        (bifurcationResultR >= initCond) & (bifurcationResultR <= controlPara)
    ]

    # Plot the bifurcation diagram using Matplotlib
    plt.scatter(filteredResultX, filteredResultR, s=1, c="red")
    plt.xlabel("X")
    plt.ylabel("R")
    plt.title("Bifurcation Diagram")
    plt.tight_layout()

    # Save the bifurcation diagram as an image file
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_buffer_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")

    # Prepare the response data
    responseData = {
        "encryptedImage": encryptedImageBase64,
        "bifurcationImage": img_buffer_base64,
    }
    print(type(encryptedImageBase64))
    print(type(img_buffer_base64))

    # Return the encrypted image and bifurcation diagram data as a JSON response
    return jsonify(responseData)

#Decryption
@app.route("/decrypt", methods=["POST"])
def decrypt():
    """
    Endpoint for decrypting an encrypted image using the ChaoticCrypto algorithm.
    
    Request JSON Parameters:
    - initCond: Initial condition for the decryption algorithm (float)
    - controlPara: Control parameter for the decryption algorithm (float)
    - encryptedImage: Base64-encoded encrypted image data (string)
    
    Returns:
    - JSON response containing the decrypted image in Base64 format
    """
    initCond = float(request.json["initCond"])
    controlPara = float(request.json["controlPara"])
    encryptedImageData = base64.b64decode(request.json["encryptedImage"])

    nparr = np.frombuffer(encryptedImageData, np.uint8)
    enimg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    imgSecure = ChaoticCrypto()
    decryptedImageBase64 = imgSecure.decrypt_img(initCond, controlPara, enimg)

    #Bifurcation For Decrypted Image
    bifurcationMap = BifurcationDiagram()
    bifurcationResultX, bifurcationResultR = bifurcationMap.calBifucation(
        min_r=3.0, max_r=4.0, step_r=0.0001, max_iters=1000, skip_iters=100
    )

    # Filter the bifurcation diagram data based on the initial condition and control parameter
    filteredResultX = bifurcationResultX[
        (bifurcationResultR >= initCond) & (bifurcationResultR <= controlPara)
    ]
    filteredResultR = bifurcationResultR[
        (bifurcationResultR >= initCond) & (bifurcationResultR <= controlPara)
    ]

    # Plot the bifurcation diagram using Matplotlib
    plt.scatter(filteredResultX, filteredResultR, s=1, c="red")
    plt.xlabel("X")
    plt.ylabel("R")
    plt.title("Bifurcation Diagram Decrypt")
    plt.tight_layout()

    # Save the bifurcation diagram as an image file
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    img_buffer_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")

    # Prepare the response data
    responseData = {
        "decryptedImage": decryptedImageBase64,
        "bifurcationImage": img_buffer_base64,
    }
    print(type(decryptedImageBase64))
    print(type(img_buffer_base64))

    # Return the encrypted image and bifurcation diagram data as a JSON response
    return jsonify(responseData)

    # # Return the decrypted image in Base64 format as a JSON response
    # return jsonify({"decryptedImage": decryptedImageBase64})

# Download encrypted image route
@app.route("/download_encrypted", methods=["GET"])
def download_encrypted():
    encrypted_image_path = r"./static/images/encrypted.jpg"
    filename = "encrypted_image.jpg"
    try:
        return send_from_directory(os.path.dirname(encrypted_image_path), filename, as_attachment=True, mimetype="image/jpeg")
    except FileNotFoundError:
        abort(404)  # Return a 404 error if the file is not found
    except Exception as e:
        print(f"Error while sending the encrypted image: {e}")
        abort(500)  # Return a 500 error for any other unexpected errors

@app.route("/bifurcation", methods=["POST"])
def bifurcation():
    """
    Endpoint for generating the bifurcation diagram.

    Request JSON Parameters:
    - min_r: Minimum value of the r parameter (float)
    - max_r: Maximum value of the r parameter (float)
    - step_r: Step size for the r parameter (float)
    - max_iters: Maximum number of iterations (integer)
    - skip_iters: Number of iterations to skip (integer)

    Returns:
    - JSON response containing the x and r coordinates of the bifurcation diagram
    """
    min_r = float(request.json["min_r"])
    max_r = float(request.json["max_r"])
    step_r = float(request.json["step_r"])
    max_iterations = int(request.json["max_iters"])
    skip_iterations = int(request.json["skip_iters"])

    result_x, result_r = BifurcationDiagram.calBifucation(min_r, max_r, step_r, max_iterations, skip_iterations)

    # Return the bifurcation diagram coordinates as a JSON response
    return jsonify({"result_x": result_x.tolist(), "result_r": result_r.tolist()})

def run_flask_server():
    # app.config['MIME_TYPES'] = {
    # '.js': 'application/javascript'
    # }
    # app.run(debug=True)
    server = make_server("localhost", 5000, app)
    server.serve_forever()
