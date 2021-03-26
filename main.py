import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from chaoticKeyGen import KeyGen
import cv2


class ChaoticCrypto:
    ''' encrypt and decrypt image by using Chaos Logistic Map(pseudo Random)'''

    def ecrypt_img(self, initCond, controlPara, pathImg: str):
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


if __name__ == "__main__":

    imgSecure = ChaoticCrypto()
    imgSecure.ecrypt_img(0.01, 3.95, 'dataSet/steve-jobs.jpg')
