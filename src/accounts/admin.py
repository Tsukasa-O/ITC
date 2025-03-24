from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    # 一覧ページ用
    list_display = (
        "email",
        "active",
        "staff",
        "admin",
    )   
    list_filter = (
        "admin",
        "active",
    )
    filter_horizontal = ()
    ordering = ("email",)
    search_fields = ("email",)
    
    # 編集ページ用
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('権限', {'fields': ('staff','admin',)}),
    )
    
    # 新規登録用
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields':('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)