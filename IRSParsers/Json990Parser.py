from IRSParsers.ParserFactory import ParserFactory
class Json990Parser:
    def __init__(self,json_990_filing:dict) -> None:
        self.__json_990_filing = json_990_filing
        self.__parsed_990_filing = {} 
        self.__parse990Filing()

    def __parse990Filing(self):
        filing = self.__json_990_filing
        if(filing == None):
            self.__parsed_990_filing = {}
            return
        scheduleResults = []
        
        for schedule in filing:
            parserStrategy = ParserFactory().createParserStrategy(schedule)
            scheduleResults.append(parserStrategy.parse(schedule))

        for schedule in scheduleResults:
            self.__parsed_990_filing.update(schedule)

    def getParsed990Filing(self):
        return self.__parsed_990_filing





        