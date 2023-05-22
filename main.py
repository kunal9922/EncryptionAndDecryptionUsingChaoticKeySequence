import numpy as np
from chaoticKeyGen import KeyGen
import cv2


class ChaoticCrypto:
    ''' encrypt and decrypt image by using Chaos Logistic Map(pseudo Random)'''

    def ecrypt_img(self, initCond, controlPara, pathImg: str):
        ''' encrypt an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter '''
        # reading an image
        img = cv2.imread(pathImg)

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

        return enImg
        
    def decrypt_img(self, initCond, controlPara, pathImg: str):
        ''' decryption an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter Note what aguments were passed to encryption is always same for decryption \n
        other wise decryption never will possible '''
        # reading an image
        enimg = cv2.imread(pathImg)

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

        return decImg
        


if __name__ == "__main__":

    imgSecure = ChaoticCrypto()
    #Encryption of Image
    encImage = imgSecure.ecrypt_img(0.01, 3.95, 'dataSet/steve-jobs.jpg')
    cv2.imwrite('dataSet/Encrypted_steve-jobs.jpg', encImage)

    # Decryption on Image 
    decrImage = imgSecure.decrypt_img(
       0.01, 3.95, 'dataSet/Encrypted_steve-jobs.jpg')
    cv2.imwrite('dataSet/Decrypted_steve-jobs.jpg', decrImage)
