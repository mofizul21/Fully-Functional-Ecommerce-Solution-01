from django.db import models
from django.db.models import CharField


class Slider(models.Model):
    primary_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    day = models.CharField(max_length=55, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    float_price = models.IntegerField(blank=True, null=True)
    button_text = models.CharField(max_length=55, blank=True, null=True)
    image = models.ImageField(upload_to='slider', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Sliders'
