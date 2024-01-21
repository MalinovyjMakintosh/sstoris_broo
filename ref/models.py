from django.db import models
from django.contrib.auth.models import User

class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrer')
    referral = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referral')