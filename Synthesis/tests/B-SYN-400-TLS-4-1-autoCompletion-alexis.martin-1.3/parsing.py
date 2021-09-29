#!/usr/bin/python3

import sys
import re
import os

class Parsing:
    def __init__(self, file):
        self.file = file
        self.bnumber = False
        self.prerequisite_addresses = []
        self.errors_list = []
        self.global_list = []

    def openfile(self):
        try:
            if os.stat(self.file).st_size == 0:
                exit(84)
            file1 = open(self.file, 'r')
            Lines = file1.readlines()
            self.Lines = Lines
        except:
            self.Lines = ""
            sys.stderr.write("Error opened file\n")
            exit(84)
    
    def parse(self):
        for self.line in self.prerequisite_addresses:
            tmp_array = []
            
            # Stock Street
            list = "allée|avenue|boulevard|chemin|impasse|place|quai|rue|square"
            search_pos_street_type = re.search(list, self.line.rstrip())
            street_type = re.findall(list, self.line.rstrip())
            street = self.line[search_pos_street_type.start():]
            if ',' in street:
                search_pos_comma = re.search(',', street)
                street = street[0:search_pos_comma.start()]

            # Stock Numbers
            substr = self.line[0:search_pos_street_type.start() - 1]
            n = substr.split(' ')
            if (n[-1].isnumeric()):
                number = n[-1]
            
            # Stock City
            if ',' in self.line:
                search_pos_comma2 = re.search(',', self.line)
                search_pos_number = re.search(number, self.line)
                if (search_pos_comma2.start() < search_pos_number.start()):
                    city = self.line[0:search_pos_comma2.start()]
                else:
                    city = self.line[search_pos_comma2.end():]

            # Add on list
            tmp_array.append(city)
            tmp_array.append(number)
            tmp_array.append(street)
            self.global_list.append(tmp_array)
        return (self.global_list)
        
    def prerequisite(self):
        for self.line in self.Lines:
            self.bnumber = False

            # Stock all words in array
            remove_spaces = " ".join(self.line.split())
            array_all = remove_spaces.split(" ")

            # Check if street Type exist
            list = "allée|avenue|boulevard|chemin|impasse|place|quai|rue|square"
            x = re.search(list, remove_spaces.lower().rstrip())
            if (not x):
                self.errors_list.append(self.line.rstrip() + " (Missing StreetType)")
                continue
            
            # Check if number exists
            for i in array_all:
                if (i.isnumeric()):
                    self.bnumber = True
                    continue

            if (not self.bnumber):
                self.errors_list.append(self.line.rstrip() + " (Missing Number)")
            else:
                self.prerequisite_addresses.append(self.line)

        for error in self.errors_list:
            sys.stderr.write(error.rstrip() + "\n")