from xml.etree.ElementInclude import DEFAULT_MAX_INCLUSION_DEPTH
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
class GrantGraphVisualizer:
    def __init__(self,path:str) -> None:
        self.__graph = nx.DiGraph() 
        self.__path = path
        self.__df = pd.read_csv(path)

    def displayGraphForYear(self,year:int):
        self.populateGraphForYear(year)
        subax1 = plt.subplot(121)
        pos = nx.circular_layout(self.__graph)
        nx.draw_networkx(self.__graph, with_labels=True, pos=pos,font_weight='bold')
        plt.show()


    def populateGraphForYear(self,year):
        df = self.__df.loc[self.__df['tax_year']==year]
        for index,row in df.iterrows():
            self.__graph.add_node(row['doner_name'])
            self.__graph.add_node(row['recepient_name'])
            self.__graph.add_weighted_edges_from([(row['doner_name'],row['recepient_name'],row['recepient_cash_grant_amount'])])
        
    def getGraph(self):
        return self.__graph