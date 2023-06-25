from django.db import models


class Teams(models.Model):
    class Meta:
        verbose_name_plural = 'Teams'

    full_name = models.CharField(max_length=254)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name
