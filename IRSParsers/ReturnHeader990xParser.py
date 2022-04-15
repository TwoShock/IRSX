from ast import parse
from IRSParsers.ParserStrategy import ParserStrategy


class ReturnHeader990xParser(ParserStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.returnHeaderObjectMap = {
            'ein': 'ein',
            'object_id': 'object_id',
            'tax_year': 'RtrnHdr_TxYr',
            'preparer_email': 'PrprrPrsn_EmlAddrssTxt',
            'filer_buisness_name_control_txt': 'Flr_BsnssNmCntrlTxt',
            'filing_security_information_federal_original_submission_id_date': 'FlngScrtyInfrmtn_FdrlOrgnlSbmssnIdDt',
            'filing_security_information_ipd_date': 'FlngScrtyInfrmtn_IPDt',
            'disaster_relief_txt': 'RtrnHdr_DsstrRlfTxt',
            'originator_group_practitioner_pin_group_efin': 'PrcttnrPIN_EFIN',
            'preparer_phone_number': 'PrprrPrsn_PhnNm',
            'preparer_firm_group_usaddress_line_2': 'PrprrUSAddrss_AddrssLn2Txt',
            'filer_state_abbreviation_code': 'USAddrss_SttAbbrvtnCd',
            'preparer_firm_group_usaddress_line_1': 'PrprrUSAddrss_AddrssLn1Txt',
            'buisness_name_line_2': 'BsnssNm_BsnssNmLn2Txt',
            'preparer_firm_group_foreign_address_country_code': 'PrprrFrgnAddrss_CntryCd',
            'preparer_self_employed_ind': 'PrprrPrsn_SlfEmplydInd',
            'originator_group_practitioner_pin': 'PrcttnrPIN_PIN',
            'preparer_ssn': 'PrprrPrsn_SSN',
            'originator_group_originator_type_code': 'Orgntr_OrgntrCd',
            'buisness_name_line_1': 'BsnssNm_BsnssNmLn1Txt',
            'filer_city_name': 'USAddrss_CtyNm',
            'buisness_officer_group_phone_number': 'BsnssOffcr_PhnNm',
            'filer_foreign_address_province_or_state_name': 'FrgnAddrss_PrvncOrSttNm',
            'business_officer_group_tax_payer_pin': 'BsnssOffcr_TxpyrPIN',
            'tax_period_start_date': 'RtrnHdr_TxPrdBgnDt',
            'filer_ein': 'Flr_EIN',
            'filer_us_address_address_line_1': 'USAddrss_AddrssLn1Txt',
            'return_type_code': 'RtrnHdr_RtrnCd',
            'filer_us_address_line_2': 'USAddrss_AddrssLn2Txt',
            'filer_foreing_address_city_name': 'FrgnAddrss_CtyNm',
            'filing_security_information_at_submission_creation_device_id': 'FlngScrtyInfrmtn_AtSbmssnCrtnDvcId',
            'preparer_foreign_address_foreign_postal_code': 'PrprrFrgnAddrss_FrgnPstlCd',
            'filing_security_information_filing_licesnse_type_code': 'FlngScrtyInfrmtn_FlngLcnsCd',
            'tax_period_end_date': 'RtrnHdr_TxPrdEndDt',
            'preparer_foreign_address_line_2': 'PrprrFrgnAddrss_AddrssLn2Txt',
            'preparer_firm_ein': 'PrprrFrm_PrprrFrmEIN',
            'preparer_buisness_name_line_2': 'PrprrFrmNm_BsnssNmLn2Txt',
            'return_creation_date': 'RtrnHdr_RtrnTs',
            'buisness_officer_group_person_title': 'BsnssOffcr_PrsnTtlTxt',
            'isp_number': 'RtrnHdr_ISPNmt',
            'preparer_ptin': 'PrprrPrsn_PTIN',
            'preparer_buisness_name_line_1': 'PrprrFrmNm_BsnssNmLn1Txt',
            'preparer_us_address_city_name': 'PrprrUSAddrss_CtyNm',
            'filling_security_information_at_submission_filing_device_id': 'FlngScrtyInfrmtn_AtSbmssnFlngDvcId',
            'preparer_foreign_address_line_1': 'PrprrFrgnAddrss_AddrssLn1Txt',
            'preparer_us_address_state_abbreviation_code': 'PrprrUSAddrss_SttAbbrvtnCd',
            'preparer_preparation_date': 'PrprrPrsn_PrprtnDt',
            'preparer_foreign_address_province_or_state_name': 'PrprrFrgnAddrss_PrvncOrSttNm',
            'filer_foreign_address_line_1': 'FrgnAddrss_AddrssLn1Txt',
            'filer_foreign_postal_code': 'FrgnAddrss_FrgnPstlCd',
            'preparer_person_name': 'PrprrPrsn_PrprrPrsnNm',
            'originator_group_efin': 'Orgntr_EFIN',
            'filer_in_care_of_name': 'Flr_InCrOfNm',
            'software_version_number': 'RtrnHdr_SftwrVrsnNm',
            'filing_security_information_ipv4_address': 'IPAddrss_IPv4AddrssTxt',
            'filing_security_information_iptimezone_code': 'FlngScrtyInfrmtn_IPTmznCd',
            'signature_option_code': 'RtrnHdr_SgntrOptnCd',
            'preparer_us_address_zip_code': 'PrprrUSAddrss_ZIPCd',
            'filing_security_information_iptm': 'FlngScrtyInfrmtn_IPTm',
            'filer_us_address_zip_code': 'USAddrss_ZIPCd',
            'buisness_officer_email_address': 'BsnssOffcr_EmlAddrssTxt',
            'buisness_officer_person_name': 'BsnssOffcr_PrsnNm',
            'pin_entered_by_code': 'RtrnHdr_PINEntrdByCd',
            'filing_security_information_ipv6_address': 'IPAddrss_IPv6AddrssTxt',
            'filer_foreign_address_line_2': 'FrgnAddrss_AddrssLn2Txt',
            'filer_phone_number': 'Flr_PhnNm',
            'software_id': 'RtrnHdr_SftwrId',
            'filing_security_information_federal_original_submission_id': 'FlngScrtyInfrmtn_FdrlOrgnlSbmssnId',
            'buisness_officer_signature_date': 'BsnssOffcr_SgntrDt',
            'filer_foreign_address_country_code': 'FrgnAddrss_CntryCd',
            'discuss_with_paid_preparer_ind': 'BsnssOffcr_DscssWthPdPrprrInd'
        }

    def parse(self, schedule: dict):
        parsedResult = {}
        scheduleParts = schedule["schedule_parts"]["returnheader990x_part_i"]
        for result_key,irs_990_key in self.returnHeaderObjectMap.items():
            try:
                parsedResult[result_key] = scheduleParts[irs_990_key]
            except:
                parsedResult[result_key] = None
        return parsedResult
