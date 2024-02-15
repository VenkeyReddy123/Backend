from rest_framework import serializers
from app1.models import *
from django.contrib.auth.models import User

# class UserSerai(serializers.Serializer):
#     class Meta:
#         model:User
#         fields:['first_name','last_name','email']
        
# class ProfileSerai(serializers.Serializer):
#     class Meta:
#         model:Profile
#         fields:['adress']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User 
        fields=['username','firstname','lastname','email']


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




class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fields='__all__'

#User Model Serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'first_name', 'last_name', 'email',]

#ProfileSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'


































#Product Image
        
        






















class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fielsd='__all__'


# class AddCardSerializer(serializers.Serializer):
#     class Meta:
#         model=Add_TO_Card
#         fields='__all__'

