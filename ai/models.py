from django.db import models

from users.models import User


class ChatSession(models.Model):

    prompt_count = models.PositiveIntegerField(default=0)
    start_date = models.TimeField()
    end_date = models.TimeField()
    last_interaction_time = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user.first_name}-{self.last_interaction_time}"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=225, null=True, blank=True)
    respomce = models.TextField(max_length=225, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.timestamp}"
