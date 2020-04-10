from config import config
from math import sqrt

class Reader:
    def __init__(self, fileName):
        self.fileName = fileName

    def readTxt(self):
        f = open(self.fileName, "r")
        lines = f.readlines()

        config["noNodes"] = int(lines[0])
        print(lines[0])
        config["network"] = []
        for i in range(1, config["noNodes"]+1):
            config["network"].append([int(x) for x in lines[i].split(",")])

    def readTextHard(self):
        f = open(self.fileName, "r")
        lines = f.readlines()

        values = []
        ok = 0
        for line in lines:
            listLine = line.split()

            if listLine[0] == "DIMENSION:":
                config["noNodes"] = int(listLine[1])
            elif listLine[0] == "DIMENSION":
                config["noNodes"] = int(listLine[2])
           

            if listLine[0] == "1" or ok == 1:
                ok = 1
                values.append([float(listLine[1]), float(listLine[2])])


        config["network"] = []
        for i in values:
            linie = []
            for j in values:
                x = abs(i[0] - j[0])
                y = abs(i[1] - j[1])
                rez = sqrt((x * x) + (y * y))
                linie.append(rez)

            config["network"].append(linie)

        
