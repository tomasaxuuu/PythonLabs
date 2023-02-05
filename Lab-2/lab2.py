import numpy
import numpy as np


def matrixVariable():
    matrix = np.random.randint(int(input("Enter low number: ")), int(input("Enter high number: ")),
                               size=(int(input("Enter N: ")), int(input("Enter M: "))))
    # maxNumber in matrix
    maxMatrix = numpy.amax(matrix)
    # divide matrix[i] on maxNumber
    newMatrix = np.divide(matrix, maxMatrix)
    # matrix[maxNumber] = maxNumber (not maxNumber / maxNumber)
    newMatrix[newMatrix == 1] = maxMatrix
    # around 2
    np.round(newMatrix, 2)
    numpy.savetxt("file1.txt", newMatrix, fmt="%.2f")
    content = numpy.loadtxt('file1.txt')

    return {'matrix': matrix, 'maximum': maxMatrix, 'resultMatrix': newMatrix, 'fileMatrix': content}


try:
    print(matrixVariable())
except Exception as e:
    print(e)
