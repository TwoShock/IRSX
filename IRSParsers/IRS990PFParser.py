from IRSParsers.ParserStrategy import ParserStrategy


class IRS990PFParser(ParserStrategy):
    def __init__(self) -> None:
        super().__init__()
        self.IRS990PFObjectMap = {
            "key_employees": "PFOffcrDrTrstKyEmpl"
        }
        self.IRS990PFEmployeeInformationObjectMap = {

        }
    def __parseEmployee(employee):
        currentEmployeeInformation = {}
        
    def __parseKeyEmployes(self, schedule: dict):
        keyEmployees = {}
        employeeList = schedule[self.IRS990PFObjectMap["key_employees"]]
        parsedEmployeeList = []
        for employee in employeeList:
            currentEmployeeInformation = {}

    def parse(self, schedule: dict):
        parsedResults = {}
        return {}

