import pickle
import time
import tensorflow as tf
from alexnet import AlexNet
import csv

nb_classes = 43
epochs = 1
batch_size = 128



def createDictCSV(fileName="", dataDict={}):
    with open(fileName, "w") as csvFile:
        csvWriter = csv.writer(csvFile)
        for i,j in dataDict.items():
            csvWriter.writerow([i,j])
        csvFile.close()



with open('./train.p', 'rb') as f:
    data = pickle.load(f)
    createDictCSV("data_csv.csv", data)
    print(len((data['labels'])))