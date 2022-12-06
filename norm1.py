import pandas as pd

def Data_Input():
    data = pd.read_csv(r"E:\lab-practice\Normalization\data.csv")
    colum_name = data.columns[0]
    data = list(data[colum_name])
    return data
def min_max_normalization():
    global data
    new_min = int(input('Please Enter new_min  '))
    new_max = int(input('\nPlease Enter new_max  '))
    
    min_in_data = min(data)
    curr_diff = max(data) - min_in_data
    new_diff = new_max-new_min

    for i in range(0,len(data)):
        num = new_min + ( (data[i]-min_in_data) / curr_diff ) * new_diff
        data[i]= round(num,2)

    return data


def variance():
    if len(data)==0:
        return None
    n = len(data)
    mean = sum(data)/n
    total=0
    
    for i in range(0,n):
        total+=(data[i]-mean)**2
        
    data_variance = (total / (n-1))
    return data_variance

def standard_deviation():
    var = variance()
    return var**0.5



def z_score_normalization():
    n = len(data)
    mean = sum(data)/n
    std = standard_deviation()
    
    for i in range(0,n):
        data[i]= (data[i]-mean)/std
        data[i]= round(data[i],2)

    return data

# filename = input("Enter File Name   ") 
# filename = "Normalization\data.csv"
data = Data_Input()

dicti = { 
    "Z score Normalization " : z_score_normalization() , 
    "Min Max Normalization" :  min_max_normalization() 
        }
print(dicti)