from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Ad(models.Model):
    CONDITION_CHOICES = [
        ('new', 'Новое'),
        ('used', 'Б/у'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads')
    title = models.CharField(max_length=50)
    description = models.TextField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=100)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.condition})'


class ExchangeProposal(models.Model):
    STATUS_CHOICES = [
        ("pending", "Ожидает"),
        ("accepted", "Принято"),
        ("rejected", "Отклонено"),
    ]

    ad_sender = models.ForeignKey(Ad, related_name="sent_proposals", on_delete=models.CASCADE)
    ad_receiver = models.ForeignKey(Ad, related_name="received_proposals", on_delete=models.CASCADE)
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Обмен {self.ad_sender} на {self.ad_receiver} — {self.status}"