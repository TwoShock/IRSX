from matplotlib.pyplot import axis
from numpy import var
import numpy
import pandas as pd
import pickle
from bs4 import BeautifulSoup
from urllib.request import urlopen

from spacy import load
url = f'http://www.irsx.info/metadata/forms.html'
baseUrl = f'http://www.irsx.info'
soup = BeautifulSoup(urlopen(url).read(), 'html.parser')


def getLinksFromParagraphWithClass(classValue):
    targetParagraphs = soup.find_all("p", {"class": classValue})
    links = []
    for p in targetParagraphs:
        links.append(p.a['href'])
    return links


def getAllPagesFromHomePage():
    return getLinksFromParagraphWithClass("h3 indent1")+getLinksFromParagraphWithClass("h4 indent2")


def getTextFromParagraphWithClass(document, classValue):
    targetParagraphs = document.find_all("p", {"class": classValue})
    variableNames = []
    for p in targetParagraphs:
        variableNames.append(p.a.text)
    return variableNames


def extractXpathsFromPage(document):
    return getTextFromParagraphWithClass(document, "lead indent2")
print(len(getAllPagesFromHomePage()))


def extractVariablesFromPage(document):
    return getTextFromParagraphWithClass(document, "h3 indent1")


def extractVariablesAndXpathsFromPage(page_url):
    currentDocument = BeautifulSoup(urlopen(page_url).read(), 'html.parser')
    return extractVariablesFromPage(currentDocument), extractXpathsFromPage(currentDocument)


def extractAllVariablesAndXpathsFromSite():
    pages = getAllPagesFromHomePage()
    variablesMergedList = []
    xpathMergedList = []
    for i, page in enumerate(pages):
        currentUrl = f'{baseUrl}{page}'
        print(f'{i}/{len(pages)}')
        print(f'extracting data from {currentUrl}...')
        variables, xpaths = extractVariablesAndXpathsFromPage(currentUrl)
        variablesMergedList = variablesMergedList + variables
        xpathMergedList = xpathMergedList + xpaths
    return variablesMergedList, xpathMergedList


def saveAllVariablesAndXpaths():
    variables, xpaths = extractAllVariablesAndXpathsFromSite()
    variableOutFile = open("variables.pkl", 'wb')
    xpathsOutFile = open("xpaths.pkl", 'wb')
    pickle.dump(variables, variableOutFile)
    pickle.dump(xpaths, xpathsOutFile)
    variableOutFile.close()
    xpathsOutFile.close()


def loadAllVariablesAndXpaths():
    return pickle.load(open('variables.pkl', 'rb')), pickle.load(open('xpaths.pkl', 'rb'))

variables,xpaths = loadAllVariablesAndXpaths()
df = pd.read_csv('metadata.csv')
def storeJsonVariableName(currentXpath):
    for i,xpath in enumerate(xpaths):
        if(f'/Return/ReturnData{xpath}' == currentXpath):
            return variables[i]
        else:
            numpy.nan
print(df.columns)
def dummy(x):
    print(x)
    return 1
df['json_variable_name'] = df.apply(lambda x: storeJsonVariableName(x.xpath),axis=1) 
pd.DataFrame.to_csv(df,'metadata_with_json_variable_names.csv',index=False)

# h3 indent1

# lead indent2
