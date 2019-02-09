import math
import time
import pandas as pd
from math import pow

df = pd.read_csv('pressures.csv')
w=diff=number=i=value=0
col = df['Portland']
length = df.shape[0]
size=0
arr = []

thr = float(input("Enter Thresold Value: "))
rmse=0



while number < length:
    value = round(col.iloc[number],2)
    number += 1
    w += 1
    arr.append(value)

    if w > 1:
        diff = max(arr) - min(arr)
        diff=round(diff,2)

        if number == length:
            rep=(max(arr)+min(arr))/2
            print("Compressed!",*arr,"Represanatative Value:",round(rep,2))
            rm = 0
            while rm < len(arr):
                rmse += pow((rep - arr[rm]), 2)
                rmse = round(rmse, 2)
                rm += 1
            i+=1


        if diff > 2 * thr:
            p=arr.pop()
            print(*arr,end=" ")
            rep=(max(arr)+min(arr))/2

            if(w < 3):
                print("Compression Succesfull!!Data Representative Value:",*arr)
                i+=1
                print("Time Stamp:",time.time() * 1000)
            else:
                print("Compression Succesfull!!Data Representative Value: ",round(rep,2))
                i+=1
                print("Time Stamp:",time.time() * 1000)
                rm = 0
                while rm < len(arr):
                    rmse += pow((rep - arr[rm]), 2)
                    rmse = round(rmse, 2)
                    rm += 1

            arr.clear()
            arr.append(value)
            print("\n")



print("Total Iteration:", i)
rmse_calc = math.sqrt(rmse / length)
print("Rmse:", round(rmse_calc,2))


thr = int(input("Enter Thresold Value: "))

