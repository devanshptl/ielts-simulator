from rest_framework import serializers
from .models import Part1Question, Part2Question, Part3Question


class Part1QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part1Question
        fields = ["id", "question_text"]


class Part2QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part2Question
        fields = ["id", "topic", "question_text", "points_to_cover"]


class Part3QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Part3Question
        fields = ["id", "question_text"]
