from django.db import models
from django.contrib.auth.models import User


# Get the current date and time



# Create your models here.
#Profile Model
class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_Pic=models.ImageField()

# #Login Custemor Details
class Login(models.Model):
    Email=models.EmailField()
    Custamer_Name=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Mobile_Number=models.IntegerField()
    def __str__(self):
        return self.Custamer_Name


# #Store Products
class Products(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE,)
    Description=models.TextField(null=True,blank=True)
    Product_Name=models.CharField(max_length=100)
    Category=models.CharField(max_length=100)
    Category_Name=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=10, decimal_places=2)
    Stack=models.IntegerField()
    Out_Of_Stack=models.BooleanField(default=False)
    def __str__(self):
        return self.Product_Name
# #Stroe Multiple Images
class Image(models.Model):
    Product_Name = models.ForeignKey(Products, related_name='images', on_delete=models.CASCADE)
    P_Images = models.ImageField(upload_to='product_images/')

#Orders Storing

class Orders(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE) 
    Order_Id=models.AutoField(primary_key=True)
    Delivary_Type=models.CharField(max_length=100)
    Payment_Status=models.CharField(max_length=100)
    Product_Name=models.ForeignKey(Products,on_delete=models.CASCADE)
    Date=models.DateTimeField(auto_now_add=True )
    def __str__(self) :
        return str(self.Order_Id)
class Custamer_Details(models.Model):
    Custamer_Name=models.ForeignKey(Login,on_delete=models.CASCADE) 
    Order_Id=models.OneToOneField(Orders,on_delete=models.CASCADE)
    Total_Amount=models.IntegerField()
    City=models.CharField(max_length=100)
    Adress=models.TextField()
    Full_Name=models.CharField(max_length=100,null=True,blank=True)
    

# class Rating(models.Model):
#     user_name=models.ForeignKey(User,on_delete=models.CASCADE)
#     # Custamer_Name=models.ForeignKey(Custamer_Details,on_delete=models.CASCADE)
#     Rating =models.DecimalField(max_digits=3, decimal_places=2)
#     Rating_Message=models.TextField(null=True,blank=True)
#     Product_Name=models.ForeignKey(Products,on_delete=models.CASCADE)
    

# class Add_TO_Card(models.Model):
#     Custamer_Name=models.ForeignKey(Custamer_Details,on_delete=models.CASCADE)
#     Product_Name=models.ForeignKey(Products,on_delete=models.CASCADE)
    
    