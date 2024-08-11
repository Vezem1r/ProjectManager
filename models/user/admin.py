from django.contrib import admin

from models.user.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    """
    User model admin
    """

    list_display = ["username", "full_name", "email", "is_active", "is_staff"]
    search_fields = ["username", "full_name", "email"]
    list_filter = ["is_active", "is_staff"]
    ordering = ["-last_login"]
    readonly_fields = ["date_joined", "last_login", "full_name"]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "Personal info",
            {"fields": ("first_name", "last_name", "full_name", "email")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("username", "password1", "password2")},
        ),
    )
    filter_horizontal = ["groups", "user_permissions"]
