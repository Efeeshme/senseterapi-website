from django.contrib import admin
from .models import Branch, TeamMember, Service, SiteContact


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "whatsapp", "working_hours", "is_active", "order", "photo")
    list_filter = ("is_active",)
    search_fields = ("name", "address", "whatsapp")
    ordering = ("order", "name")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "title", "branch", "is_active", "order")
    list_filter = ("is_active", "branch")
    search_fields = ("full_name", "title", "bio")
    ordering = ("order", "full_name")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "order")
    list_filter = ("is_active",)
    search_fields = ("name", "short_description", "description")
    ordering = ("order", "name")


@admin.register(SiteContact)
class SiteContactAdmin(admin.ModelAdmin):
    list_display = ("whatsapp_number", "updated_at")

    def has_add_permission(self, request):
        return not SiteContact.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False