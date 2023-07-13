from django.db import models


class CoffeeShop(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=1)
    coffee_rating = models.DecimalField(max_digits=3, decimal_places=1)
    food_rating = models.DecimalField(max_digits=3, decimal_places=1)
    price_rating = models.DecimalField(max_digits=3, decimal_places=1)
    vibe_rating = models.DecimalField(max_digits=3, decimal_places=1)
    wifi_rating = models.DecimalField(max_digits=3, decimal_places=1)
    quiet_rating = models.DecimalField(max_digits=3, decimal_places=1)
    meeting_rating = models.DecimalField(max_digits=3, decimal_places=1)
    study_work_rating = models.DecimalField(max_digits=3, decimal_places=1)

    def __str__(self):
        return self.name


class Review(models.Model):
    coffee_shop = models.CharField(max_length=100)
    overall_rating = models.DecimalField(max_digits=3, decimal_places=1)
    coffee_rating = models.DecimalField(max_digits=3, decimal_places=1)
    food_rating = models.DecimalField(max_digits=3, decimal_places=1)
    review_text = models.TextField()

    def __str__(self):
        return f"Review for {self.coffee_shop}"