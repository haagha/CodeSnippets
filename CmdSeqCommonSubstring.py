# function for most common substring 
import csv
import time
import re

list_of_list = []
cmdlist = []
counter = 0
with open('30d30t.csv') as csvfile:

    #data format = ['["account list","group show","storage account create"]']
    list_of_list = (csv.reader(csvfile))

    # remove brackets and split into list
    # cmdlist format = [['"account list"','"group show"','"storage account create"'], ['"account list2"','"group show2"','"storage account create2"']]
    for lines in list_of_list:
        newline = re.sub('[\[\]]', '', lines[0])
        newlist = newline.split(",")
        cmdlist.append(newlist)
        
print("total sessions = " + str(len(cmdlist)))

def concatenate_list_data(list):
    result= ' '
    for element in list:
        result += str(element)
    return result


# Create a set of all substrings in from all lists
#create a copy of seq

def find_most_common_substring(list_of_list, min_key_len, max_key_len):
    # First, we create a set of all substrings in from all lists
    substrings = dict()
    for x in range(len(list_of_list)):        
        for i in range(len(list_of_list[x])-1):
            for j in range(i, len(list_of_list[x])-1):
                
                write_seq = []
                temp_min_key = min_key_len
                # iterate over each element in seq and if read then keep iterating
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
                
                #print(write_seq)
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
    
    #print(substrings)
    print("number of combinations = " + str(len(substrings.keys())))
    #print("max(substrings.values()))
    #sleep(600)

    for key in list(substrings):
        if not key.__contains__("vm"):
            substrings.pop(key)

    #for kv in substrings.items():
        #print(kv[0], kv[1])

    # Then, we count the number of times each substring appears in both lists
    substring_counts = {}
    #print(substrings)

    # Finally, we return the substring with the highest count
    #print(max(substrings, key=substrings.get))

    # sort dictionary and print top 10
    print("top 30 most common occuring sequences of " + str(min_key_len) + " to " + str(max_key_len) + " commands")
    for kv in sorted(substrings.items(), key=lambda kv: kv[1], reverse=True)[:30]:
        print(kv[0], kv[1])

    return max(substrings, key=substrings.get)


lister=[[''],['"storage blob upload","vm show","image create"'],
["storage blob upload2","vm show2","image create2","storage blob 21","vm show21","image create21","storage blob upload21","vm show21","image create21","storage blob upload22","vm show22","image create22"],
["storage blob upload3","vm show3","image create3"]]

find_most_common_substring(cmdlist, 5, 5)
