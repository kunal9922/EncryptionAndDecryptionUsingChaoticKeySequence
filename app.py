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
        pass

    def decrypt_img(self, initCond, controlPara, enimg):
        ''' decryption an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter Note what aguments were passed to encryption is always same for decryption \n
        other wise decryption never will possible '''
        pass

#main 
if __name__ == "__main__":
    pass 
