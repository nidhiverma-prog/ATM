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
from django.contrib.auth import authenticate

@api_view(["POST"])
def Atm_card(carddata):
    try:
        card_no=json.loads(carddata.body)
        if card_no in range(10000000,100000000):
           return JsonResponse(card_no,safe=False)
        else:
            return JsonResponse("enter valid number",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)    
@api_view(["POST"])
def Atm_pin(pindata):  
    try:
        pin_no=json.loads(pindata.body) 
        if pin_no in range(1000,10000):

            return JsonResponse(pin_no,safe=False)
        else:
            return JsonResponse("enter valid number",safe=False)    
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])       
def authenticate_details(card_no,pin_no):
    card_no=data.get("card_no","")
    pin_no=data.get("pin_no","")

    if card_no and pin_no:
        user=authenticate(card_no=card_no,pin_no=pin_no)
        if user:
            return JsonResponse("User is authenticate",safe=False)
        else:
            return JsonResponse("User is authenticate",safe=False)   

