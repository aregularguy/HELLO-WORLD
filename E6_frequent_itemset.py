import pandas
import math
from  itertools import combinations,permutations

def read_data_in_dict(filename):
   f = open(filename)
   lines = f.readlines()
   transactions = []
   items = lines[0].split(',')
   for line in lines[1:]:
       transactions.append(list(map(int,line.split(','))))
   data = {
       'items' :items,
       'transactions' : transactions
   }  
#    print('Transaction list is ')
#    print(transactions)
#    print('lines is ')
#    print(items)  
   return data
data =read_data_in_dict('data.csv')   

def get_freq(s,items,transactions):
    freq_cnt = 0
    for t in transactions:
        tmp = 1
        for item in s:
            tmp *= t[items.index(item)]
            if tmp ==1:
                freq_cnt +=1
    return freq_cnt         

def frequent_itemset(data,level,min_support):
    items = data["items"]
    transactions = data["transactions"]
    min_freq = math.ceil(min_support*len(transactions))
    sets = list(combinations(items,level))
    frequents_sets = []
    for s in sets:
        freq = get_freq(s,items,transactions)
        if freq >= min_freq:
            frequents_sets.append(s)
    return frequents_sets        
            


print(frequent_itemset(data,2,0.5))
