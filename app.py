import numpy as np
from chaoticKeyGen import KeyGen
import cv2
from flask import Flask, request, jsonify, render_template
import base64

#flask app
app = Flask(__name__)

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
    pass

#Decryption
@app.route("/decrypt", methods=["POST"])
def decrypt():
    pass 



#main 
if __name__ == "__main__":
    pass 
