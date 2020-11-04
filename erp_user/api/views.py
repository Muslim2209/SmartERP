from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from rest_framework import generics, permissions

from customer.models import Customer
from erp_user.api.serializers import UserSerializer
from erp_user.decorators import unauthenticated_user, allowed_users
from erp_user.forms import CreateUserForm, CustomerForm
from tools.config import CONSTANTS


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
