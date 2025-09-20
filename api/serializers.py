
from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    client = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'users', 'client', 'created_at', 'created_by']

    def get_created_by(self, obj):
        try:
            return obj.created_by.username
        except:
            return None


class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'updated_at', 'created_by']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'users']

    def create(self, validated_data):
        users = validated_data.pop('users', [])
        client = self.context['client']
        created_by = self.context['created_by']
        project = Project.objects.create(client=client, created_by=created_by, **validated_data)
        project.users.set(users)
        return project
