from rest_framework import serializers
from users.models import ProjectUser


class ProjectUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectUser
        fields = ['id', 'username', 'first_name', 'last_name']
