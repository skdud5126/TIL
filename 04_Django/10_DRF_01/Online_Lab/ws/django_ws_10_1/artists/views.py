from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def artist_list(request):
    if request.method =='GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many = True)
        return Response(serializer.data)
    
    elif request.method =='POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        