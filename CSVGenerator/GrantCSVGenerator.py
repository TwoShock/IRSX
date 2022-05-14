from fileinput import filename
import pandas as pd
from DataExtractor.GrantDataExtractor import GrantDataExtractor
from utils.pickle_utils import loadPickleObject
import os
import time
import csv
"""
Takes in the list of grants extracted from GrantDataExtractor and generates a CSV file from the grant data.
"""


class GrantCSVGenerator:
    fieldsToWriteFromCurrentYear = [
        'tax_year', 'object_id', 'doner_name', 'doner_ein']
    fieldsToWriteFromGrant = ['recepient_name', 'recepient_address', 'zip_code', 'street_abreviation_code',
                              'irc_section_description', 'recepient_ein', 'recepient_cash_grant_amount', 'purpose_of_grant_txt']
    filedsToWriteForApprovedPaid = ['recepient_name', 'recepient_address', 'city_num','zip_code', 'street_abreviation_code','recepient_cash_grant_amount', 'purpose_of_grant_txt']
    def __init__(self, einList: list) -> None:
        self.__einList = einList
    def write990PFSkedIncrementally(self,pathToPaid,pathToApproved):
        self.__writePaidApprovedGrantMetaData(pathToPaid)
        self.__writePaidApprovedGrantMetaData(pathToApproved)
        for ein in self.__einList:
            grantData = GrantDataExtractor(ein).getGrantData()
            with open(pathToPaid,"a") as file:
                for currentYearGrants in grantData:
                    for grant in currentYearGrants['GrantsPaidDuringYear']:
                        for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                            file.write(f'{currentYearGrants.get(field)},')
                        for field in GrantCSVGenerator.filedsToWriteForApprovedPaid:
                            file.write(f'{grant.get(field)},' )
                        file.write('\n')
            with open(pathToApproved,"a") as file:
                for currentYearGrants in grantData:
                    for grant in currentYearGrants['GrantsApprovedForFuture']:
                        for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                            file.write(f'{currentYearGrants.get(field)},')
                        for field in GrantCSVGenerator.filedsToWriteForApprovedPaid:
                            file.write(f'{grant.get(field)},' )
                        file.write('\n')
    def __writePaidApprovedGrantMetaData(self,path):
        with open(path,'w') as file:
            for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                file.write(f'{field},')
            for field in GrantCSVGenerator.filedsToWriteForApprovedPaid:
                file.write(f'{field},' )
            file.write('\n')
    def writeSkedICSVIncrementally(self, path):
        self.__writeSkedICSVMetaData(path)
        for i, ein in enumerate(self.__einList):
            grantDataExtractor = GrantDataExtractor(ein=ein)
            if(len(grantDataExtractor.getGrantData()) != 0):
                self.writeSkedIGrantDataToCSV(
                    grantDataExtractor.getGrantData(), path)
            print(f'{(i/len(self.__einList))*100}% completed...\n\n')

    def __writeSkedICSVMetaData(self, path):
        with open(path, 'w') as file:
            for field in GrantCSVGenerator.fieldsToWriteFromCurrentYear:
                file.write(f'{field},')
            for i, field in enumerate(GrantCSVGenerator.fieldsToWriteFromGrant):
                if(i == len(GrantCSVGenerator.fieldsToWriteFromGrant)-1):
                    file.write(f'{field}\n')
                else:
                    file.write(f'{field},')

    def writeSkedIGrantDataToCSV(self, grantData, path):
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