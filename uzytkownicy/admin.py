from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("imie", "nazwisko", "adres", "email", "numer_telefonu", "detektyw", "admin", "is_staff", "is_active", "last_login", )
    # fieldsets = ()
    # list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("imie", "nazwisko", "adres", "email", "numer_telefonu", "inne", "detektyw", "admin")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("imie", "nazwisko", "adres", "email", "numer_telefonu", "inne", "detektyw", "admin", "password1", "password2")}
        ),
    )
    # search_fields = ("email",)
    ordering = ("email",)
    # show_change_link = True


admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(CustomUser)