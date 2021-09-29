#!/usr/bin/python3

import sys
import parsing
import search

def helper():
    print("USAGE")
    print("     ./autoCompletion dictionary")
    print("DESCRIPTION")
    print("     dictionary    file containing one address per line, as knowledge base")

def core(correct_address):
    print("{m} {l} {p} {s} {d}")

def main():
    size = len(sys.argv)
    if (size == 2 and sys.argv[1] == "-h"):
        helper()
    elif (size != 2):
        sys.stderr.write("Invalid argument")
        exit(84)
    else:
        parse = parsing.Parsing(sys.argv[1])
        parse.openfile()
        parse.prerequisite()
        global_list = parse.parse()
        stdin_values = []
        for line in sys.stdin:
            for char in line:
                if (char.rstrip() != ""):
                    stdin_values.append(char.rstrip())
        find = search.Search(stdin_values)
        city = find.search_city(global_list, 0)
        street = find.search_city(city, 2)
    return (0)

if __name__ == '__main__':
    main()