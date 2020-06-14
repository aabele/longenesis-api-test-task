from rest_framework import viewsets
from rest_framework import authentication
from rest_framework import permissions
from rest_framework import decorators
from rest_framework import response
from rest_framework import status
from rest_framework import exceptions


from questionnaries.models import Answer, Question, Questionnary
from questionnaries.serializers import AnswerSerializer, AnswerPictureSerializer, QuestionSerializer, \
    QuestionnarySerializer
from users.permissions import SuperUserOrReadOnly


class QuestionnaryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnarySerializer
    queryset = Questionnary.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, SuperUserOrReadOnly]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, SuperUserOrReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    image_serializer_class = AnswerPictureSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, SuperUserOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return Answer.objects.all()

        return Answer.objects.filter(author=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @decorators.action(detail=True,
                       url_path='upload-image',
                       methods=['post'],
                       permission_classes=permission_classes,
                       authentication_classes=authentication_classes)
    def upload_image(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise exceptions.PermissionDenied('You must be superuser in order to access this endpoint.')

        serializer = self.image_serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @decorators.action(detail=False,
                       url_path='create-many',
                       methods=['post'],
                       permission_classes=permission_classes,
                       authentication_classes=authentication_classes)
    def create_many(self, request, *args, **kwargs):
        """
        Allow to submit multiple items in single http requests
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
