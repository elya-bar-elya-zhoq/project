from django.contrib import admin
from .models import Suggestion, Comment

# adding Suggestions and their Comments to admin site
admin.site.register(Suggestion)
admin.site.register(Comment)