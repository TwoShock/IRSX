
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from IRSParsers.ParserFactory import ParserFactory
from IRSParsers.IRS990PFParser import IRS990PFParser
from IRSParsers.NullParserStrategy import NullParserStrategy
from IRSParsers.ReturnHeader990xParser import ReturnHeader990xParser
from IRSParsers.Json990Parser import Json990Parser
from IRSParsers.IRSScheduleIParser import IRSScheduleIParser

def test_return_header_990x_parser():
    returnHeaderSchedule = {
        "schedule_name": "ReturnHeader990x",
        "groups": {},
        "schedule_parts": {
            "returnheader990x_part_i": {
                "object_id": 201542399349300724,
                "ein": "270964918",
                "RtrnHdr_RtrnTs": "2015-08-27T14:10:50-05:00",
                "RtrnHdr_TxPrdEndDt": "2014-12-31",
                "PrprrFrm_PrprrFrmEIN": "420714325",
                "PrprrFrmNm_BsnssNmLn1Txt": "MCGLADREY LLP",
                "PrprrUSAddrss_AddrssLn1Txt": "1252 BELL VALLEY ROAD SUITE 300",
                "PrprrUSAddrss_CtyNm": "ROCKFORD",
                "PrprrUSAddrss_SttAbbrvtnCd": "IL",
                "PrprrUSAddrss_ZIPCd": "61108",
                "RtrnHdr_RtrnCd": "990",
                "RtrnHdr_TxPrdBgnDt": "2014-01-01",
                "Flr_EIN": "270964918",
                "BsnssNm_BsnssNmLn1Txt": "ROCKFORD AREA STRATEGIC INITIATIVE",
                "Flr_BsnssNmCntrlTxt": "ROCK",
                "Flr_PhnNm": "8159878118",
                "USAddrss_AddrssLn1Txt": "100 PARK AVENUE SUITE 100",
                "USAddrss_CtyNm": "ROCKFORD",
                "USAddrss_SttAbbrvtnCd": "IL",
                "USAddrss_ZIPCd": "61101",
                "BsnssOffcr_PrsnNm": "JOEL SJOSTROM",
                "BsnssOffcr_PrsnTtlTxt": "CHAIRMAN OF THE BOARD",
                "BsnssOffcr_PhnNm": "8159878118",
                "BsnssOffcr_SgntrDt": "2015-06-11",
                "BsnssOffcr_DscssWthPdPrprrInd": "1",
                "PrprrPrsn_PrprrPrsnNm": "MICHAEL J SPODEN",
                "PrprrPrsn_PTIN": "P00007977",
                "PrprrPrsn_PhnNm": "8152317300",
                "RtrnHdr_TxYr": "2014"
            }
        },
        "csv_line_array": []
    }
    expectedParsedSchedule = {'ein': '270964918', 'object_id': 201542399349300724, 'tax_year': '2014', 'preparer_email': None, 'filer_buisness_name_control_txt': 'ROCK', 'filing_security_information_federal_original_submission_id_date': None, 'filing_security_information_ipd_date': None, 'disaster_relief_txt': None, 'originator_group_practitioner_pin_group_efin': None, 'preparer_phone_number': '8152317300', 'preparer_firm_group_usaddress_line_2': None, 'filer_state_abbreviation_code': 'IL', 'preparer_firm_group_usaddress_line_1': '1252 BELL VALLEY ROAD SUITE 300', 'buisness_name_line_2': None, 'preparer_firm_group_foreign_address_country_code': None, 'preparer_self_employed_ind': None, 'originator_group_practitioner_pin': None, 'preparer_ssn': None, 'originator_group_originator_type_code': None, 'buisness_name_line_1': 'ROCKFORD AREA STRATEGIC INITIATIVE', 'filer_city_name': 'ROCKFORD', 'buisness_officer_group_phone_number': '8159878118', 'filer_foreign_address_province_or_state_name': None, 'business_officer_group_tax_payer_pin': None, 'tax_period_start_date': '2014-01-01', 'filer_ein': '270964918', 'filer_us_address_address_line_1': '100 PARK AVENUE SUITE 100', 'return_type_code': '990', 'filer_us_address_line_2': None, 'filer_foreing_address_city_name': None, 'filing_security_information_at_submission_creation_device_id': None, 'preparer_foreign_address_foreign_postal_code': None, 'filing_security_information_filing_licesnse_type_code': None, 'tax_period_end_date': '2014-12-31', 'preparer_foreign_address_line_2': None,
                              'preparer_firm_ein': '420714325', 'preparer_buisness_name_line_2': None, 'return_creation_date': '2015-08-27T14:10:50-05:00', 'buisness_officer_group_person_title': 'CHAIRMAN OF THE BOARD', 'isp_number': None, 'preparer_ptin': 'P00007977', 'preparer_buisness_name_line_1': 'MCGLADREY LLP', 'preparer_us_address_city_name': 'ROCKFORD', 'filling_security_information_at_submission_filing_device_id': None, 'preparer_foreign_address_line_1': None, 'preparer_us_address_state_abbreviation_code': 'IL', 'preparer_preparation_date': None, 'preparer_foreign_address_province_or_state_name': None, 'filer_foreign_address_line_1': None, 'filer_foreign_postal_code': None, 'preparer_person_name': 'MICHAEL J SPODEN', 'originator_group_efin': None, 'filer_in_care_of_name': None, 'software_version_number': None, 'filing_security_information_ipv4_address': None, 'filing_security_information_iptimezone_code': None, 'signature_option_code': None, 'preparer_us_address_zip_code': '61108', 'filing_security_information_iptm': None, 'filer_us_address_zip_code': '61101', 'buisness_officer_email_address': None, 'buisness_officer_person_name': 'JOEL SJOSTROM', 'pin_entered_by_code': None, 'filing_security_information_ipv6_address': None, 'filer_foreign_address_line_2': None, 'filer_phone_number': '8159878118', 'software_id': None, 'filing_security_information_federal_original_submission_id': None, 'buisness_officer_signature_date': '2015-06-11', 'filer_foreign_address_country_code': None, 'discuss_with_paid_preparer_ind': '1'}
    parsedReturnHeader = ReturnHeader990xParser().parse(returnHeaderSchedule)
    assert expectedParsedSchedule == parsedReturnHeader


