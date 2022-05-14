from ast import parse
from IRSParsers.ParserStrategy import ParserStrategy


class IRSScheduleIParser(ParserStrategy):
    IRSScheduleIObjectLookupMap = {
        "recepient_name": "RcpntBsnssNm_BsnssNmLn1Txt",
        "recepient_address": "USAddrss_AddrssLn1Txt",
        "city_num": "USAddrss_CtyNm",
        "street_abreviation_code": "USAddrss_SttAbbrvtnCd",
        "zip_code": "USAddrss_ZIPCd",
        "recepient_ein": "RcpntTbl_RcpntEIN",
        "irc_section_description": "RcpntTbl_IRCSctnDsc",
        "recepient_cash_grant_amount": "RcpntTbl_CshGrntAmt",
        "purpose_of_grant_txt": "RcpntTbl_PrpsOfGrntTxt"
    }
    def __init__(self) -> None:
        super().__init__()

    def parseGrant(self, grant: dict):
        parsedGrant = {}
        for result_key, irs_sked_i_key in IRSScheduleIParser.IRSScheduleIObjectLookupMap.items():
            try:
                parsedGrant[result_key] = grant[irs_sked_i_key]
            except:
                parsedGrant[result_key] = None
        return parsedGrant

    def parse(self, schedule: dict):
        parsedResult = {"grants_to_organizations_in_the_us": []}
        grants = schedule['groups']
        if('SkdIRcpntTbl' in grants):
            grants = schedule['groups']['SkdIRcpntTbl']
            for grant in grants:
                parsedResult["grants_to_organizations_in_the_us"].append(
                    self.parseGrant(grant))
        return parsedResult
