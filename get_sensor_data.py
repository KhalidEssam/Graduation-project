import random
import asyncio
from itertools import count
from multiprocessing.connection import wait
from re import L
from sensordroid import Client
import time
from xlwt import *
import csv
from datetime import datetime
import os
from csv import DictReader, DictWriter
from collections import defaultdict
from Random_forest_test import loader
import pandas as pd
from time import sleep
with(
    open("E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv", "a") as out
):
    clone = list()
    writer = DictWriter(
        out, ['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)', 'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'], lineterminator='\n')
    writer.writeheader()

    def devicesDiscoveredEventHandler(devices):
        print(devices)

        if len(devices) > 0:
            client = Client(devices[0])

            client.connectionUpdated = connectionUpdatedEventHandler
            client.sensorsSampleRate = 10
            client.sensorsReceived = sensorsReceivedEventHandler
            client.imageReceived = cameraReceivedEventHandler

            client.cameraResolution = 13

            client.connect()

    def connectionUpdatedEventHandler(sender, msg):
        if sender is not None:
            if sender.connected:
                print("Connected")
            else:
                print("Disonnected")
    #

    l = 1
    c = 1

    k = [1]

    def getnextval():
        k.append(0)
        return len(k)-1
    k2 = [1]

    def getnextval2():
        k2.append(0)
        return len(k2)-1

    def sensorsReceivedEventHandler(sender, dataCurrent):

        # if writer.fieldnames is None:
        #     print('yes')
        #     writer = DictWriter(
        #         out,  fieldnames=['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)', 'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'], lineterminator='\n')
        #     writer.writeheader()
        data = dataCurrent.Acceleration.Values.AsString
        data1 = dataCurrent.Orientation.Values.AsString
        y1, y2, y3 = data.split()
        y11, y22, y33 = data1.split()
        # print(data, "dddddddddddd", data1)
        time_now = datetime.now().strftime("%H:%M:%S")
        b = getnextval()
        # print(b)
        clone.append(
            ("Gyroscope X (deg/s)", y11[:-1]))
        clone.append(
            ("Gyroscope Y (deg/s)", y22[:-1]))
        clone.append(
            ("Gyroscope Z (deg/s)", y33[:-1]))
        clone.append(
            ("Accelerometer X (g)", y1[:-1]))
        clone.append(
            ("Accelerometer Y (g)", y2[:-1]))
        clone.append(
            ("Accelerometer Z (g)", y3[:-1]))
        final = dict(clone)
        # print(writer)
        if b % 300 == 0:

            print(b)
            loader.Livedemo()
            sender.sensorsSampleRate = 10000
            with(open("E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv", "w", newline='') as out
                 ):
                # if writer.fieldnames is None:
                #     print('yes')
                # writer = DictWriter(
                #     out,  fieldnames=['Gyroscope X (deg/s)', 'Gyroscope Y (deg/s)', 'Gyroscope Z (deg/s)', 'Accelerometer X (g)', 'Accelerometer Y (g)', 'Accelerometer Z (g)'], lineterminator='\n')
                # writer.writeheader()

                print("**************")
                sender.sensorsSampleRate = 10
            # sleep(60)
            # sender.sensorsSampleRate = 100000

        writer.writerow(final)

    def cameraReceivedEventHandler(sender, image):
        # Process image data bytes
        pass

    Client.devicesDiscovered = devicesDiscoveredEventHandler
    Client.startDiscovery()

    key = input("Press ENTER to exit\n")
    Client.closeAll()


# df = pd.read_csv("MYprojectssss.csv")
# loader.Livedemo("MYprojectssss.csv")

# with(open("E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv", "w") as out
#      ):
#     print("done")
os.remove("E:/MY-GRAD/CNN-LSTM/MYprojectssss.csv")
