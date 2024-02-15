from django.shortcuts import render
import random
import datetime

# Get the current date


# Create your views here.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from app1.models import *
from django.http import HttpResponse
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import status
from app1.serializer import *
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from rest_framework import serializers

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def LoginDetails(request):
    if(request.method=='GET'):
        Data=Login.objects.all()
        Serializer_Data=LoginSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        print('POST')
        data=request.data 
        print(data)
        print(data['Custamer_Name'],data['Email'])

        serializer=LoginSerializer(data=data)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        data = request.data
        custamer_name = data.get('Customer_Name')  # Assuming 'Customer_Name' is the unique identifier
        if custamer_name:
            try:
                obj = Login.objects.get(Custamer_Name=custamer_name)
                serializer = LoginSerializer(obj, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Login.DoesNotExist:
                return Response("Customer not found", status=status.HTTP_404_NOT_FOUND)
        


#Product Details

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProductDetails(request):
    if(request.method=='GET'):
        Data=Products.objects.all()
        Serializer_Data=ProductSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        username = request.data.get('username')
        user = User.objects.get(username=username)
        request.data['username'] = user.pk
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        username = request.data.get('username')
        user = User.objects.get(username=username)
        # product_id = request.data.get('Id')
        request.data['username'] = user.pk
        if product_id is None:
            return Response({'error': 'Product ID is missing from the request'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Products.objects.get(Id=product_id)
        except Products.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(instance=product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            print('Ending')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        username = request.data.get('username')
        user = User.objects.get(username=username)
        product_id = request.data.get('Id')
        request.data['username'] = user.pk
        if product_id is None:
            return Response({'error': 'Product ID is missing from the request'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = Products.objects.get(Id=product_id)
            product.delete()

        except Products.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response({'Message':'DeletedSuccess'}, status=status.HTTP_200_OK)
    
#-----------------------------------------------------------------------------------
#------------------------------------------------------------------------
#---------------------------------------------------------------- 
    
# OrderDetails
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def OrderDetails(request):
    if(request.method=='GET'):
        Data=Orders.objects.all()
        Serializer_Data=OrderSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        print('POST')
        Data=request.data 
        pn=Data['Product_Name']
        PO=Products.objects.get(Product_Name=pn)
        print(PO.username)
    #-----------------Custaner_Name
        cn=Data['Custamer_Name']
        CO=Login.objects.get(Custamer_Name=cn)
        Data['Custamer_Name']=CO.pk
    #------------------Usename id POsting
        UO=User.objects.get(username=PO.username)
        Data['username']=UO.pk
    #-------------------Product id posting
        Data['Product_Name']=PO.pk    
    #---------------Serilization
        serializer = OrderSerializer(data=Data)
        print(Data)
        if(serializer.is_valid()):
             print('Ok')
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
       
 
# custemar Details
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def CustamerDetails(request):
    if(request.method=='GET'):
        Data=Custamer_Details.objects.all()
        Serializer_Data=CustamerSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        Data=request.data
        # -----------Custamer Name 
        cn=Data['Custamer_Name']
        CO=Login.objects.get(Custamer_Name=cn)
        Data['Custamer_Name']=CO.pk
        #---------------Product Name 
        pn=Data['Product_Name']
        PO=Products.objects.get(Product_Name=pn)
        Data['Product_Name']=PO.pk 
        #-----------------Order Id 
        OO=Orders.objects.filter(Custamer_Name=CO.pk,Product_Name=PO.pk)[0]
        print("order")
        Data["Order_Id"]=OO.Order_Id
        serializer = CustamerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #Ratings
# @api_view(['GET','POST','PATCH','PUT','DELETE'])
# def RatingDetails(request):
#     if(request.method=='GET'):
#         Data=Rating.objects.all()
#         Serializer_Data=RatingSerializer(Data,many=True)
#         return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
#     elif(request.method=='POST'):
#         data=request.data 
#         serializer=RatingSerializer(data=data)
#         if(serializer.is_valid()):
#              serializer.save()
#              return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    






# @api_view(['GET','POST','PATCH','PUT','DELETE'])
# def AddCardDetails(request):
#     if(request.method=='GET'):
#         Data=Add_TO_Card.objects.all()
#         Serializer_Data=AddCardSerializer(Data,many=True)
#         return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
#     elif(request.method=='POST'):
#         data=request.data 
#         serializer=AddCardSerializer(data=data)
#         if(serializer.is_valid()):
#              serializer.save()
#              return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#ProfileDetails
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProfileDetails(request):
    if(request.method=='GET'):
        Data=Profile.objects.all()
        Serializer_Data=ProfileSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        data=request.data 
        user=data['username']
        UO=User.objects.get(username=user)
        data['username']=UO.pk 
        serializer=ProfileSerializer(data=data)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            
        
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def  UserDetails(request):
    if(request.method=='GET'):
        Data=User.objects.all()
        Serializer_Data=UserSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        data=request.data 
        serializer=UserSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            send_mail('Registration',
            'Thanku For Registration',
            'venkateswarlureddy647@gmail.com',
             [data['email']],
            fail_silently=True,
             )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ImageDetails(request):
    if(request.method=='GET'):
        Data=Image.objects.all()
        Serializer_Data=ImageSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
        pname = request.data.get('Product_Name')
        print('POst')
        PO =Products.objects.get(Product_Name=pname)
        request.data['Product_Name'] =PO.pk
        serializer =ImageSerializer(data=request.data)
        print('Yes')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)














    


    
    



