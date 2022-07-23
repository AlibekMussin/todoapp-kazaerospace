from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name']
    list_filter = ['name', ]
    readonly_fields = ['permissions']