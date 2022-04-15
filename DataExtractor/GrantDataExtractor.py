import os
from irsx.xmlrunner import XMLRunner
from IRSParsers.Json990Parser import Json990Parser
from utils.pickle_utils import loadPickleObject
import time


"""
This class will extract the grant data for all filings of a given ein if they exist.
"""


class GrantDataExtractor:
    dir = os.path.dirname(__file__)
    lookup = loadPickleObject(
        os.path.join(dir, '../pickle/einLookup.pkl'))
    def __init__(self, ein) -> None:
        self.__ein = ein
        self.__objectIDs = []
        self.__filings = []
        if(ein in GrantDataExtractor.lookup.keys()):
            self.__objectIDs = GrantDataExtractor.lookup[self.__ein]
            self.__filings = self.__extractFilings()

    def __extractFilings(self):
        parsedFilings = []
        for objectID in self.__objectIDs:
            filing = XMLRunner().run_filing(objectID).get_result()
            parsedFilings.append(Json990Parser(filing).getParsed990Filing())
        return parsedFilings

    def __filterAndReturnFilingData(self, filing: dict):
        currentFilingData = {}
        currentFilingData['tax_year'] = filing.get('tax_year')
        currentFilingData['object_id'] = filing.get('object_id')
        currentFilingData['doner_name'] = filing.get('buisness_name_line_1')
        currentFilingData['doner_ein'] = filing.get('ein')
        if('grants_to_organizations_in_the_us' in filing.keys()):
            currentFilingData['grants'] = filing['grants_to_organizations_in_the_us']
        else:
            currentFilingData['grants'] = []
        return currentFilingData

    def __filterGrantDataToRemoveEmptyGrants(self, grantData: list) -> list:
        filteredGrantData = []
        for grant in grantData:
            if(len(grant['grants']) != 0):
                filteredGrantData.append(grant)
        return filteredGrantData

    def getObjectIDCount(self):
        return len(self.__objectIDs)

    def getGrantData(self) -> list:
        grantData = []
        for filing in self.__filings:
            if(len(list(filing.keys())) != 0):
                grantData.append(self.__filterAndReturnFilingData(filing))
        grantData = self.__filterGrantDataToRemoveEmptyGrants(grantData)
        return grantData
