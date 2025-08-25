from rest_framework import serializers
from account.models import Account




class ResgisterSerializer(serializers.ModelSerializer):
     class Meta:
          model = Account
          fields =['first_name','last_name','password','email','country','phone_number','user_name']
     
     def create(self,validated_data):
          user = Account.objects.create_user(
               first_name = validated_data['first_name'],
               last_name = validated_data['last_name'],
               email =  validated_data['email'],
               user_name = validated_data['user_name'],
               country = validated_data['country'],
               phone_number = validated_data['phone_number'],
               password = validated_data['password'],
          )
          return user

