from django.contrib import admin
from models import UserType,News,NewType,Chat,Admin,Reply
# Register your models here.

class NewsInfoAdmin(admin.ModelAdmin):
    list_display = ('title','favor_count','reply_count')

admin.site.register(UserType)
admin.site.register(News)
admin.site.register(NewType)
admin.site.register(Chat)
admin.site.register(Admin)
admin.site.register(Reply)