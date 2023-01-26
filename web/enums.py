from django.db import models


class Category(models.TextChoices):
    study = "study", "Учеба"
    food = "food", "Еда"
    credit = "credit", "Кредиты"
    health = "health", "Здоровье"
    purchase = "purchase", "Покупки"
    other = "other", "Другое"
