import itertools
class KeyGen:
    ''' chaos is based on the ability of some dynamic \n
    systems to produce of numbers that are random in nature and use as a keys for \n
    encrypt and decrypt every pixel of an image '''

    def logisticMapKeyGen(self, initCondition, controlParameter, img) -> list:

        # Get the image dimensions
        height, width, ch = img.shape
        for y, x in itertools.product(range(height), range(width)):
            if not isinstance(initCondition, (int, float)):
                raise ValueError("Invalid initial condition")
            if not isinstance(controlParameter, (int, float)):
                raise ValueError("Invalid control parameter")

            # .`. x = initialCondition , r = controlParameter
            # x = r * x * (1-x) logistic map
            # logistic map for key geniration
            initCondition = controlParameter * \
                initCondition*(1 - initCondition)
                
            for chnl in range(ch):
                # this is a key for for encryption as well decryption
                # taking mod 256 because it is for 8bit image
                #Updating Image pixels with generated keys
                img[y, x, chnl] = img[y, x, chnl] ^ int((initCondition*pow(10, 16)) % 256)
    
        return img
