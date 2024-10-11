
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserAcc



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	class Meta:
		model = get_user_model()
		fields = '__all__'
		#fields = ['email', 'password']

	def create(self, validated_data):
		user_password = validated_data.get('password', None)
		firstname = validated_data.get('firstname', '')
		lastname = validated_data.get('lastname', '')
		phone = validated_data.get('phone', '')
		db_instance = self.Meta.model(email=validated_data.get('email'), firstname=firstname, lastname=lastname, phone=phone)
		db_instance.set_password(user_password)
		db_instance.save()
		return db_instance



class UserLoginSerializer(serializers.Serializer):
	email = serializers.CharField(max_length=100)
	username = serializers.CharField(max_length=100, read_only=True)
	password = serializers.CharField(max_length=100, min_length=8, style={'input_type': 'password'})
	token = serializers.CharField(max_length=255, read_only=True)

