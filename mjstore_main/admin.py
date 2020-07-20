from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(
    [
        models.Category,
        models.Product,
        models.Customer,
        models.Order,
    ]
)