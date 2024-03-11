from django.shortcuts import render
import random
import datetime

# # Get the current date


# # Create your views here.
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
            serializer.save()
            send_mail('Login Information',
            'Thanku For Creating Account',
            'venkateswarlureddy647@gmail.com',
             [data['Email']],
            fail_silently=True,
             )
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
        

# from django.http import HttpResponseRedirect


# #Product Details

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
    

# # OrderDetails
    
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
        if(serializer.is_valid()):
          
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
    elif request.method == 'POST':
        LO=Login.objects.get(pk=request.data['Custamer_Name'])
        IOL=Image.objects.filter(ImageUrl=request.data['ImageUrl'])
        UO=User.objects.get(pk=request.data['username'])
        PO=Products.objects.get(pk=request.data['Product_Name'])
        OOL=Orders.objects.filter(Custamer_Name=LO,username=UO,Product_Name=PO)
        request.data.pop('username')
        request.data.pop('Product_Name')
        print(request.data)
        IO=IOL[len(IOL)-1]
        OO=OOL[len(OOL)-1]
        request.data['Order_Id']=OO.Order_Id
        request.data["ImageUrl"]=IO.pk
        print(OO.Order_Id)
        serializer = CustamerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)
            
        return Response({"Message":"Yes"}, status=status.HTTP_201_CREATED)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def AddCardDetails(request):
    if(request.method=='GET'):
        Data=Add_TO_Card.objects.all()
        Serializer_Data=AddCardSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        data=request.data 
        serializer=AddCardSerializer(data=data)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



#ProfileDetails
@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ProfileDetails(request):
    if(request.method=='GET'):
        Data=Profile.objects.all()
        Serializer_Data=ProfileSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        P_url=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data['P_Url']=P_url
        serializer=ProfileSerializer(data=request.data)
        if(serializer.is_valid()):
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        Po=Profile.objects.get(pk=request.data['pk'])
        P_url=request.build_absolute_uri(request.data['Profile_Pic'])
        request.data.pop('Profile_Pic')
        print(P_url)
        request.data['P_Url']=P_url
        serializer=ProfileSerializer(Po,data=request.data,partial=True)
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
            print('va')
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            send_mail('Registration',
            'Thanku For Registration',
            'venkateswarlureddy647@gmail.com',
             [data['email']],
            fail_silently=True,
             )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif(request.method=='PATCH'):
        Uo=User.objects.get(pk=request.data['pk'])
        serializer=UserSerializer(Uo,data=request.data,partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PATCH','PUT','DELETE'])
def ImageDetails(request):
    if(request.method=='GET'):
        Data=Image.objects.all()
        Serializer_Data=ImageSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif request.method == 'POST':
    # Create and validate serializer
        request.data['ImageUrl']=request.build_absolute_uri(request.data['P_Images'])
        serializer = ImageSerializer(data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
          
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        print('PATCH')
        image_pk = request.data['pk']  # Assuming 'pk' is the primary key of the Image object
        image_obj = Image.objects.get(pk=image_pk)
        request.data['ImageUrl'] = request.build_absolute_uri(request.data['P_Images'])
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            IO=Image.objects.get(pk=image_obj.pk)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        imo=Image.objects.get(pk=request.data['pk'])
        imo.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def UpdateDetails(request):
    if(request.method=='PATCH'):
        image_pk = request.data['pk']  # Assuming 'pk' is the primary key of the Image object
        image_obj = Image.objects.get(pk=image_pk)
        print(image_obj.P_Images)
        request.data['ImageUrl'] = request.build_absolute_uri(request.data['P_Images'])
        request.data.pop('P_Images') 
        serializer = ImageSerializer(image_obj, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            IO=Image.objects.get(pk=image_obj.pk)
            print(IO.P_Images)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
        Serializer_Data=AddCardDisplySerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        email=request.data['Custamer_Name']
        print(email)
        CO=Login.objects.get(Email=email)
        request.data['Custamer_Name']=CO.pk
        print(CO.pk)
        serializer=AddCardSerializer(data=request.data)
        if(serializer.is_valid()):
             print('bye')
             serializer.save()
             return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"Message":'Success'},status=status.HTTP_201_CREATED)
    elif(request.method=='DELETE'):
        try:
            customer_id = request.data.get('Custamer_Name')
            Product_id=Products.objects.get(pk=request.data['Product_Name'])
            customer = Login.objects.get(pk=customer_id)
            cart_item = Add_TO_Card.objects.get(Custamer_Name=customer, Product_Name=Product_id)   
        except Add_TO_Card.DoesNotExist:
            return Response({"Message": "Error: Cart item not found"}, status=status.HTTP_404_NOT_FOUND)

        # Initialize serializer with instance to delete
        serializer = AddCardSerializer(instance=cart_item)
        # Perform deletion
       
        cart_item.delete()
        return Response({"Message": "Success"}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def CuponCodeDetails(request):
    if(request.method=='GET'):
        Data=CupenCode.objects.all()
        Serializer_Data=CuponCodeSerializer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        serializers=CuponCodeSerializer(data=request.data)
        if(serializers.is_valid()):
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PATCH','PUT','DELETE'])
def CheckCodeDetails(request):
    if(request.method=='GET'):
        Data=CheckCode.objects.all()
        Serializer_Data=CheckCuponCodeSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
    elif(request.method=='POST'):
        CO=CupenCode.objects.get(pk=request.data['Code_Name'])
        print(CO.Limit)
        CCO=CheckCode.objects.filter(Code_Name=request.data['Code_Name'])
        print(len(CCO))
        if(int(CO.Limit)>len(CCO)):
            request.data['Times']=len(CCO)+1
            print(request.data['Times'])
            serializers=CheckCuponCodeSerilizer(data=request.data)
            if(serializers.is_valid()):
                serializers.save()
                return Response({"Message":True},status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"Message":False},status=status.HTTP_201_CREATED)


@api_view(['GET'])
def LCODetails(request):
    if request.method == 'GET':
        Data=Custamer_Details.objects.all()
        Serializer_Data=LCOserilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)

