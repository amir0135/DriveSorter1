from django.shortcuts import render
from rest_framework import viewsets
from .models import File
from .serializers import FileSerializer
from django.http import JsonResponse
from django.http import HttpResponse

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

def test_view(request):
    return JsonResponse({"message": "Hello, world!"})
