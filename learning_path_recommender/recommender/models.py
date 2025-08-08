from django.db import models
from django.contrib.auth.models import User

class Recommendation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recommendations')
    skill = models.CharField(max_length=100, default='')
    goal = models.CharField(max_length=100, default='')
    courses = models.TextField(default='')
    youtube_links = models.TextField(default='')
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.skill} - {self.goal}"

class SkillQuiz(models.Model):
    skill = models.CharField(max_length=100, default='')
    question = models.TextField(default='')
    option1 = models.CharField(max_length=255, default='')
    option2 = models.CharField(max_length=255, default='')
    option3 = models.CharField(max_length=255, default='')
    option4 = models.CharField(max_length=255, default='')
    correct_option = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.skill} - {self.question[:50]}"
