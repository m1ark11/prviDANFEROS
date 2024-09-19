#! /usr/bin/python3

import json, yaml
import pickle as pkl
import numpy as np
import matplotlib.pylab as plt


global zgodovina
zgodovina =[]



def main():
    global zgodovina
    print("kalkulator")
    operacija = input("Katero operacijo želiš izvesti (sestevanje, odstevanje, izhod)?")

    if operacija == "sestevanje":
        a = int(input("vnesi prvo število:"))
        b = int(input("vnesi drugo število:"))
        rezultat = {"a":a, "b":b, "r":a+b}
        zgodovina.append(rezultat)
        with open("../log.txt", "w") as f: #datoteko odpremo kot Write,Read, Append
            f.writelines(yaml.dump(zgodovina))
        print(f"rezultat: {a+b}")

    elif operacija == "odstevanje":
        a = int(input("vnesi prvo število:"))
        b = int(input("vnesi drugo število:"))
        rezultat = {"a":a, "b":b, "r":a-b}
        zgodovina.append(rezultat)
        with open("../log.txt", "w") as f: #datoteko odpremo kot Write,Read, Append
            f.writelines(yaml.dump(zgodovina))
        print(f"rezultat: {a-b}")
    
    elif operacija == "izhod":
        with open("../log.txt", "w") as f: #datoteko odpremo kot Write,Read, Append
            f.writelines(yaml.dump(zgodovina))

        pass

    else:
        print("neveljaven ukaz")





if __name__ == "__main__":
    main()