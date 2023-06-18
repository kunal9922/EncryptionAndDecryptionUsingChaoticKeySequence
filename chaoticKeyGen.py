class KeyGen:
    ''' chaos is based on the ability of some dynamic \n
    systems to produce of numbers that are random in nature and use as a keys for \n
    encrypt and decrypt every pixel of an image '''

    def logisticMapKeyGen(self, initCondition, controlParameter, NoOfKeys) -> list:

        key = []  # list for storing the no. of keys for ecryption

        for _ in range(NoOfKeys):
            if not isinstance(initCondition, (int, float)):
                raise ValueError("Invalid initial condition")
            if not isinstance(controlParameter, (int, float)):
                raise ValueError("Invalid control parameter")

            # .`. x = initialCondition , r = controlParameter
            # x = r * x * (1-x) logistic map
            # logistic map for key geniration
            initCondition = controlParameter * \
                initCondition*(1 - initCondition)

            # this is a key for for encryption as well decryption
            # taking mod 256 because  is for 8bit image
            key.append(int((initCondition*pow(10, 16)) % 256))

        return key
