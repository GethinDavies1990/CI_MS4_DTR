# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Teams(models.Model):
    """
    A class for the Teams Model
    """

    class Meta:
        """
        A class for the Meta Teams Model
        """

        verbose_name_plural = "Teams"

    full_name = models.CharField(max_length=254)
    role = models.CharField(max_length=254, null=True)
    about = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """
        Return new title string
        Args:
            self (object): self
        Returns:
            news title
        """
        return self.full_name
