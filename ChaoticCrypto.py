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


if __name__ == "__main__":
    print("hello")

    imgSecure = ChaoticCrypto()
    imgSecure.ecrypt_img('steve-jobs.jpg')
