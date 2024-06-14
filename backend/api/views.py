import io
import os
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import File, UserProfile
from .serializers import FileSerializer, UserProfileSerializer
from django.http import JsonResponse
from googleapiclient.http import MediaIoBaseUpload
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import openai

# Google Drive upload function
def upload_file_to_drive(file_content, file_name):
    SCOPES = ['https://www.googleapis.com/auth/drive.file']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', SCOPES)
    service = build('drive', 'v3', credentials=creds)
    
    file_metadata = {'name': file_name}
    media = MediaIoBaseUpload(io.BytesIO(file_content), mimetype='application/octet-stream')
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')

# AI-based file naming suggestion function
def suggest_file_name(file_content):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-4-turbo",
        prompt=f"Suggest a name for this file content: {file_content}",
        max_tokens=100
    )
    return response.choices[0].text.strip()

# AI-based file categorization suggestion function
def suggest_file_category(file_content):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-4-turbo",
        prompt=f"Categorize this file content: {file_content}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# AI-based file tagging suggestion function
def suggest_file_tags(file_content):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Completion.create(
        engine="gpt-4-turbo",
        prompt=f"Suggest tags for this file content: {file_content}",
        max_tokens=50
    )
    tags = response.choices[0].text.strip().split(',')
    return [tag.strip() for tag in tags]

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_content = file.read()
        
        # Get AI suggestion for file name
        suggested_name = suggest_file_name(file_content.decode('utf-8'))
        
        # Get AI suggestion for file category and tags
        suggested_category = suggest_file_category(file_content.decode('utf-8'))
        suggested_tags = suggest_file_tags(file_content.decode('utf-8'))
        
        # Upload file to Google Drive
        file_id = upload_file_to_drive(file_content, suggested_name)
        
        # Save file info to database
        file_instance = File.objects.create(
            name=suggested_name, 
            category=suggested_category, 
            tags=suggested_tags,
            file_id=file_id
        )
        serializer = self.get_serializer(file_instance)
        return Response(serializer.data)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

@api_view(['GET'])
def search_files(request):
    query = request.query_params.get('q', '')
    if query:
        files = File.objects.filter(
            Q(name__icontains=query) | 
            Q(category__icontains=query) | 
            Q(tags__icontains=query)
        )
    else:
        files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)

def test_view(request):
    return JsonResponse({"message": "Hello, world!"})
