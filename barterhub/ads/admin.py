from django.contrib import admin
from .models import Ad, ExchangeProposal

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "condition", "user", "created_at")
    search_fields = ("title", "description")
    list_filter = ("category", "condition")

@admin.register(ExchangeProposal)
class ExchangeProposalAdmin(admin.ModelAdmin):
    list_display = ("ad_sender", "ad_receiver", "status", "created_at")
    search_fields = ("comment",)
    list_filter = ("status",)