from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BudgetSheet(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    is_income = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    access_by_everyone = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=1)
    budget_sheet = models.ForeignKey(BudgetSheet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + str(self.amount) + " - " + str(self.category)
