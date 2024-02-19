from rest_framework import serializers
from app1.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','firstname','lastname','email','password']


#Login Seializer
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model =Login
        fields = '__all__'

#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'


#Orders Serializer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields=['username','Delivary_Type','Payment_Status','Product_Name','Custamer_Name']

#Custemor Serializer


class CustamerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Custamer_Details
        fields='__all__'


#RatingSerializer
# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Rating
#         fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

#User Model Serializer
class AddCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Add_TO_Card
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email','password',]

#ProfileSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'

class UserChekSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','password']

class ProductDisplaySerilizer(serializers.ModelSerializer):
    Product_Name = ProductSerializer()
    class Meta:
        model = Image 
        fields = ['P_Images', 'ImageUrl','Product_Name']  # Include 'Product_Name' in the fields list


class LoginM(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields=['Email','Custamer_Name']


class AddCardDisplySerializer(serializers.ModelSerializer):
    Custamer_Name=LoginM()
    class Meta:
        model=Add_TO_Card 
        fields = ['Product_Name', 'Custamer_Name'] 
    








































#Product Image
        
        






















class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fielsd='__all__'


# class AddCardSerializer(serializers.Serializer):
#     class Meta:
#         model=Add_TO_Card
#         fields='__all__'

