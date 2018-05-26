from django.shortcuts import render
from .models import Language, Employee, Company
from .serializers import LanguageSerializer, CompanySerializer, EmployeeSerializer
from rest_framework import viewsets, permissions

# Create your views here.
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
