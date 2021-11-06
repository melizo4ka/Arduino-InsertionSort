import csv
import serial
from timeit import default_timer as timer
import random


def insertionSort(A):
    if A is None:
        A = []
    for j in range(2, 500):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def main():
    # arduino insertion
    ser = serial.Serial('COM3', 9600, timeout=1)
    startTimeA = timer()
    for i in range(500):
        line = ser.readline()
        if line:
            string = line.decode()
            num = int(string)
    endTimeA = timer()
    tempoIS = round(endTimeA - startTimeA, 3)
    ser.close()
    table = [['Sorting', 'Time'], ['InsertionSort 500', tempoIS]]
    file = open('timeArd500.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(table)

    # python insertion
    A = []
    startTimeP = timer()
    for i in range(500):
        x = random.randint(0, 500)
        A.append(x)
    insertionSort(A)
    for k in range(500):
        y = A[k]
    endTimeP = timer()
    tempoISP = round(endTimeP - startTimeP, 3)
    table = [['Sorting', 'Time'], ['InsertionSort 500', tempoISP]]
    file = open('timePython500.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerows(table)


if __name__ == "__main__":
    main()
