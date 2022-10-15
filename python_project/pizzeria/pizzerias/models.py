from django.db import models


class Pizza(models.Model):
    """
    pizza model
    """
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """
        return pizza object str
        """
        return self.name


class Topping(models.Model):
    """
    topping model
    """
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "toppings"

    def __str__(self) -> str:
        """
        return topping object str
        """
        return self.name
