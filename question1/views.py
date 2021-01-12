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

@api_view(["POST"])
def items(data):
    try:
        data=json.loads(data.body)
        ve=0 #variable to store number of valid enteries.
        ive=0 #variable to store number of invalid enteries
        sum=0
        l=[] #list to store all valid enteries.
        for i in data:
            if  type(i)==int and i>0: #if enteries are positive integer
                l.append(i)
                ve+=1
                sum=sum+i
            else:
                ive+=1
        avg=sum/ve
        mn=min(l)
        mx=max(l)
        return JsonResponse({
            "valid_enteries": ve,
            "invalid_enteries": ive,
            "min": mn,
            "max": mx,
            "average": avg
        }, safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


