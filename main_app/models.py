from django.db import models


class Ads(models.Model):
    class Meta:
        verbose_name_plural = 'Ads'
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
