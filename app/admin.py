from django.contrib import admin
from .models import ClickTransactionPR


@admin.register(ClickTransactionPR)
class ClickTransactionAdminPR(admin.ModelAdmin):
    list_display = ('id', 'click_paydoc_id', 'amount', 'status',)
    list_display_links = ('id', 'amount')
    list_filter = ('status',)
    search_fields = ['status', 'id', 'click_paydoc_id']
    save_on_top = True
