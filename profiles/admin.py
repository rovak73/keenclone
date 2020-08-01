from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

# Register your models here.

admin.site.register(Profile)

# class UserProfile(admin,ModelAdmin):
    # fieldsets = (
    #     (None, {'fields': ('email', 'password', 'name', 'last_login')}),
    #     ('Permissions', {'fields': (
    #         'is_active', 
    #         'is_staff', 
    #         'is_superuser',
    #         'is_banned',
    #         'is_listed',
    #         'groups', 
    #         'user_permissions',
    #     )}),
    # )
    # add_fieldsets = (
    #     (
    #         None,
    #         {
    #             'classes': ('wide',),
    #             'fields': ('email', 'password1', 'password2')
    #         }
    #     ),
    # )

    # list_display = ('email', 'name')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_banned', 'is_listed', 'groups')
#     search_fields = ('email', 'name')
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)


# admin.site.register(UserProfile)