from django.contrib.auth.models import AbstractUser
from django.db import models

class Admin(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='user_management_admin_set',  # Add a unique related_name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='user_management_admin_set',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Worker(models.Model):
    user = models.OneToOneField(Admin, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    contact_info = models.TextField()

    def __str__(self):
        return self.user.username

class Message(models.Model):
    sender = models.ForeignKey(Admin, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Admin, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.receiver.username}"

class Upload(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Upload by {self.worker.user.username}"

class TaskLog(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    task_description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"Task log by {self.worker.user.username} on {self.date}"
