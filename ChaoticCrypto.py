import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


class ChaoticCrypto:
    ''' encrypt and decrypt image by using Logistic Map(pseudo Random)'''

    def ecrypt_img(self, path: str):
        # reading an image
        img = mpimg.imread(path)

        plt.imshow(img)
        plt.show()

        # take the image width and height
        height = img.shape[0]
        width = img.shape[1]

        noOfPixels = width * height


if __name__ == "__main__":
    print("hello")

    imgSecure = ChaoticCrypto()
    imgSecure.ecrypt_img('steve-jobs.jpg')
