from django.contrib import admin

from .models import actor, Issue, result

# Register your models here.

admin.site.register(actor)
admin.site.register(Issue)
admin.site.register(result)
