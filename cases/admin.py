from django.contrib import admin
from .models import Case, Lawyer, Client

admin.site.register(Case)
admin.site.register(Lawyer)
admin.site.register(Client)
