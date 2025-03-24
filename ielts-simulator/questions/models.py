from django.db import models

# Create your models here.


class Part1Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Part 1: {self.question_text[:50]}..."


class Part2Question(models.Model):
    topic = models.CharField(max_length=200)
    question_text = models.TextField()
    points_to_cover = models.TextField(
        help_text="Points that the candidate should cover in their answer"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Part 2: {self.topic}"


class Part3Question(models.Model):
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Part 3: {self.question_text[:50]}..."
