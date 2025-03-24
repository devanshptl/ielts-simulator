from django.shortcuts import render
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

# Create your views here.


class RandomPart1QuestionView(APIView):
    def get(self, request):
        question = Part1Question.objects.order_by("?").first()
        if question:
            serializer = Part1QuestionSerializer(question)
            return Response(serializer.data)
        return Response({"error": "No questions available"})


class RandomPart2QuestionView(APIView):
    def get(self, request):
        question = Part2Question.objects.order_by("?").first()
        if question:
            serializer = Part2QuestionSerializer(question)
            return Response(serializer.data)
        return Response({"error": "No questions available"})


class RandomPart3QuestionView(APIView):
    def get(self, request):
        question = Part3Question.objects.order_by("?").first()
        if question:
            serializer = Part3QuestionSerializer(question)
            return Response(serializer.data)
        return Response({"error": "No questions available"})
