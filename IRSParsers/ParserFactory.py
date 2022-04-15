from IRSParsers.IRS990PFParser import IRS990PFParser
from IRSParsers.IRSScheduleIParser import IRSScheduleIParser
from IRSParsers.NullParserStrategy import NullParserStrategy
from IRSParsers.ReturnHeader990xParser import ReturnHeader990xParser
class ParserFactory:
    def createParserStrategy(self,schedule:dict):
        scheduleName = schedule['schedule_name']
        if scheduleName == "ReturnHeader990x":
            return ReturnHeader990xParser()
        elif scheduleName == "IRS990PF":
            return IRS990PFParser()
        elif scheduleName =="IRS990ScheduleI":
            return IRSScheduleIParser()
        else:
            return NullParserStrategy()
        