from main.models import User
from django.contrib import admin


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Custom User Admin
    """

    list_display = ("email", "first_name", "last_name", "contact_number", "is_active", "is_superuser")
    search_fields = ("email", "first_name", "last_name", "contact_number")
    list_filter = ("is_active", "is_superuser")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "contact_number")}),
        ("Permissions", {"fields": ("is_active", "is_superuser")}),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2"),
        }),
    )
    ordering = ("email",)
    filter_horizontal = ()
