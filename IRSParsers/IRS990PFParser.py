from IRSParsers.ParserStrategy import ParserStrategy


class IRS990PFParser(ParserStrategy):
    grantPaidDuringYearMap = {
        "recepient_name": "RcpntBsnssNm_BsnssNmLn1Txt",
        "recepient_address": "RcpntUSAddrss_AddrssLn1Txt",
        "city_num": "RcpntUSAddrss_CtyNm",
        "street_abreviation_code": "RcpntUSAddrss_SttAbbrvtnCd",
        "zip_code": "RcpntUSAddrss_ZIPCd",
        "recepient_cash_grant_amount": "GrntOrCntrbtnPdDrYr_Amt",
        "purpose_of_grant_txt": "GrntOrCntrbtnPdDrYr_GrntOrCntrbtnPrpsTxt"
    }
    grantApprovedForFutureMap = {
        "recepient_name": "RcpntBsnssNm_BsnssNmLn1Txt",
        "recepient_address": "RcpntUSAddrss_AddrssLn1Txt",
        "recepient_address": "RcpntUSAddrss_AddrssLn1Txt",
        "city_num": "RcpntUSAddrss_CtyNm",
        "street_abreviation_code": "RcpntUSAddrss_SttAbbrvtnCd",
        "zip_code": "RcpntUSAddrss_ZIPCd",
        "recepient_cash_grant_amount": "GrntOrCntrApprvFrFt_Amt",
        "purpose_of_grant_txt": "GrntOrCntrApprvFrFt_GrntOrCntrbtnPrpsTxt"
    }

    def __init__(self) -> None:
        super().__init__()

    def __getGrantSectionFromSectionName(self, sectionName: str):
        if(sectionName == 'PFGrntOrCntrbtnPdDrYr'):
            return IRS990PFParser.grantPaidDuringYearMap
        else:
            return IRS990PFParser.grantApprovedForFutureMap

    def __parseGrants(self, schedule: dict, section: str):
        grantsSection = schedule['groups'].get(section)
        results = []
        if(grantsSection == None):
            return results
        for grant in grantsSection:
            results.append({key: grant.get(
                val) for key, val in self.__getGrantSectionFromSectionName(section).items()})
        return results

    def parse(self, schedule: dict):
        parsedResults = {}
        grantsPaidDuringYear = self.__parseGrants(
            schedule, 'PFGrntOrCntrbtnPdDrYr')
        grantsApprovedForFuture = self.__parseGrants(
            schedule, 'PFGrntOrCntrApprvFrFt')
        parsedResults['GrantsPaidDuringYear'] = grantsPaidDuringYear
        parsedResults['GrantsApprovedForFuture'] = grantsApprovedForFuture
        return parsedResults
