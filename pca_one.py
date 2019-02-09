import pandas as pd
import math


while True:
    thr = float(input("Enter Thresold Value: "))
    w = int(input("Enter Window Size: "))
    df = pd.read_csv('pressures.csv')
    arr = []
    rmse=0
    diff=number=i=value=index=err_point=0
    col=df['Portland']
    length = df.shape[0]
    d_point = 0


    while number < length :
        value = round(col.iloc[index],2)
        number += 1
        index += 1
        arr.append(value)


        if index % w == 0:
                max_global =float(max(arr))
                min_global =float(min(arr))
                diff = max_global - min_global
                diff = round(diff, 2)

                if diff <= 2 * thr:
                    print(*arr,end="")
                    rep = round((max_global+min_global)/2,2)
                    print(" Compressed ! String Representative Value: ", rep)
                    rm = 0
                    while rm < len(arr):
                        rmse += pow((rep - arr[rm]), 2)
                        rmse = round(rmse, 2)
                        rm += 1
                    print('\n')
                    d_point+=1

                    arr.clear()
                else:
                    print("Compression Failed!", "Main String :", end=" ")
                    d_point += w
                    print(*arr, end=" ")
                    print('\n')
                    arr.clear()


    d_point += float(length%w)
    print("Total Compressed Data Point:", d_point)
    rmse_calc = math.sqrt(rmse / length)
    print("Rmse", round(rmse_calc,2))
    print("\n")

