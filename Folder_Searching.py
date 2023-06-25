import os
from csv import DictReader, DictWriter
from collections import defaultdict
import pandas as pd
with(
    open("E:/MY-GRAD/CNN-LSTM/FullCollected.csv", "a") as out
):
    writer = DictWriter(
        out, ['X', 'Y', 'Z', 'Activity'], lineterminator='\n')
    writer.writeheader()
    # mapping: dict[int, int] = {'walking.csv': 0, 'crouching.csv': 1,  'running.csv': 2, 'jumping.csv': 3,  'setting_down.csv': 18, 'standing.csv': 19}

    # mapping: dict[int, int] = {'walking.csv': 0,
    #                            'crouching.csv': 1, 'running.csv': 2, 'jumping.csv': 3, 'carrying.csv': 4, 'checking_time.csv': 5, 'closing.csv': 6, 'entering.csv': 7, 'exiting.csv': 8, 'fall.csv': 9, 'kicking.csv': 10, 'loitering.csv': 11,
    #                            'looking_around.csv': 12, 'opening.csv': 13, 'picking_up.csv': 14, 'pointing.csv': 15, 'pulling.csv': 16, 'pushing.csv': 17, 'setting_down.csv': 18, 'standing.csv': 19, 'talking.csv': 20, 'talking_on_phone.csv': 21,
    #                            'throwing.csv': 22, 'transferring_object.csv': 23, 'using_phone.csv': 24, 'waving_hand.csv': 25}

    # targeted_files = ['crouching.csv', 'running.csv', 'walking.csv', 'jumping.csv', 'carrying.csv', 'checking_time.csv', 'closing.csv', 'entering.csv', 'exiting.csv/', 'fall.csv', 'kicking.csv', 'loitering.csv', 'looking_around.csv',
    #                   'opening.csv', 'picking_up.csv', 'pointing.csv', 'pulling.csv', 'pushing.csv', 'setting_down.csv', 'standing.csv', 'talking.csv', 'talking_on_phone.csv', 'throwing.csv', 'transferring_object.csv', 'using_phone.csv', 'waving_hand.csv']

    # targeted_files = ['crouching.csv',
    #                 'running.csv', 'walking.csv', 'standing.csv']

    files = os.listdir("E:/MY-GRAD/CNN-LSTM/New folder/collected")
    # # myfile = 'crouching.csv'
    ct = 0
    # keys = ['Time_stamp', 'X', 'Y', 'Z',
    #         'Activity', 'Subject', 'Scene', 'SESSION']
    for filename_0 in files:
        # ct += 1
        # print(filename_0)

        # filename = 'subject'+str(ct)
        # if ct >= 8 and ct < 11:
        #     new_files = os.listdir(
        #         "E:/MY-GRAD/CNN-LSTM/MMact dataset/acc_phone_clip/"+filename)
        #     for filename_1 in new_files:
        #         new_files_1 = os.listdir(
        #             "E:/MY-GRAD/CNN-LSTM/MMact dataset/acc_phone_clip/"+filename+"/"+filename_1)
        #         for filename_2 in new_files_1:
        #             new_files_2 = os.listdir(
        #                 "E:/MY-GRAD/CNN-LSTM/MMact dataset/acc_phone_clip/"+filename+"/"+filename_1+"/"+filename_2)
        #             for filename_3 in new_files_2:
        #                 if filename_3 in targeted_files:
        #                     Activity = mapping[filename_3]
        #                     foldername = filename_3[:-4]
        #                     Session = filename_2
        #                     scene = filename_1

        #                     # print(ct)
        # with (

        #     open("E:/MY-GRAD/CNN-LSTM/New folder/collected"+filename_0, "r") as csvfile,
        #     # open("E:/MY-GRAD/CNN-LSTM/collected.csv", "a") as out,
        #     # open("E:/MY-GRAD/CNN-LSTM/"+filename+"_"+filename_1+"_"+filename_2+"_"+filename_3, "w") as out,
        #     # open("E:/MY-GRAD/CNN-LSTM/ALL26.CSV", "a") as out,
        # ):
        mypath = "E:/MY-GRAD/CNN-LSTM/New folder/collected/"+filename_0
        columns = ['X', 'Y', 'Z', 'SUBJECT', 'ACT']
        ACC_df = pd.read_csv(
            mypath, header=None, names=columns)
        clone = list()
        # print(ACC_df)
        num = ACC_df.shape[0]
        for i in range(num):

            # print()
            # #                             # clone[0][0] = 1
            # #                             # clone.keys()
            # #                             # clone = list[]
            # # clone.append(
            # #     ("Time_stamp", row[reader.fieldnames[0]]))
            #     print(row.items())
            clone.append(
                ("X", ACC_df['X'][i]))
            clone.append(
                ("Y", ACC_df['Y'][i]))
            clone.append(
                ("Z", ACC_df['Z'][i]))
            clone.append(
                ("Activity", ACC_df['ACT'][i]))
            # # clone.append(("Activity", Activity))
            # # clone.append(("Subject", filename))
            # # clone.append(("Scene", scene))
            # # clone.append(("SESSION", Session))
            final = dict(clone)
            # # print(clone)
            writer.writerow(final)

        # print(ACC_df['X'])

        # writer = DictWriter(
        #     out, ['Time_stamp', 'X', 'Y', 'Z', 'Activity', 'Subject', 'Scene', 'SESSION'], lineterminator='\n')
        # writer.writeheader()
        # reader = DictReader(ACC_df)

        # #                         pb = 0
        # for row in reader:
        #     #                             # print(row)
        #     #                             # khaled = list(row.items())
        #     clone = list()
        # #                             # clone[0][0] = 1
        # #                             # clone.keys()
        # #                             # clone = list[]
        # # clone.append(
        # #     ("Time_stamp", row[reader.fieldnames[0]]))
        #     print(row.items())
        # # clone.append(
        # #     ("X", row[reader.fieldnames[0]]))
        # # clone.append(
        # #     ("Y", row[reader.fieldnames[1]]))
        # # clone.append(
        # #     ("Z", row[reader.fieldnames[2]]))
        # # clone.append(("Activity", Activity))
        # # clone.append(("Subject", filename))
        # # clone.append(("Scene", scene))
        # # clone.append(("SESSION", Session))
        # final = dict(clone)
        # # print(clone)
        # writer.writerow(final)
        # ct += 1
        # # print(ct)
    # print(ct/8)
