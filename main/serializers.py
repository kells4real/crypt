from rest_framework import serializers
from .models import Transaction, AuthUser, AvailableBtc
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionCrudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('memo', 'amount', 'sent', 'address')

class AvailableSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableBtc
        fields = '__all__'


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = AuthUser.objects.get(username=obj['username'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access'],
        }

    class Meta:
        model = AuthUser
        fields = ['username', 'password', 'tokens', 'id']

    def validate(self, attrs):
        username = attrs.get('username', '')
        password = attrs.get('password', '')
        filtered_user_by_email = AuthUser.objects.filter(username=username)
        user = auth.authenticate(username=username, password=password)

        # if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
        #     raise AuthenticationFailed(
        #         {'detail':'Please continue your sign in with ' + filtered_user_by_email[0].auth_provider + ' or reset your password and be able to sign in either through google or by using your email and new password',
        #          'error': "email is google"})
        #
        # if not user:
        #     raise AuthenticationFailed('Invalid credentials, try again')
        # if not user.is_active:
        #     raise AuthenticationFailed('Account disabled, contact admin')
        # if not user.is_verified:
        #     raise AuthenticationFailed('Email is not verified')

        return {
            'username': user.username,
            'tokens': user.tokens,
            'id': user.id,
        }

        return super().validate(attrs)
