from django.shortcuts import render
from . serializer import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework import generics
from rest_framework.views import APIView
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":True,"message": "User created successfully" ,"data":{}})
        return Response(
            {
                "status" : False,
                "message": "Invalid data",
                "data" : serializer.errors
            }
        )


class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            
            print(f"Authenticating user: {username}")  # Debugging
            user = authenticate(username=username, password=password)
            
            if user is None:
                print("Invalid credentials")
                return Response(
                    {"status": False, "message": "Invalid credentials", "data": serializer.errors}
                )
            
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"status": True, "message": "User logged in successfully", "data": {"token": token.key}}
            )
        else:
            print("Serializer errors:", serializer.errors)  # Debugging
            return Response(
                {"status": False, "message": "Invalid input", "data": serializer.errors}
            )

@api_view(['GET'])
def get_list(request):
    location = request.GET.get('location')
    list = FoodListing.objects.all()
    list = list.filter(location__icontains=location)
    serializer = ListSerializer(list,many = True)
    return Response(
        {
        "status":True,
        "message":"list fetched",
        "data":serializer.data
        }
    )

@api_view(['POST'])    
def add_list(request):
    if request.method == 'POST':
        data = request.data
        serializer = ListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":True,"message":"list added","data":serializer.data})
        else:
            return Response({"status":False,"message":"list not added","data":serializer.errors})