import numpy as np


class ShuffleMatrix:
    '''shuffle matrix '''

    def shuffleMatrix(self, matrix, idx: int):
        rows = len(matrix)
        cols = len(matrix[0])
        shuffleMatrix = np.zeros((rows, cols), type(matrix))

        # matix shuffling
        for r in range(0, rows):
            k = 0
            for c in range(0, cols):
                shuffleMatrix[r][c] = matrix[r][idx[k]]
                k = k + 1
        return shuffleMatrix

    def reshuffleMatrix(self, matrix, idx: int):
        rows = len(matrix)
        cols = len(matrix[0])
        orignalMatrix = np.zeros((rows, cols), type(matrix))

        # matix shuffling
        for r in range(0, rows):
            k = 0
            for c in range(0, cols):
                orignalMatrix[r][idx[k]] = matrix[r][c]
                k = k + 1
        return orignalMatrix


class ShuffleArray:
    ''' shuffle the values in array and reShuffle the values'''

    def shuffle(self, arr, index: int):
        '''shuffle the array args {arr:[list or numpy.array], index:[list or numpy.array]}
            index will be the how to shuffle the values according to index values
        '''
        lenArray = len(arr)
        suffledArr = []  # empty list to store the shuffled list
        for i in range(0, lenArray):
            suffledArr.append(arr[index[i]])

        return suffledArr

    def reshuffle(self, shuffledArr, index: int):
        '''Reshuffle the array to it's orignal state args = {arr:[list or numpy.array], index:[list or numpy.array]}
            index will be the how to reshuffle the values according through index values'''
        lenArray = len(shuffledArr)
        orignalArr = np.zeros(lenArray, dtype=type(shuffledArr))
        for i in range(0, lenArray):
            orignalArr[index[i]] = shuffledArr[i]

        return orignalArr


lst = [10, 20, 30, 40, 50]
idx = [3, 2, 0, 1, 4]

arrange = ShuffleArray()
lst = arrange.shuffle(lst, idx)
lst = arrange.reshuffle(lst, idx)

matrix = [[2, 5],
          [8, 3]]
arrangeMatrix = ShuffleMatrix()
arrangeMatrix.shuffleMatrix(matrix=matrix, idx=[1, 0])
arrangeMatrix.reshuffleMatrix(matrix=matrix, idx=[1, 0])
