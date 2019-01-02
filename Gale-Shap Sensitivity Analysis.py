# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:04:23 2018

@author: karti
"""
import pandas as pd
import copy
from itertools import product


def swapiterate(cd): #This function moves the first element of an array to the end by iteration
    c=copy.deepcopy(cd)
    f=copy.deepcopy(c)
    a=[f]
    j=0
    while j<(len(c)-1):
        c[j], c[j+1] = c[j+1], c[j]
        a.append(copy.deepcopy(c))
        j=j+1
    return a

def sensitivity_analysis(dic1,dic2): #This gives all the combinations of the preferences with moving the first preference to the last one by one
    a=copy.deepcopy(dic1)
    b=copy.deepcopy(dic2)
    length_a=len(a.keys())
    length_b=len(b.keys())
    items_a=list(a.keys())
    items_b=list(b.keys())
    a_variants = [dict(zip(items_a, values)) 
                 for values in product(swapiterate(items_b), repeat=length_a)]
    b_variants = [dict(zip(items_b, values)) 
                 for values in product(swapiterate(items_a), repeat=length_b)]

    all_variants = [list(p) for p in product(a_variants, b_variants)]
    return all_variants

def insert_dummies(ab,ba):#insert dummies into the dictionary to square up the participants on both sides
    a=copy.deepcopy(ab)
    b=copy.deepcopy(ba)
    length_a=len(a.keys())
    length_b=len(b.keys())
    items_a=list(a.keys())
    items_b=list(b.keys())
    dummy_list=[]
    if length_a>length_b:
        dummy_number=length_a-length_b
        nummer=1
        while nummer<dummy_number+1:
            dummy_list.append("Dummy%d" %nummer)
            nummer=nummer+1
        for i in items_a:
            f=0
            while dummy_number>f:
                a.setdefault(i,[]).append(dummy_list[f])
                f=f+1
        n=0    
        while n<(dummy_number):
            for z in dummy_list:
                b[z]=items_a
            n=n+1
    if length_a<length_b:
        dummy_number=length_b-length_a
        nummer=1
        while nummer<dummy_number+1:
            dummy_list.append("Dummy%d" %nummer)
            nummer=nummer+1
        for i in items_b:
            f=0
            while dummy_number>f:
                b.setdefault(i,[]).append(dummy_list[f])
                f=f+1
        n=0    
        while n<(dummy_number):
            for z in dummy_list:
                a[z]=items_b
            n=n+1
    else:
        return

    return a,b



#This function returns the result of the algorithm. Parameter 'a' refers to the preferences of the gender
#that we want to find the optimized solution for, while the parameter 'b' refers to the preferences of the other gender.
def StableMatching(a, b):
    #this function returns a stable matching
    dict_a = a.keys()  #This list contains the names of the group for we are optimizing.
    names1 = list(dict_a)
    dict_b = b.keys() #This list contains the names of the other group.
    names2 = list(dict_b)
    i = 0
    engaged = []
    #This dictionary contains the names of the gender for which we attempt to find the optimized solution.
    times = {}
    t = 0
    position_existing = 0
    position_potential = 0
    counter = 0
    #Can have the values 'free' or 'not free'.
    a_p = {}
    while(counter < len(names1)):
        a_p.update({names1[counter]: 'free'})
        counter = counter + 1

    counter = 0
    #Can have the values 'free' or 'not free'.
    b_p = {}
    while(counter < len(names2)):
        b_p.update({names2[counter]: 'free'})
        counter = counter + 1

    counter = 0
    #Initialization of times dictionary.
    while(counter < len(names1)):
        times.update({names1[counter]: 0})
        counter = counter + 1

    #The value -1 has the meaning that when all men or women are paired, the loop stops;
    while((i != -1) and (a_p[names1[i]] == 'free') and (times[names1[i]] < len(names2))):
        #The man/woman who is next in the ranking of the proposals.
        w = a[names1[i]][times[names1[i]]]
        if(b_p[w] == 'free'):
            a_p[names1[i]] = 'not free'
            b_p[w] = 'not free'
            t = (names1[i], w)
            engaged.append(t)
            times[names1[i]] = times[names1[i]] + 1
        else:
            q = 0
            while(q < (len(engaged))):
                  if(w in engaged[q]):
                      t1 = engaged[q]
                      l = 0
                      while(l < len(names1)):
                          if(names1[i] == b[w][l]):
                              position_potential = l
                              l = len(names1)
                          l = l + 1
                      l = 0
                      while(l < len(names1)):
                          if(t1[0] == b[w][l]):
                              position_existing = l
                              l = len(names1)
                          l = l + 1
                      if(position_potential < position_existing):
                          t = (names1[i], w)
                          engaged.append(t)
                          del(engaged[q])
                          a_p[names1[i]] = 'not free'
                          a_p[t1[0]] = 'free'
                          q = len(engaged)
                  q = q + 1

            times[names1[i]] = times[names1[i]] + 1
        i = i + 1
        #If the variable i has passed from all the men/women then it starts from the beginning
        #in order to check the ones who remain single.
        if(i == len(names1)):
            i = 0
        if(a_p[names1[i]] == 'not free'):
            k = 0
            z = False
            while((k < len(names1)) and (z == False)):
                if(a_p[names1[k]] == 'free'):
                    i = k
                    z = True
                k = k + 1
            if((k == len(names1)) and (z == False)):
                i = -1
    engaged_dict = dict(engaged)
    return engaged_dict

def check(engaged,a,b):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = a[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = b[he]
        helikesbetter = helikes[:helikes.index(she)]
        for guy in shelikesbetter:
            guysgirl = inverseengaged[guy]
            guylikes = b[guy]
            if guylikes.index(guysgirl) > guylikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, guy, he, guysgirl))
                return False
        for gal in helikesbetter:
            girlsguy = engaged[gal]
            gallikes = a[gal]
            if gallikes.index(girlsguy) > gallikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, gal, she, girlsguy))
                return False
    return True

ra_position_preferences = {"yoder3":["J","E","T","S","M","R"],
                           "yoder4":["J","E","S","T","M","R"],
                           "kratz3":["M","J","S","E","T","R"],
                           "miller3":["S","M","J","E","T","R"],
                           "nofloor":["R","T","S","M","E","J"]}

applicants_floor_prefernce ={"J":["yoder3","yoder4","kratz3","miller3","nofloor"],
                             "E":["yoder3","yoder4","kratz3","miller3","nofloor"],
                             "S":["kratz3","miller3","yoder3","yoder4","nofloor"],
                             "M":["kratz3","miller3","nofloor","yoder3","yoder4"],
                             "T":["nofloor","yoder4","yoder3","kratz3","miller3"],
                             'R':["kratz3","miller3","yoder3","yoder4","nofloor"]
                             }


sensitivity_list=sensitivity_analysis(ra_position_preferences,applicants_floor_prefernce)

new_dic=[]
stabe=[]
i=0
while i<len(sensitivity_list):
    newdic1 = {k:v[:] for k, v in sensitivity_list[i][0].items()}
    newdic2 = {k:v[:] for k, v in sensitivity_list[i][1].items()}
    almaty=insert_dummies(newdic1,newdic2)
    z=StableMatching(almaty[0], almaty[1])
    stab=check(z,almaty[0], almaty[1])
    new_dic.append(z)
    stabe.append(stab)
    i=i+1
    
result = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in new_dic)]
d1=copy.deepcopy(ra_position_preferences)
d2=copy.deepcopy(applicants_floor_prefernce)
length_d1=len(d1.keys())
length_d2=len(d2.keys())
items_d1=list(d1.keys())
items_d2=list(d2.keys())
final_dic={}
for popo in items_d1:
    final_dic[popo]=[d[popo] for d in result]

df = pd.DataFrame(final_dic) #putting the results in the csv file
df.to_csv('myfile5.csv')