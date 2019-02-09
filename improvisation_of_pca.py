import pandas as pd
import math
import xlrd
from math import pow
rmse_one=0

def split_window(*temp):

    dp =number =w=flag= 0
    temparr= []
    win=len(temp)
    global rmse_one

    while number < win :
        value = temp[number]
        w += 1
        number += 1
        temparr.append(value)

        if w > 1:
            diff = max(temparr) - min(temparr)
            diff = round(diff, 2)

            if diff <= 2 * thr:
                if number==5:
                     rep = round(((max(temparr) + min(temparr)) / 2),2)
                     print(*temparr, end=" ")
                     rm = 0
                     while rm < len(temparr):
                         rmse_one += pow((rep - temparr[rm]), 2)
                         rmse_one=round(rmse_one,2)
                         rm+=1
                     print("Compression Succesfull!!Data Representative Value: ", rep)
                     dp += 1
                     temparr.clear()
                continue

            else:
                temparr.pop()
                rep =round((max(temparr) + min(temparr)) / 2 ,2)

                if(len(temparr)==1):
                    print("Compression Succesfull!!Data Representative Value: ",*temparr)
                    temparr.clear()
                    temparr.append(value)
                    dp+=1
                    w=1
                    if(number==5):
                        print("Compression Succesfull!!Data Representative Value: ", *temparr)
                        dp+=1

                else:
                    print(*temparr, end=" ")
                    print("Compression Succesfull!!Data Representative Value: ", round(rep,2))
                    dp += 1
                    rm = 0
                    while rm < len(temparr):
                        rmse_one += pow((rep - temparr[rm]), 2)
                        rmse_one = round(rmse_one, 2)
                        rm += 1
                    temparr.clear()
                    temparr.append(value)
                    w=1
                    if(number==5):
                        print("Compression Succesfull!!Data Representative Value: ", *temparr)
                        dp+=1
    return dp

while True:
    thr = float(input("Enter Thresold Value: "))
    w = int(input("Enter Window Size: "))
    maximum_win = int(input("Enter Maximum Window to merge: "))
    df = pd.read_csv('sensorData.csv')
    arr = []
    current_arr = []
    global rmse
    diff=number=i=value=index=cr_point=err_point=rmse=0
    col=df['Sensor']
    #col = df[''].fillna(7.2)
    length = df.shape[0]
    d_point = 0
    size = w + 1

    while  number < length :
        value = round(col.values[number],2)
        number+=1
        index += 1
        arr.append(value)
        current_arr.append(value)

        if index % w == 0:
            max_global = max(arr)
            min_global = min(arr)
            diff_global = max_global - min_global
            diff_global = round(diff_global,2)


            if diff_global <= 2 * thr:
                if len(arr)== maximum_win * w:
                    print(*arr,end=" ")
                    rep = ((max_global + min_global) / 2)
                    print("Compressed ! String Representative Value: ", round (rep,2))
                    rm=0
                    while rm < len(arr):
                        rmse += round(rep - arr[rm],2)
                        rm += 1

                    d_point+=1
                    arr.clear()
                    current_arr.clear( )

                else:
                    cr_point = len(arr)
                    current_arr.clear()
                    continue

            else:
                max_cr = max(current_arr)
                min_cr = min(current_arr)
                diff_cr = max_cr - min_cr
                diff_cr = round(diff_cr, 2)

                if diff_cr <= 2 * thr:
                        print(arr[0:cr_point], end=" ")
                        print(arr[0:cr_point], end=" ")
                        max_temp = max(arr[0:cr_point])
                        min_temp = min(arr[0:cr_point])
                        rep = round(((max_temp + min_temp) / 2), 2)
                        print("Compressed ! String Representative Value: ",rep)
                        rm = 0
                        while rm < cr_point:
                            rmse += pow((rep - arr[rm]), 2)
                            rmse = round(rmse, 2)
                            rm += 1

                        d_point += 1
                        arr.clear()
                        arr = current_arr.copy()
                        current_arr.clear()
                        cr_point=len(arr)

                else:
                        if len(arr) < size:
                            d_point+=split_window(*current_arr)
                            arr.clear()
                            current_arr.clear()

                        else:
                            print(arr[0:cr_point], end=" ")
                            max_temp=max(arr[0:cr_point])
                            min_temp=min(arr[0:cr_point])
                            rep = (max_temp + min_temp)/2
                            print("Compressed ! String Representative Value: ", round(((max_temp + min_temp) / 2),2))
                            rm = 0
                            while rm < cr_point :
                                rmse += pow((rep - arr[rm]),2)
                                rmse= round(rmse,2)
                                rm += 1

                            d_point +=  1
                            d_point+=split_window(*current_arr)
                            arr.clear()
                            current_arr.clear()
    d_point += split_window(*arr)
    print("Total Data Point:",d_point)
    rmse_calc = (rmse + rmse_one)
    final =  rmse_calc/number
    final = math.sqrt(final)
    print("Rmse::",round(final,2))
    blank = input("")
    break















