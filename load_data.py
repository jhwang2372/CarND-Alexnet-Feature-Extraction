import pickle
import time
import tensorflow as tf
from alexnet import AlexNet
import csv

nb_classes = 43
epochs = 1
batch_size = 128
labels = []


def createDictCSV(fileName="", dataDict={}):
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for i,j in dataDict.items():
            if i == 'labels':
                labels = j
                for index, value in enumerate(labels):
                    if value:
                        labels[index] = 1
                j = labels
            csvWriter.writerow([i,j])
        csvFile.close()



with open('./train.p', 'rb') as f:
    data = pickle.load(f)
    createDictCSV("data_csv.csv", data)
    print(data['labels'])