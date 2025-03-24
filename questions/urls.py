from django.urls import path
from .views import (
    RandomPart1QuestionView,
    RandomPart2QuestionView,
    RandomPart3QuestionView,
)

urlpatterns = [
    path("part1/random/", RandomPart1QuestionView.as_view(), name="random-part1"),
    path("part2/random/", RandomPart2QuestionView.as_view(), name="random-part2"),
    path("part3/random/", RandomPart3QuestionView.as_view(), name="random-part3"),
]
