from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import F
from django.db.models.functions import Random
from .models import Part1Question, Part2Question, Part3Question
from .serializers import (
    Part1QuestionSerializer,
    Part2QuestionSerializer,
    Part3QuestionSerializer,
)


class RandomPart1QuestionView(APIView):
    def get(self, request):
        question = Part1Question.objects.order_by(Random()).first()
        serializer = Part1QuestionSerializer(question)
        return Response(serializer.data)


class RandomPart2QuestionView(APIView):
    def get(self, request):
        question = Part2Question.objects.order_by(Random()).first()
        serializer = Part2QuestionSerializer(question)
        return Response(serializer.data)


class RandomPart3QuestionView(APIView):
    def get(self, request):
        question = Part3Question.objects.order_by(Random()).first()
        serializer = Part3QuestionSerializer(question)
        return Response(serializer.data)
