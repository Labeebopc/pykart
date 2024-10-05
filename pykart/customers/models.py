from django.db import models
from django.contrib.auth.models import User

# Signup models

class Customer(models.Model):
    # To move into trash
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, "Delete"))

    name = models.CharField(max_length = 200)
    address = models.TextField()
    user = models.OneToOneField(User, on_delete = models.CASCADE , related_name = 'customer_profile')
    phone = models.CharField(max_length = 10)
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # __str__ , string reprecentation
    def __str__(self) -> str:
        return self.title