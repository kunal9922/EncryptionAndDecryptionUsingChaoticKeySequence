import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from chaoticKeyGen import KeyGen
import cv2


class ChaoticCrypto:
    ''' encrypt and decrypt image by using Chaos Logistic Map(pseudo Random)'''

    def ecrypt_img(self, initCond, controlPara, pathImg: str):
        ''' encrypt an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter '''
        # reading an image
        img = mpimg.imread(pathImg)

        plt.imshow(img)
        plt.show()

        # take the image width and height
        height = img.shape[0]
        width = img.shape[1]

        noOfPixels = width * height
        keys = KeyGen()
        keysList = keys.logisticMapKeyGen(initCond, controlPara, noOfPixels)

        # another blank image for store encrypted image
        z = 0  # for tracking each key in key list
        enImg = np.zeros(shape=(height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                enImg[y, x] = img[y, x] ^ keysList[z]
                z += 1

        plt.imshow(enImg)
        plt.show()
        plt.imsave('dataSet/Encrypted_steve-jobs.jpg', enImg)

    def decrypt_img(self, initCond, controlPara, pathImg: str):
        ''' decryption an image by using Chaostic key Sequence and keys complexity is based on \n
        your passing initialCondition and controlParameter Note what aguments were passed to encryption is always same for decryption \n
        other wise decryption never will possible '''
        # reading an image
        enimg = mpimg.imread(pathImg)

        # take the image width and height
        height = enimg.shape[0]
        width = enimg.shape[1]

        noOfPixels = width * height
        keys = KeyGen()
        keysList = keys.logisticMapKeyGen(initCond, controlPara, noOfPixels)

        # another blank image for store decrypted image
        z = 0  # for tracking each key in key list
        decImg = np.zeros(shape=(height, width, 3), dtype=np.uint8)

        for y in range(height):
            for x in range(width):
                decImg[y, x] = enimg[y, x] ^ keysList[z]
                z += 1

        plt.imshow(decImg)
        plt.show()
        plt.imsave('dataSet/Decrypted_steve-jobs.jpg', decImg)


if __name__ == "__main__":

    imgSecure = ChaoticCrypto()
    imgSecure.ecrypt_img(0.01, 3.95, 'dataSet/steve-jobs.jpg')
    imgSecure.decrypt_img(
        0.01, 3.95, 'dataSet/Encrypted_steve-jobs.jpg')
