from django.contrib import admin
from .models import Ticket


# Register your models here.
class TicektAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ticket, TicektAdmin)
