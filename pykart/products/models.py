from django.db import models

# Model for product

class Product(models.Model):
    # To move into trash
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = ((LIVE, 'Live'), (DELETE, "Delete"))

    title = models.CharField(max_length = 200)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/')
    priority = models.IntegerField(default = 0)
    delete_status = models.IntegerField(choices = DELETE_CHOICES, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    # __str__ , string reprecentation
    def __str__(self) -> str:
        return self.title
