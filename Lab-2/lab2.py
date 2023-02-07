import os
import numpy
import numpy as np


def saveTxt(initial, result):
    numpy.savetxt("file1.txt", initial, fmt="%.1d")
    numpy.savetxt("file2.txt", result, fmt="%.2f")
    open("result.txt", "w").write(open("file1.txt", "r").read() + "\n\n" + open("file2.txt", "r").read())
    os.remove("file1.txt")
    os.remove("file2.txt")
    content = numpy.loadtxt("result.txt")
    return content


def saveNpz(initial, result):
    np.savez_compressed('file.npz', matrix=initial, newMatrix=result, fmt="%.2f")
    finalRes = np.load('file.npz')
    old = finalRes['matrix']
    new = finalRes['newMatrix']
    np.round(new, 2)
    print("\nOld:", old, "New:", new, sep="\n")


def matrixVariable():
    matrix = np.random.randint(int(input("Enter low number: ")), int(input("Enter high number: ")),
                               size=(int(input("Enter N: ")), int(input("Enter M: "))))
    # maxNumber in matrix
    maxMatrix = numpy.amax(matrix)
    # divide matrix[i] on maxNumber
    newMatrix = np.divide(matrix, maxMatrix)
    # save newMatrix and initial matrix
    print('Initial matrix:', matrix, 'MaximumEl:', maxMatrix, sep='\n')
    np.round(newMatrix, 2)
    print(saveTxt(matrix, newMatrix))
    saveNpz(matrix, newMatrix)


try:
    matrixVariable()
except Exception as e:
    print(e)
