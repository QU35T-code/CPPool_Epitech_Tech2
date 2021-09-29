#!/usr/bin/python3

import sys
import re
import itertools

class Search:
    def __init__(self, stdin_values):
        self.stdin = stdin_values
        self.possible_cities = []
        self.possible_streets = []
        self.left_letters = []
        self.test = []
        self.payload = ""
        self.city = ""

    def prepare_payload(self, index):
        first_array = []
        possibilities = []
        self.payload = ""
        for p in range(20):
            for t in self.test:
                if (p < len(t[0])):
                    first_array.append(t[index][p])
                else:
                    #print("VILLE OK")
                    # self.city += self.payload
                    # self.city = self.city.upper() + ", "
                    #print("[LOOP] STDIN : " + str(self.left_letters))
                    #print("[LOOP] PAYLOAD : " + str(self.payload[:-1]))
                    last = self.payload.strip()[-1]
                    self.payload = self.payload[:-1]
                    self.left_letters.insert(0, last)
                    #print("LETTRES A TEST : " + str(self.left_letters))
                    return
            first_array = list(dict.fromkeys(first_array))
            if (len(first_array) > 1):
                for iterator in first_array:
                    # REGEX
                    tmp = self.payload
                    liste = "allée|avenue|boulevard|chemin|impasse|place|quai|rue|square"
                    x = re.search(liste, tmp.lower().rstrip())
                    if (x):
                        tmp = ""
                   # print("ADDED >CITY< : " + str(self.city) + " | >payload< : " + str(tmp) + " | >iterator< : " + str(iterator))
                    possibilities.append("{" + self.city + tmp.upper() + iterator.lower() + "}")                
                print(" ".join(str(x) for x in possibilities))
                first_array.clear()
                return
            else:
                self.payload = self.payload + first_array[0]
                first_array.clear()

    def search_city(self, global_list, index):
        try:
            self.test = global_list[:]
        except:
            sys.stderr.write("Unknown address\n")
            exit(84)
        self.possible_cities.clear()

        # Copy the list
        self.left_letters = self.stdin[:]

        # Read the list
        self.prepare_payload(index)
        #print("LETtERS : " + str(self.left_letters))
        for element in self.left_letters:
            #print("TRY : " + str(element))
            self.payload = self.payload + element
            #print("NEW PAYLOAD : " + str(self.payload))
            for glo in self.test:
                if (index == 1):
                    #print("On loop : " + str(glo[index]))
                    t = glo[index].partition(' ')[index].rstrip()
                    t = t.split()
                    #print("COMPARE 1 : " + self.payload.lower() + " | COMPARE 2 : " + t[0].lower())
                    x = re.search('^' + self.payload.lower(), t[0].lower().rstrip())
                    if (x):
                        self.possible_cities.append(glo)
                else:
                # Check if payload match with city
                    x = re.search('^' + self.payload.lower(), glo[index].lower().rstrip())
                    if (x):
                        self.possible_cities.append(glo)
            # Remove occurences in the list
            self.possible_cities.sort()
            self.possible_cities = list(k for k,_ in itertools.groupby(self.possible_cities))
            if (len(self.possible_cities) == 1):
                print("=> " + str(self.possible_cities[0][0]) + ", " + str(self.possible_cities[0][1]) + " " + str(self.possible_cities[0][2].rstrip()))
                exit(0)
            elif (len(self.possible_cities) == 0):
                sys.stderr.write("Unknown address\n")
                exit(84)
            else:
                # Remove occurences of city in the list and find the correct city
                city_locked = []
                for pos in self.possible_cities:
                    city_tmp = list(l for l,_ in itertools.groupby(pos[0]))
                    city_locked.append(pos[index].split())
                city_tmp = list(l for l,_ in itertools.groupby(city_locked))
                if (len(city_tmp) != 1):
                    #print("[DEBUG] POSSIBLE ADDRESSES : ")
                    print(self.possible_cities)
                    self.prepare_payload(index)
                    #print("[DEBUG] Plusieurs possibilité : " + self.payload + " | {" + str(city_tmp) + "}")
                elif (len(city_tmp) == 1):
                    self.city += city_tmp[0][0].upper() + ", "
                    #print("FOUND : " + str(city_tmp[0][0]))
                    try:
                        self.stdin.remove(element)
                    except:
                        pass
                    return (self.possible_cities)
            # Clear list
            self.possible_cities.clear()
            try:
                self.stdin.remove(element)
            except:
                exit(84)