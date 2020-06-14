from rest_framework import serializers
from questionnaries.models import Question, Questionnary, Answer


class QuestionnarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnary
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'contents', 'questionnary')


class AnswerPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = (
            'image',
        )


class AnswerSerializer(serializers.ModelSerializer):
    qid = serializers.SerializerMethodField('get_question')
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Answer
        fields = (
            'qid',
            'contents',
        )
        read_only_fields = (
            'insert_date',
            'get_image_url',
        )

    def get_image_url(self, item):
        """ Return image full URL """
        request = self.context.get('request')
        return request.build_absolute_uri(item.image.url) if item.image else None
