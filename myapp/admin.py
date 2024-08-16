from django.contrib import admin
from .models import Audit

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('id', 'source_app', 'audited_user', 'description', 'creation_date')
    search_fields = ('source_app', 'audited_user')
