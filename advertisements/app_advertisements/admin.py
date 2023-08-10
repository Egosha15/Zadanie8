from django.contrib import admin
from .models import Advertisement
from django.utils import timezone

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'create_at', 'auction', 'custom_updated_at']
    list_filter = ['auction', 'create_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description'),
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        }),
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    def custom_updated_at(self, obj):
        if obj.update_at.date() == timezone.now().date():
            return f'<span style="color: green;">Сегодня в {obj.update_at.time().strftime("%H:%M")}</span>'
        else:
            return obj.update_at
    custom_updated_at.short_description = 'Последнее обновление'
    custom_updated_at.allow_tags = True

admin.site.register(Advertisement, AdvertisementAdmin)
