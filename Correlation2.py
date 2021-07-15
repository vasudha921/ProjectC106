import pandas 
import csv
import numpy as np
import plotly.express as px


def getSource(data_path):
    CoffeeInml = []
    SleepInhours = []
    with open ('Coffee vs Sleep.csv') as f:
        csvReader = csv.DictReader(f)
        for i in csvReader: 
            CoffeeInml.append(float(i['Coffee in ml']))
            SleepInhours.append(float(i['sleep in hours']))
    return{'x': CoffeeInml, 'y': SleepInhours}

def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0,1])

def setup():
    data_path = "Coffee vs Sleep.csv"
    data_source= getSource(data_path)
    findCorrelation(data_source)

setup()