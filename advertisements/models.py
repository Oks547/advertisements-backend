from django.db import models
from django.contrib.auth.models import User

class Advertisement(models.Model):
    STATUS_CHOICES = (
        ('OPEN', 'Открыто'),
        ('CLOSED', 'Закрыто'),
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='advertisements')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title