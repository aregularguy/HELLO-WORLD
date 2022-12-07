import math
from itertools import combinations

def read_data_in_dict(filename):
    f = open(filename)         
    lines = f.readlines()
    transactions = []
    items = lines[0].split(',')
    print(lines[2])
    for line in lines[1:]:
        transactions.append(list(map(int,line.split(','))))
    data ={
        'items':items,
        'transactions':transactions
    }
    # print('Transaction list is ')
    # print(transactions)
    # print('lines is ')
    # print(items)
    return data
data = read_data_in_dict('E:\lab-practice\data.csv')

def get_freq(s,items,transactions):
    freq_cnt=0
    for t in transactions:
        temp=1
        for item in s:
            temp*=t[items.index(item)]
        if temp==1:
            freq_cnt += 1  
    return freq_cnt


def frequent_itemsets(data,level,min_support):
        items = data['items']
        transactions = data['transactions']
        min_freq = math.ceil(min_support*len(transactions))
        sets = list(combinations(items,level))
        # print("combinations")
        # print(sets)
        # print("end of combinations")
        frequent_sets = []
        for s in sets:
            freq=get_freq(s,items,transactions)
            if freq>=min_freq:
                frequent_sets.append(s)
                # a,b,c,d,e,f,g
        return frequent_sets



print(frequent_itemsets(data,2,0.5))    
