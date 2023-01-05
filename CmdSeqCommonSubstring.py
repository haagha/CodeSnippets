# function for most common substring 
import csv
import time
import re

list_of_list = []
cmdlist = []
with open('timeout5seq20.csv') as csvfile:
    list_of_list = (csv.reader(csvfile))
    for lines in list_of_list:
        newline = re.sub('[\[\]]', '', lines[0])
        #print(newline)
        newlist = newline.split(",")
        cmdlist.append(newlist)

print("total sessions = " + str(len(cmdlist)))
#for i in range(len(cmdlist)):
#    print(cmdlist[i])

#sleep(600)

def concatenate_list_data(list):
    result= ' '
    for element in list:
        result += str(element)
    return result


def find_most_common_substring(list_of_list, min_key_len, max_key_len):
    # First, we create a set of all substrings in from all lists
    substrings = dict()
    for x in range(len(list_of_list)):        
        for i in range(len(list_of_list[x])-1):
            for j in range(i, i+max_key_len-min_key_len+1):
                if j+min_key_len > len(list_of_list[x]):
                    break
                seq = ''.join(map(concatenate_list_data, list_of_list[x][i:j+min_key_len]))
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
    for kv in sorted(substrings.items(), key=lambda kv: kv[1], reverse=True)[:20]:
        print(kv[0], kv[1])

    return max(substrings, key=substrings.get)


lister=[['"storage blob upload","vm show","image create"'],
["storage blob upload2","vm show2","image create2","storage blob upload","vm show","image create","storage blob upload2","vm show2","image create2","storage blob upload","vm show","image create"],
["storage blob upload3","vm show3","image create3"]]

find_most_common_substring(cmdlist, 4, 5)
