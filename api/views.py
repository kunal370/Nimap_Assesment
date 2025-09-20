from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Client, Project, User
from .serializers import ClientSerializer, ProjectSerializer, ProjectCreateSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class ProjectCreateAPIView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        client_id = self.kwargs.get('client_id')
        client = Client.objects.get(pk=client_id)
        return {
            'request': self.request,
            'client': client,
            'created_by': self.request.user
        }

class MyProjectsListAPIView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects.all()
