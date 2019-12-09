from django.contrib import admin
from .models import Suggestion, Comment, News

# adding Suggestions and their Comments to admin site
admin.site.register(Suggestion)
admin.site.register(Comment)
admin.site.register(News)