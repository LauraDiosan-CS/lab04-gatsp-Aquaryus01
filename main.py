import warnings

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from GA import GA
from config import config
from reader import Reader

def calculateFitness(repres, network):
    distance = 0
    for i in range(len(repres)-1):
        distance += network[repres[i]][repres[i+1]]

    distance += network[repres[-1]][repres[0]]
    return distance

def main():
    reader = Reader(config["fileName"])
    
    #Modifica daca schimb de la [easy,medium,hard] la [hardE, berlin52]
    
    # reader.readTxt()
    reader.readTextHard()


    GAparam = {
        'popSize' : config["popSize"],
        'noGen'   : config["noGen"]
    }
    
    problParam = {
        'function': calculateFitness, 
        'network': config["network"],
        'noNodes': config["noNodes"], 
    }

    ga = GA(GAparam, problParam)

    for _ in range(GAparam["noGen"]):
        ga.oneGenerationElitism()
        bestChromo = ga.bestChromosome()
        print(str(bestChromo))

main()