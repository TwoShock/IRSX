import pickle


def pickleObject(object, outputFilePath) -> None:
    with open(outputFilePath, 'wb') as file:
        pickle.dump(obj=object, file=file)


def loadPickleObject(inputFilePath):
    object = None
    with open(inputFilePath,'rb') as file:
        object = pickle.load(file=file)
    return object