def test_irs_schedule_i_parser():
    scheduleIExample = {
        "schedule_name": "IRS990ScheduleI",
        "groups": {
            "SkdIRcpntTbl": [
                {
                    "object_id": 202012259349301611,
                    "ein": "746076224",
                    "RcpntBsnssNm_BsnssNmLn1Txt": "CHILDREN'S ASSOCIATION FOR MAXIMUM POTENTIAL",
                    "USAddrss_AddrssLn1Txt": "515 SKYLINE DR",
                    "USAddrss_CtyNm": "CENTER POINT",
                    "USAddrss_SttAbbrvtnCd": "TX",
                    "USAddrss_ZIPCd": "78010",
                    "RcpntTbl_RcpntEIN": "742095766",
                    "RcpntTbl_IRCSctnDsc": "501(C)(3)",
                    "RcpntTbl_CshGrntAmt": "7500",
                    "RcpntTbl_PrpsOfGrntTxt": "PROGRAM FOR CHILDREN WITH SPECIAL NEEDS TO ATTEND CAMP."
                },
                {
                    "object_id": 202012259349301611,
                    "ein": "746076224",
                    "RcpntBsnssNm_BsnssNmLn1Txt": "WHEELCHAIRS 4 KIDS",
                    "USAddrss_AddrssLn1Txt": "1976 S PINELLAS AVE",
                    "USAddrss_CtyNm": "TARPON SPRINGS",
                    "USAddrss_SttAbbrvtnCd": "FL",
                    "USAddrss_ZIPCd": "34689",
                    "RcpntTbl_RcpntEIN": "451308941",
                    "RcpntTbl_IRCSctnDsc": "501(C)(3)",
                    "RcpntTbl_CshGrntAmt": "7500",
                    "RcpntTbl_PrpsOfGrntTxt": "ASSISTANCE PURCHASING ADAPTIVE TRICYCLES FOR CHILDREN WITH DISABILITIES ."
                },
                {
                    "object_id": 202012259349301611,
                    "ein": "746076224",
                    "RcpntBsnssNm_BsnssNmLn1Txt": "ANY BABY CAN OF SAN ANTONIO INC",
                    "USAddrss_AddrssLn1Txt": "217 HOWARD",
                    "USAddrss_CtyNm": "SAN ANTONIO",
                    "USAddrss_SttAbbrvtnCd": "TX",
                    "USAddrss_ZIPCd": "78212",
                    "RcpntTbl_RcpntEIN": "742684333",
                    "RcpntTbl_IRCSctnDsc": "501(C)(3)",
                    "RcpntTbl_CshGrntAmt": "5000",
                    "RcpntTbl_PrpsOfGrntTxt": "ASSIST FAMILIES WITH CHILDREN DIAGNOSED WITH A CHRONIC ILLNESS OR DISABILITY"
                },
            ],
            "SkdISpplmntlInfrmtnDtl": [
                {
                    "object_id": 202012259349301611,
                    "ein": "746076224",
                    "FrmAndLnRfrncDsc": "PART I, LINE 2:",
                    "ExplntnTxt": "CHARITIES REQUESTING GRANTS MUST SPECIFY THE PROJECT OR PROGRAM THE FUNDS WILL BE USED PRIOR TO FUNDING. THE ORGANIZATION FOLLOWS UP WITH GRANT RECIPIENTS THROUGHOUT THE YEAR TO BE UPDATED ON THE PROGRAMS AND PROJECTS."
                }
            ]
        },
        "schedule_parts": {
            "skedi_part_i": {
                "object_id": 202012259349301611,
                "ein": "746076224",
                "GrntRcrdsMntndInd": "1"
            }
        },
        "csv_line_array": []
    }
    parsedSchedule = IRSScheduleIParser().parse(scheduleIExample)
    expectedSchedule = {'grants_to_organizations_in_the_us': [{'recepient_name': "CHILDREN'S ASSOCIATION FOR MAXIMUM POTENTIAL", 'recepient_address': '515 SKYLINE DR', 'city_num': 'CENTER POINT', 'street_abreviation_code': 'TX', 'zip_code': '78010', 'recepient_ein': '742095766', 'irc_section_description': '501(C)(3)', 'recepient_cash_grant_amount': '7500', 'purpose_of_grant_txt': 'PROGRAM FOR CHILDREN WITH SPECIAL NEEDS TO ATTEND CAMP.'}, {'recepient_name': 'WHEELCHAIRS 4 KIDS', 'recepient_address': '1976 S PINELLAS AVE', 'city_num': 'TARPON SPRINGS', 'street_abreviation_code': 'FL', 'zip_code': '34689', 'recepient_ein': '451308941', 'irc_section_description': '501(C)(3)', 'recepient_cash_grant_amount': '7500', 'purpose_of_grant_txt': 'ASSISTANCE PURCHASING ADAPTIVE TRICYCLES FOR CHILDREN WITH DISABILITIES .'}, {
        'recepient_name': 'ANY BABY CAN OF SAN ANTONIO INC', 'recepient_address': '217 HOWARD', 'city_num': 'SAN ANTONIO', 'street_abreviation_code': 'TX', 'zip_code': '78212', 'recepient_ein': '742684333', 'irc_section_description': '501(C)(3)', 'recepient_cash_grant_amount': '5000', 'purpose_of_grant_txt': 'ASSIST FAMILIES WITH CHILDREN DIAGNOSED WITH A CHRONIC ILLNESS OR DISABILITY'}]}
    assert expectedSchedule == parsedSchedule


def test_null_parser():
    dummySchedule = {
        "schedule_name": "dummy"
    }
    parsedSchedule = NullParserStrategy().parse(dummySchedule)
    assert parsedSchedule == {}


def test_parser_factory():
    filings = [

        {
            'schedule_name': 'ReturnHeader990x'

        }, {
            'schedule_name': 'IRS990PF'

        }, {
            'schedule_name': 'IRS990ScheduleI'

        }, {
            'schedule_name': 'NullParser'

        }
    ]

    strategyTypes = [ReturnHeader990xParser, IRS990PFParser,
                     IRSScheduleIParser, NullParserStrategy]
    for i, filing in enumerate(filings):
        parserStrategy = ParserFactory().createParserStrategy(filing)
        assert type(parserStrategy) is strategyTypes[i]


