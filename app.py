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
import mimetypes
from flask_ngrok import run_with_ngrok
#flask app
app = Flask(__name__)
app.config["DEBUG"] = True

class ChaoticCrypto:
    ''' encrypt and decrypt image by using Chaos Logistic Map(pseudo Random)'''

    def encrypt_img(self, initCond, controlPara, img):
        ''' encrypt an image by using Chaotic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter '''
        keys = KeyGen()
        img = keys.logisticMapKeyGen(initCond, controlPara, img)

        #saving the encrypted image 
        encrypted_image_path = r"./static/images/" + enFileName
        print(encrypted_image_path)
        imgExt = enFileName.split(".")[-1]
        # Use the appropriate OpenCV flag for saving images in their original format
        if imgExt in ("jpg", "jpeg"):
            cv2.imwrite(encrypted_image_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        elif imgExt == "png":
            cv2.imwrite(encrypted_image_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        # Save the encrypted image with its original file extension
        #cv2.imwrite(encrypted_image_path, img)

        # Convert encrypted image to base64 for sending as JSON
        _, encImageBuffer = cv2.imencode(".jpg", img)
        encImageBase64 = base64.b64encode(encImageBuffer).decode("utf-8")

        return encImageBase64

    def decrypt_img(self, initCond, controlPara, enimg):
        ''' decryption an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter Note what aguments were passed to encryption is always same for decryption \n
        other wise decryption never will possible '''

        keys = KeyGen()
        enimg = keys.logisticMapKeyGen(initCond, controlPara, enimg)

        #saving the encrypted image 
        decrypted_image_path = r"./static/images/" + deFileName
        imgExt = deFileName.split(".")[-1]
        # Save the encrypted image
        # Use the appropriate OpenCV flag for saving images in their original format
        if imgExt in ("jpg", "jpeg"):
            cv2.imwrite(decrypted_image_path, enimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        elif imgExt == "png":
            cv2.imwrite(decrypted_image_path, enimg, [cv2.IMWRITE_PNG_COMPRESSION, 0])

        #cv2.imwrite(decrypted_image_path, enimg, [cv2.IMWRITE_PNG_COMPRESSION, 0])
        
        # Convert decrypted image to base64 for sending as JSON
        _, decImageBuffer = cv2.imencode(".jpg", enimg)
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
    
    print(request.json["fileName"])
    fileName = request.json["fileName"].split(".")
    
    global enFileName
    enFileName = f"{fileName[0]}_encrypted.{fileName[1]}"
    print(enFileName)
    img = cv2.imdecode(np.frombuffer(imgData, np.uint8), cv2.IMREAD_COLOR)

    # Get the size (width and height) of the image
    height, width, channels = img.shape

    print(f"Image Size (Width x Height): {width} x {height} = {enFileName}")

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

    # Decode the base64 data and convert it to a NumPy array directly
    enimg = cv2.imdecode(np.frombuffer(encryptedImageData, np.uint8), cv2.IMREAD_COLOR)
    
    print(request.json["fileName"])
    fileName = request.json["fileName"].split(".")
    
    global deFileName
    deFileName = f"{fileName[0]}_decrypted.{fileName[1]}"
    print(enFileName)
    # # Get the size (width and height) of the image
    # height, width, channels = enimg.shape
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

# Download encrypted image route
@app.route("/download_encrypted", methods=["GET"])
def download_encrypted():
    encrypted_image_path = r"./static/images/"
    try:
        # Use the mimetypes module to map the extension to a MIME type
        mimetype, _ = mimetypes.guess_type(enFileName)
        print(mimetype)

        # Default to "application/octet-stream" if the MIME type cannot be determined
        if mimetype is None:
            mimetype = "application/octet-stream"

        # Use the send_from_directory function to send the file
        return send_from_directory(os.path.dirname(encrypted_image_path), enFileName, as_attachment=True, mimetype=mimetype)
    except FileNotFoundError:
        abort(404)  # Return a 404 error if the file is not found
    except Exception as e:
        print(f"Error while sending the encrypted image: {e}")
        abort(500)  # Return a 500 error for any other unexpected errors

# Download decrypted image route
@app.route("/download_decrypted", methods=["GET"])
def download_decrypted():
    decrypted_image_path = r"./static/images/"
    try:
        # Use the mimetypes module to map the extension to a MIME type
        mimetype, _ = mimetypes.guess_type(deFileName)
        print(mimetype)

        # Default to "application/octet-stream" if the MIME type cannot be determined
        if mimetype is None:
            mimetype = "application/octet-stream"
            
        return send_from_directory(os.path.dirname(decrypted_image_path), deFileName, as_attachment=True, mimetype=mimetype)
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
