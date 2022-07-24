from django.contrib import admin
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
    list_display = ['id', 'name']
    list_filter = ['name', ]
    readonly_fields = ['permissions']

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    search_fields = ['id', 'username', 'email', 'last_name']
    list_display = ['id', 'username', 'email', 'last_name', 'first_name', 'is_staff', 'is_active']
    list_filter = ['groups',  'is_staff',  'is_superuser', 'is_active']
    readonly_fields = ['date_joined', 'password', 'user_permissions', 'last_login']