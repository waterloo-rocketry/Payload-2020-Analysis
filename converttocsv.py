import pandas as pd

def ifnum(string):
    try:
        new = float(string)
        return True
    except:
        return False

def main(filepath):
    peaks = []
    signals = []
    times = []

    try:
        with open(filepath, 'r') as log:
            lines = log.readlines()
            # load the lines into a buffer variable

            for line in lines:
                data = line.split()
                data = list(filter(ifnum, data))
                peaks.append(data[0])
                signals.append(data[1])
                times.append(data[2])
                

        csvfmt = {
                "Peak":peaks,
                "Signal":signals,
                "Time":times,
                }



        df = pd.DataFrame(csvfmt)
        csv_data = df.to_csv('./Photodiode_Test_Data/based.csv', header=False, index=False, sep=':')

    except:
        print("Error opening file.")
