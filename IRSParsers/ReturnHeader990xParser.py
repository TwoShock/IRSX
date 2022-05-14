from ast import parse
from IRSParsers.ParserStrategy import ParserStrategy


class ReturnHeader990xParser(ParserStrategy):
    returnHeaderObjectMap = {
        'ein': 'ein',
        'object_id': 'object_id',
        'tax_year': 'RtrnHdr_TxYr',
        'buisness_name_line_1': 'BsnssNm_BsnssNmLn1Txt',
    }
    def __init__(self) -> None:
        super().__init__()

    def parse(self, schedule: dict):
        parsedResult = {}
        scheduleParts = schedule["schedule_parts"]["returnheader990x_part_i"]
        for result_key,irs_990_key in ReturnHeader990xParser.returnHeaderObjectMap.items():
            try:
                parsedResult[result_key] = scheduleParts[irs_990_key]
            except:
                parsedResult[result_key] = None
        return parsedResult
