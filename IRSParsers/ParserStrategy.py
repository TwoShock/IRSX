from abc import ABC, abstractmethod
class ParserStrategy:
    @abstractmethod
    def parse(self,schedule:dict):
        pass
        