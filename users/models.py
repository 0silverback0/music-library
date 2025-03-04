from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    producer_name = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=150, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    pro = models.CharField(max_length=100, blank=True, null=True)  # PRO organization (ASCAP, BMI, etc.)
    pro_number = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.producer_name

class Beat(models.Model):
    producer = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    bpm = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file_url = models.URLField(max_length=200, default='N?A')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('producer', 'title', 'file_url')

    def __str__(self):
        return f'{self.title} - {self.producer}'
