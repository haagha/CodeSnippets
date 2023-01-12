# Description: Find the most common substring in a list of lists

# Author: Haider Agha
# Date: 12/12/2022
# Version: 1.0
# License: MIT

# Usage: python CmdSeqCommonSubstring.py
# Output: top 30 most common occuring sequences of 5 to 5 commands
# Example: ('"storage blob upload","vm show","image create"', 2)

# Note: This script is not optimized for performance. It is a proof of concept.

import csv
import time
import re
import sys


# read csv file and convert to list of lists
#data format = ['["account list","group show","storage account create"]']
# remove brackets and split into list
# cmdlist format = [['"account list"','"group show"','"storage account create"'], ['"account list2"','"group show2"','"storage account create2"']]

def read_csv_file(filename):
    list_of_list = []
    cmdlist = []
    with open(filename) as csvfile:
        list_of_list = (csv.reader(csvfile))

        # remove brackets and split into list
        for lines in list_of_list:
            newline = re.sub('[\[\]]', '', lines[0])
            newlist = newline.split(",")
            cmdlist.append(newlist)
        
        # print number of sessions
        print("total sessions = " + str(len(cmdlist)))

        return cmdlist
        

# concatenate list data
def concatenate_list_data(list):
    result= ' '
    for element in list:
        result += str(element)
    return result



# find most common substring
# iterate over each list in list of lists
# iterate over each element in list
# iterate over each element after i in list
# if read command then keep iterating
# if write command then add to write_seq
def find_most_common_substring(list_of_list, min_key_len, max_key_len):

    substrings = dict()

    for x in range(len(list_of_list)):       
        for i in range(len(list_of_list[x])-1):
            for j in range(i, len(list_of_list[x])-1):
                
                write_seq = []                
                temp_min_key = min_key_len

                for k in range(j, j+temp_min_key):
                    if k+temp_min_key > len(list_of_list[x]):
                        break
                    command = list_of_list[x][k]
                    if any(read_cmds in command for read_cmds in ('show', 'list', 'get')):
                        temp_min_key = temp_min_key+1
                        #print(command + " read command")
                    else:
                        write_seq.append(command)
                        #print(command + " write command")
                
                
                if j+temp_min_key > len(list_of_list[x]):
                    break
                if write_seq == []:
                    continue
                
                if len(write_seq) < min_key_len:
                    continue
                seq = ''.join(map(concatenate_list_data, write_seq))                
                seq = re.sub('[\[\]]', '', seq)
                #print(seq)
                


                if seq not in substrings:
                    substrings[seq] = 0
                substrings[seq] += 1
    
    print("number of combinations = " + str(len(substrings.keys())))

    #for key in list(substrings):
    #    if not key.__contains__("vm"):
    #        substrings.pop(key)

    substring_counts = {}

    print("top 30 most common occuring sequences of " + str(min_key_len) + " to " + str(max_key_len) + " commands")
    for kv in sorted(substrings.items(), key=lambda kv: kv[1], reverse=True)[:30]:
        print(kv[0], kv[1])

    return max(substrings, key=substrings.get)


lister=[[''],['"storage blob upload","vm show","image create"'],
["storage blob upload2","vm show2","image create2","storage blob 21","vm show21","image create21","storage blob upload21","vm show21","image create21","storage blob upload22","vm show22","image create22"],
["storage blob upload3","vm show3","image create3"]]

# read command line arguments
filename = sys.argv[1]
min_key_len = int(sys.argv[2])
max_key_len = int(sys.argv[3])

cmdlist = read_csv_file(filename)

# call function to find most common substring
find_most_common_substring(cmdlist, min_key_len, max_key_len)
