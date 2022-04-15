from fileinput import filename
import pandas as pd
from DataExtractor.GrantDataExtractor import GrantDataExtractor
from utils.pickle_utils import loadPickleObject
import os
import time
"""
Takes in the list of grants extracted from GrantDataExtractor and generates a CSV file from the grant data.
"""


class GrantCSVGenerator:
    fieldsToWriteFromCurrentYear = [
        'tax_year', 'object_id', 'doner_name', 'doner_ein']
    fieldsToWriteFromGrant = ['recepient_name', 'recepient_address', 'zip_code', 'street_abreviation_code',
                              'irc_section_description', 'recepient_ein', 'recepient_cash_grant_amount', 'purpose_of_grant_txt']

    def __init__(self, einList: list) -> None:
        self.__einList = einList

    def __extractGrantDataListFromEinList(self):
        grantDataList = []
        for i, ein in enumerate(self.__einList):
            grantDataExtractor = GrantDataExtractor(ein=ein)
            if(len(grantDataExtractor.getGrantData()) != 0):
                grantDataList.extend(grantDataExtractor.getGrantData())
            print(f'{(i/len(self.__einList))*100}% completed...\n\n')
        return grantDataList

    def writeCSVIncrementally(self, path):
        self.__writeCSVMetaData(path)
        for i, ein in enumerate(self.__einList):
            grantDataExtractor = GrantDataExtractor(ein=ein)
            if(len(grantDataExtractor.getGrantData()) != 0):
                self.writeGrantDataToCSV(
                    grantDataExtractor.getGrantData(), path)
            print(f'{(i/len(self.__einList))*100}% completed...\n\n')

    def __writeCSVMetaData(self, path):
        with open(path, 'w') as file:
            for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                file.write(f'{field},')
            for i, field in enumerate(GrantCSVGenerator.fieldsToWriteFromGrant):
                if(i == len(GrantCSVGenerator.fieldsToWriteFromGrant)-1):
                    file.write(f'{field}\n')
                else:
                    file.write(f'{field},')

    def writeGrantDataToCSV(self, grantData, path):
        with open(path, 'a') as file:
            for currentYearGrants in grantData:
                for grant in currentYearGrants['grants']:
                    for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                        file.write(f'{currentYearGrants.get(field)},')
                    for i, field in enumerate(GrantCSVGenerator.fieldsToWriteFromGrant):
                        if(i == len(GrantCSVGenerator.fieldsToWriteFromGrant)-1):
                            file.write(f'{grant.get(field)}\n')
                        else:
                            file.write(f'{grant.get(field)},')

    def generateCSV(self, path: str):
        csvGrantList = []
        for currentYearGrants in self.__grantDataList:
            for grant in currentYearGrants['grants']:
                csvGrantList.append({
                    'tax_year': currentYearGrants.get('tax_year'),
                    'object_id': currentYearGrants.get('object_id'),
                    'doner_name': currentYearGrants.get('doner_name'),
                    'doner_ein': currentYearGrants.get('doner_ein'),
                    'recepient_name': grant.get('recepient_name'),
                    'recepient_address': grant.get('recepient_address'),
                    'recepient_zip': grant.get('zip_code'),
                    'recepient_street_abreviation_code': grant.get('street_abreviation_code'),
                    'irc_section_description': grant.get('irc_section_description'),
                    'recepient_ein': grant.get('recepient_ein'),
                    'recepient_cash_grant_amount': grant.get('recepient_cash_grant_amount'),
                    'purpose_of_grant_txt': grant.get('purpose_of_grant_txt')
                })
        df = pd.DataFrame(csvGrantList)
        pd.DataFrame.to_csv(df, path)
