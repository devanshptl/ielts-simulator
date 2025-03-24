from django.contrib import admin
from .models import Part1Question, Part2Question, Part3Question


@admin.register(Part1Question)
class Part1QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "created_at")
    search_fields = ("question_text",)


@admin.register(Part2Question)
class Part2QuestionAdmin(admin.ModelAdmin):
    list_display = ("topic", "created_at")
    search_fields = ("topic", "question_text")


@admin.register(Part3Question)
class Part3QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "created_at")
    search_fields = ("question_text",)
