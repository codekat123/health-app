from rest_framework import serializer
from account.models import Account




class ResgisterSerializer(serializer.ModelSerializer):
     class Meta:
          model = Account
          fields =['first_name','last_name','password','email','country','phone_number']
     
     def create(self,validated_data):
          user = Account.objects.create_user(
               first_name = validated_data['first_name'],
               last_name = validated_data['last_name'],
               email =  validated_data['email'],
               username = validated_data['user_name'],
               country = validated_data['country'],
          )
          return user

