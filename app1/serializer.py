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


from rest_framework import serializers
from .models import Custamer_Details

class CustamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custamer_Details
        fields = '__all__'


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
        fields = ['id','P_Images', 'ImageUrl','Product_Name']  # Include 'Product_Name' in the fields list


class LoginM(serializers.ModelSerializer):
    class Meta:
        model=Login 
        fields=['Email','Custamer_Name']
class AdressSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Adress 
        fields='__all__'


class AddCardDisplySerializer(serializers.ModelSerializer):
    Custamer_Name=LoginM()
    class Meta:
        model=Add_TO_Card 
        fields = ['Product_Name', 'Custamer_Name'] 
class CuponCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=CupenCode 
        fields='__all__'
class CheckCuponCodeSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CheckCode 
        fields='__all__'

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Products  # Assuming Product is the name of your product model
        fields = ['Product_Name', 'Price','id']

class LoginsSerializer(serializers.ModelSerializer):
    class Meta:
        model =Login # Assuming Customer is the name of your customer model
        fields = ['Custamer_Name', 'Email']  
class ImgeLSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Image 
        fields=['ImageUrl']
class OrderLSerilizer(serializers.ModelSerializer):
    Product_Name=ProductsSerializer()
    class Meta:
        model=Orders 
        fields=["Product_Name",'Order_Id','Delivary_Type','Payment_Status','Date']

class LCOserilizer(serializers.ModelSerializer):
    ImageUrl=ImgeLSerilizer()
    Order_Id=OrderLSerilizer()
    Custamer_Name=LoginsSerializer()
    # 
    class Meta:
        model=Custamer_Details 
        # fields=['username','Product_Name','Custamer_Name','Order_Id','Delivary_Type','Payment_Status','Date']
        fields=['ImageUrl',"Order_Id","Custamer_Name",'Adress','Quantity','Total_Amount']
        fields='__all__'
class LSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['Custamer_Name', 'id']


class Oserilizer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    Product_Name=ProductsSerializer()
    class Meta:
        model = Orders 
        fields = ['Order_Id','Custamer_Name','Product_Name','username','Delivary_Type','Payment_Status','Date']

class CDSerilizer(serializers.ModelSerializer):
    Order_Id = Oserilizer()
    # Custamer_Name = LSerilizer()
    
    class Meta:
        model = Custamer_Details 
        fields = ['Order_Id', 'Quantity', 'Total_Amount', 'City', 'Adress', 'Full_Name', ]



class Oderserilizer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    ImageUrl=ProductDisplaySerilizer()
    class Meta:
        model = Orders 
        fields = ['Order_Id','Custamer_Name','ImageUrl','username','Delivary_Type','Payment_Status','Date']
class CDSerializer(serializers.ModelSerializer):
    Custamer_Name=LoginsSerializer()
    Order_Id=Oserilizer()
    class Meta:
        model=Custamer_Details 
        fields=['id','City','Total_Amount','Custamer_Name','Order_Id','Quantity','Adress','Full_Name']
    


    
    








































#Product Image
        
        






















class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Image
        fielsd='__all__'


# class AddCardSerializer(serializers.Serializer):
#     class Meta:
#         model=Add_TO_Card
#         fields='__all__'

