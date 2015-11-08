#my practice
# -*- coding: utf-8 -*-
#冒泡排序法
def bubble(*args):
    list=[p for p in args]
    for i in range(1,len(list)):
        for j in range(0,len(list)-i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

pp=[1,65,7,34,96,443]
print bubble(*pp)