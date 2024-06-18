from django.db import models
from django.contrib.auth.models import User

class QueuedAction(models.Model):
    ACTION_TYPES = [
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete'),
    ]
    action_type = models.CharField(max_length=6, choices=ACTION_TYPES)
    model_name = models.CharField(max_length=100)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.action_type} {self.model_name} at {self.timestamp}"

class SynchronizationLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

    def __str__(self):
        return f"Synchronization log for {self.user.username} at {self.timestamp}"
