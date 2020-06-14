from questionnaries.views import AnswerViewSet, QuestionViewSet, QuestionnaryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'questionnaries', QuestionnaryViewSet, basename='questionnary')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'answers', AnswerViewSet, basename='answer')
urlpatterns = router.urls
