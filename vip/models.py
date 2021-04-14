from django.db import models


class Vip(models.Model):
    text = models.TextField()
    secret_level = models.CharField(choices=(
        ('limited', 'limited'),
        ('unlimited', 'unlimited'),
        ('strongly','strongly')
    ), max_length=15)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.PositiveIntegerField(default=1)
    status = models.CharField(choices=(
        ('active', 'active'),
        ('dead', 'dead')
    ), max_length=10, default='active')

