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

# Create your views here.
book=[] #list to store booking details where each component is a dictionary of format {"slot":slotno,"name":name}
slotdic={} #dictionary where keys represent booked slot with number of bookings in that slot as value.

@api_view(["GET","POST"])
def booking(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body)
            slot=data["slot"]
            name=data["name"]
            if slot in range(24):
                if slot not in slotdic.keys():
                    slotdic[slot]=1
                    
                    dic={
                        "slot": slot,
                        "name": name
                    }
                    book.append(dic)
                    return JsonResponse({"status": "confirmed"}, safe=False)

                else:
                    if slotdic[slot]==1: #if number of booking for that perticular slot is one,than one more booking can be confirmed.
                        slotdic[slot]=2
                        for i in range(len(book)):
                            if book[i]["slot"]==slot:
                                l=[]
                                n=book[i]["name"]
                                l.append(name)
                                l.append(n)
                                book[i]["name"]=l
                                break
                        return JsonResponse({"status": "confirmed"}, safe=False)
                
                    else:
                        return JsonResponse({"status": f"slot full, unable to save booking for {name} in slot {slot}",}, safe=False)
        except ValueError as e:
            return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
    
    elif request.method=="GET":
        return JsonResponse(book, safe=False)


@api_view(["POST"])
def cancel(data):
    try:
        if(data.method=="POST"):
            data=json.loads(data.body)
            slot=data["slot"]
            name=data["name"]
            s=slotdic[slot]-1
            slotdic[slot]=s
            if slot in range(24):
                if slot in slotdic.keys(): #check if slot is in booked slots or not 
                    cond=0 #flag value to determine whether input name is present in the dictionary having key as the matched slot is present in the list book.
                    for i in range(len(book)):
                        if book[i]["slot"]==slot:
                            l=book[i]["name"]
                            if type(l)==list:
                                for j in range(len(l)):
                                    if l[j]==name:
                                        l.pop(j)
                                        cond=1
                                        break
                                    else:
                                        cond=0
                                if len(l)==1:
                                    n=l[0]
                                    book[i]["name"]=n
                                    break
                            elif type(l)==str:
                                if book[i]["name"]==name:
                                    cond=1
                                    book.pop(i)
                                    break
                    if cond==1: #means found the matchind data in list book.
                        return JsonResponse({"status": f"cancelled booking for {name} in slot {slot}"}, safe=False)
                    else:
                        return JsonResponse({"status": f"no booking for the name {name} in slot {slot}"}, safe=False)
            else:
                    return JsonResponse({f"wrong input for slot {slot}"}, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


