from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import CustomAdminChangeForm

class UserAdmin(BaseUserAdmin):
    form = CustomAdminChangeForm
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
    
    # 編集ページ    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('プロフィール', {'fields': (
            'username',
            'department',
            'phone_number',
            'gender',
            'birthday',
        )}),
        ('Permissions', {'fields': ('staff','admin',)}),
    )

    # 新規登録
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )

admin.site.register(User, UserAdmin)
#Profileクラスは不要になったのでコメントアウト
# admin.site.register(Profile)