from random import randint
@api_view(['GET','POST'])
def OtpDetails(request):
    if(request.method=='POST'):
        UO=User.objects.filter(username=request.data['username'])
        if(len(UO)>0):
            otp=randint(1000,9999)
            send_mail('Forget Password OTP',
            f'You Otp is ${otp}',
            'venkateswarlureddy647@gmail.com',
             [UO[0].email],
            fail_silently=True,
             )
            return Response({"Message":otp},status=status.HTTP_201_CREATED)   
        return Response({"Message":"UserName Not Valid"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['PATCH'])
def ForgetDetails(request):
    if(request.method=='PATCH'):
        UO=User.objects.get(username=request.data['username'])
        serializer=UserSerializer(UO,data=request.data,partial=True)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def CDDetails(request):
    if(request.method=='GET'):
        Data=Custamer_Details.objects.all()
        Serializer_Data=CDSerilizer(Data,many=True)
        return Response(Serializer_Data.data,status=status.HTTP_201_CREATED)
# from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.crypto import get_random_string

@api_view(['POST'])
def LoginOtpDetails(request):
    if request.method == 'POST':
        email = request.data.get('Email')  # Get email from request data 
        user_exists = Login.objects.filter(Email=email).exists()
        if user_exists:
            otp = get_random_string(length=4, allowed_chars='0123456789')  # Generate OTP
            send_mail('Forget Password OTP',
                      f'Your OTP is {otp}',
                      'venkateswarlureddy647@gmail.com',
                      [email],
                      fail_silently=True)
            return JsonResponse({"Message": otp}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({"Message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({"Message": "Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
@api_view(['PATCH'])
def LoginPasswordChange(request):
    LE=Login.objects.get(Email=request.data['Email'])
    serializer=LoginSerializer(LE,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({"Message":'Success'},status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def OrderDisplayDetails(request):
    Data = Custamer_Details.objects.all()
    Serializer_Data = CDSerializer(Data, many=True)
    return Response(Serializer_Data.data, status=status.HTTP_200_OK)








            
        
            
        
        

        



          
        


















    

from django.http import JsonResponse    
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        print('POST')
        image_instance = Image.objects.create(image_url=image.url)
        image_instance.save()
        return JsonResponse({'url': image_instance.request.build_absolute_uri(image.url)})
    return JsonResponse({'error': 'No image provided'}, status=400)


