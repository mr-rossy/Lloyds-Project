import pandas as pd
import matplotlib.pyplot as plt
import os


files = [f for f in os.listdir('.') if os.path.isfile(f)]

for f in files:
    filename, ext = os.path.splitext(f)
    if ext == '.csv':
        tempdata = pd.read_csv(f)
        tempdata.insert(1,"Ticker", filename)
        tempdata["Change in Share Price"] = tempdata["Open"] - tempdata["Close"]
        tempdata.to_csv("{}".format(f))

        

        



               

    

  