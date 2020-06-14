from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import authentication

from users.models import ProjectUser
from users.serializers import ProjectUserSerializer
from users.permissions import SuperUserOrReadOnly


class ProjectUserViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectUserSerializer
    queryset = ProjectUser.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, SuperUserOrReadOnly]
