# backend/api/views.py

import io
import os
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
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
        max_tokens=100  )
    return response.choices[0].text.strip()

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_content = file.read()
        
        # Get AI suggestion for file name
        suggested_name = suggest_file_name(file_content.decode('utf-8'))
        
        # Upload file to Google Drive
        file_id = upload_file_to_drive(file_content, suggested_name)

        # Save file info to database
        file_instance = File.objects.create(name=suggested_name, category='', file_id=file_id)
        serializer = self.get_serializer(file_instance)
        return Response(serializer.data)

def test_view(request):
    return JsonResponse({"message": "Hello, world!"})
