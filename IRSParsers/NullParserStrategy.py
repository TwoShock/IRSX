from IRSParsers.ParserStrategy import ParserStrategy
class NullParserStrategy(ParserStrategy):
    def parse(self,schedule:dict):
        return {}

