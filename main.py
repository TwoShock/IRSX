from textwrap import indent
import threading
import pandas as pd
import numpy as np
from CSVGenerator.GrantCSVGenerator import GrantCSVGenerator
from GrantGraphVisualizer.GrantGraphVisualizer import GrantGraphVisualizer
from IRSParsers.Json990Parser import Json990Parser
from utils.pickle_utils import *
from DataExtractor.GrantDataExtractor import GrantDataExtractor


def fetchObjectIdList(path_to_index_csv: str):
    df = pd.read_csv(path_to_index_csv)
    return df["OBJECT_ID"].tolist()


def buildEinToObjectIdLookupMap():
    yearList = ['2013', '2014', '2015', '2016',
                '2017', '2018', '2019', '2020', '2021']
    einToObjectIdMap = {}
    for year in yearList:
        df = pd.read_csv(f'./index/index_{year}.csv')
        einList = df['EIN'].tolist()
        objectIdList = df['OBJECT_ID'].tolist()
        for i, ein in enumerate(einList):
            if(ein not in einToObjectIdMap.keys()):
                einToObjectIdMap[ein] = []
            einToObjectIdMap[ein].append(objectIdList[i])
    return einToObjectIdMap


lookup = loadPickleObject('./pickle/einLookup.pkl')

einList1 = pd.read_csv('nccs_pd_ein.csv')['ein'].tolist()
einList2 = pd.read_csv('nccs_Philantropy_ein.csv')['ein'].tolist()

i1 = np.intersect1d(list(lookup.keys()), einList1)
i2 = np.intersect1d(list(lookup.keys()), einList2).tolist()


def generateCSV(inputList, start, end, outputPath):
    GrantCSVGenerator(inputList[start:end]).generateCSV(outputPath)
def generateCSVIncrementally(inputList, start, end, outputPath):
    GrantCSVGenerator(inputList[start:end]).generateCSVIncrementally(outputPath)
generateCSVIncrementally(i2,0,100,'test_out.csv')

