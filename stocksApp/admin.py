from django.contrib import admin
from .models import Stock, Bond, Investor

# Register your models here.
admin.site.register(Stock)
admin.site.register(Bond)
admin.site.register(Investor)