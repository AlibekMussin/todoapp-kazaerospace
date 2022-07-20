from django.contrib import admin

from todoapp.apps.cardlist.models import Card, CardExecutor

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    search_fields = ['id', 'subject', 'description']
    list_display = ['id', 'subject', 'description', 'status', 'created_by_user', 'created_at']
    list_filter = ['status', ]
    readonly_fields = ['created_at',
                       'created_by_user',
                       'updated_by_user',
                       'deleted_by_user',
                       'deleted_at']

@admin.register(CardExecutor)
class CardExecutorAdmin(admin.ModelAdmin):
    search_fields = ['id', 'card__id']
    list_display = ['id', 'card', 'executor', 'created_by_user', 'created_at']
    list_filter = ['card__status', ]
    autocomplete_fields = ['card', 'executor']
    readonly_fields = ['created_at',
                       'created_by_user',
                       'updated_by_user',
                       'deleted_by_user',
                       'deleted_at']
