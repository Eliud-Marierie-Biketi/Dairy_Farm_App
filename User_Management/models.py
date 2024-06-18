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
