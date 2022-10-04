import json
import numpy as np
import math


with open('H:\\summary0.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
for i in json_data["results"]["all"]:
    list1.append(i['1']['Dice'])
    list2.append(i['1']['Jaccard'])
    if math.isnan(i['1']['Precision']):
        list3.append(0)
    else:
        list3.append(i['1']['Precision'])
    list4.append(i['1']['Recall'])

    if math.isnan(i['1']['Precision']):
        list5.append(0)
    else:
        list5.append(2*i['1']['Precision']*i['1']['Recall']/(i['1']['Precision']+i['1']['Recall']))


mean1 = np.mean(list1)
max1 = np.max(list1)
min1 = np.min(list1)
median1=np.median(list1)
std1 = np.std(list1)

mean2 = np.mean(list2)
max2 = np.max(list2)
min2 = np.min(list2)
median2=np.median(list2)
std2 = np.std(list2)

mean3 = np.mean(list3)
max3 = np.max(list3)
min3 = np.min(list3)
median3=np.median(list3)
std3 = np.std(list3)

mean4 = np.mean(list4)
max4 = np.max(list4)
min4 = np.min(list4)
median4=np.median(list4)
std4 = np.std(list4)

mean5 = np.mean(list5)
max5 = np.max(list5)
min5 = np.min(list5)
median5=np.median(list5)
std5 = np.std(list5)


n=len(list1)
print(mean1, max1, min1,median1)
print(mean2, max2, min2, median2)
print(mean3, max3, min3,median3)
print(mean4, max4, min4,median4)
print(mean5, max5, min5,median5)

def CI(mean,std,n):
    return mean-1.96*std/pow(n,0.5),mean+1.96*std/pow(n,0.5)

print(CI(mean1,std1,n),CI(mean2,std2,n),CI(mean3,std3,n),CI(mean4,std4,n),CI(mean5,std5,n))