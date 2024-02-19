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
        data=request.data 
        serializer=LoginSerializer(data=data)
        if(serializer.is_valid()):
             serializer.set_password(data['Pasword'])
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
        
























from django.http import HttpResponseRedirect


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
    elif request.method=='PATCH':
        print('Patch')
        print(request.data['pk'])
        PO=Products.objects.get(pk=request.data['pk'])
        serializer=ProductSerializer(PO,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        PO=Products.objects.get(pk=request.data['pk'])
        serializer=ProductSerializer(PO,data=request.data,partial=True)
        if serializer.is_valid():
            PO.delete()
            return Response({"Message":"Success"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
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
        email=request.data['Custamer_Name']
        CO=Login.objects.get(Email=email)
        request.data['Custamer_Name']=CO.pk
        serializer = OrderSerializer(data=request.data)
        print('ok')
        if(serializer.is_valid()):
             print('okok')
             serializer.save()
             print('okok')
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
    elif request.method == 'POST':
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            print(serializer.validated_data)
            # Get validated data
            validated_data = serializer.validated_data
            # Create a new user instance with validated data
            user = serializer.create(validated_data)
            # Set the password for the user
            user.set_password(data['password'])
            # Save the user with the updated password
            user.save()
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
        PO =Products.objects.get(Product_Name=pname)
        request.data['Product_Name'] =PO.pk
        request.data['ImageUrl']=request.build_absolute_uri( request.data['P_Images'])
        serializer =ImageSerializer(data=request.data)
        print('Yes')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='PATCH':
        # pname = request.data.get('Product_Name')
        # PO =Products.objects.get(Product_Name=pname)
        # request.data['Product_Name'] =PO.pk
        IO=Image.objects.get(pk=request.data['pk'])
        request.data['ImageUrl']=request.build_absolute_uri(request.data['P_Images'])
        print(request.data['ImageUrl'])
        request.data.pop('P_Images')
        serializer =ImageSerializer(IO,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth import authenticate
@api_view(['POST'])
def UserCheckDetails(request):
    if(request.method=='POST'):
        un=request.data.get('username')
        pw=request.data.get('password')
        AUO=authenticate(username=un,password=pw)
        if(AUO):
            print(True)
            return Response({"Message":True},status=status.HTTP_201_CREATED)
        else:
            print(False)
            return Response({"Message":False},status=status.HTTP_201_CREATED)
           
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProductDispalyView(request):
    if(request.method=='GET'):
        Data=Image.objects.all()
        Serializer_Data=ProductDisplaySerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def AddCardDetails(request):
    if(request.method=='GET'):
        Data=Add_TO_Card.objects.all()
        Serializer_Data=AddCardSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        email=request.data['Custamer_Name']
        CO=Login.objects.get(Email=email)
        request.data['Custamer_Name']=CO.pk
        print('hi')
        serializer=AddCardSerializer(data=request.data)
        if(serializer.is_valid()):
             print('bye')
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



          
        


















    


    
    



