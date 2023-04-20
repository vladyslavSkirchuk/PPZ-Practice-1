from django.db import models


class Task(models.Model):
    low = 'LOW'
    mid = 'MIDDLE'
    high = 'HIGH'
    PRIORITY_ENUM = [
        (low, 'LOW'),
        (mid, 'MIDDLE'),
        (high, 'HIGH')
    ]
    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=6,
        choices=PRIORITY_ENUM,
        default=low
    )
    published_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_absolute_url():
        from django.urls import reverse
        return reverse('task_list')
