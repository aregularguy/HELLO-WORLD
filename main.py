# 50 lines (32 sloc)  882 Bytes

import statistics as st
import pandas as pd
import csv

data = pd.read_csv("E:\lab-practice\corelation\input.csv")
A = data["A"].tolist()
B = data["B"].tolist()

n = len(A)

A_mean = sum(A) / n
B_mean = sum(B) / n

A_diff = []
B_diff = []

corelation = []
for i in range(len(A)):
    tmp = A[i] - A_mean
    A_diff.append(tmp)
    tmp2 = B[i] - B_mean
    B_diff.append(tmp2)
    corelation.append(A_diff[i] * B_diff[i])

total_corelation = sum(corelation)

stdDevA = st.stdev(A)
stdDevB = st.stdev(B)
ans = total_corelation / (stdDevA*stdDevB*(n-1))
print(ans)

headr = ["A","B","A-a","B-b","(A-a)*(B-b)"]

with open("output_corelation.csv",'w+',encoding='UTF8') as f:
    writer = csv.writer(f)

    writer.writerow(headr)
    for i in range(len(A)):
        data = [A[i],B[i],A_diff[i],B_diff[i],corelation[i]]
        writer.writerow(data)

