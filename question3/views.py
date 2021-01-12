from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

cl=[]  #list to store all the points input to the API, where each point is represented by a list of x and y 

# createdic function returns a dictionary where x coordinate is the key and count of their occurance in the points in list cl is their corresponding value. 
def createdic(cl):
    dic={}
    for i in range(len(cl)):
        ct=1 #variable to store the the count of occurance of x coordinate in points present in list cl. 
        for j in range(i+1,len(cl)):
            if cl[i][0] not in dic.keys() and cl[i][0]==cl[j][0]:
                ct+=1
        if cl[i][0] not in dic.keys():
            dic[cl[i][0]]=ct
    return dic
# grouppair function will return a list where each component is a list of points having same x coordinate.
def grouppair(dic,cl):
    gr=[]
    for i in dic.keys():
        sm=[]
        if dic[i]>1:
            for j in range(len(cl)):
                if cl[j][0]==i:
                    sm.append(cl[j])
            gr.append(sm)
    return gr

# findsquare returns a list of list where each component is a point and all the four points in the list sq forms a square.
def findsquare(gr):
    sq=[]
    for i in range(len(gr)):
        fl=gr[0] 
        for j in range(i+1,len(gr)):
            sl=gr[j]
            for k1 in range(len(fl)):
                for k2 in range(len(sl)):
                    if fl[k1][1]==sl[k2][1]:
                        if fl[k1] not in sq and sl[k2] not in sq and len(sq)<5:
                            sq.append(fl[k1])
                            sq.append(sl[k2])
                        if len(sq)==4:
                            return sq
    return sq
    
@api_view(["POST"])
def plot(data):
    data=json.loads(data.body)
    x=data["x"]
    y=data["y"]
    l=[x,y] #creating a list of x and y coordinates to represent a point of 2D plane.
    cl.append(l) #adding the point to the coordinate list.
    if len(cl)<4: #if less than 4 points are given input to the API, then no square can be formed.
        return JsonResponse({"status": "accepted"}, safe=False)
    else:
        dic=createdic(cl) #calling createdic function to to get a dictionary whre keys will be the x coordinate and their corresponding values will be the count of occurance of that x coordinates in points of list cl.
        if len(dic)==len(cl):# if no repetition of x coordinate in the points of cl list, then no square can be formed.
            return JsonResponse({"status": "accepted"}, safe=False)
        else:
            gr=grouppair(dic,cl)
            out=findsquare(gr)
            if len(out)==4:
                a1=tuple(out[0])
                a2=tuple(out[1])
                a3=tuple(out[2])
                a4=tuple(out[3])
                return JsonResponse({"status": f"success {a1} {a2} {a3} {a4}"}, safe=False)
            else:
                return JsonResponse({"status": "accepted"}, safe=False)
