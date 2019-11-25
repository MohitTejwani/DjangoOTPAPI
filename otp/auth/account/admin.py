from django.contrib import admin
from django.contrib.auth import get_user_model
User=get_user_model()
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import AbstractUser
from .models import PhoneoTP
admin.site.register(PhoneoTP)
# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form = UserCreationForm
    list_display=('phone',)
    ordering = ()
    list_filter=()
    fieldsets=(
        (None,{'fields':('phone','password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
       
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('phone','password')}
            ),
    )
    filter_horizontal=()
    def get_inline_instances(self,required,obj=None):
        if not obj:
            return list()
        return super(UserAdmin,self).get_inline_instances(required,obj)
admin.site.register(User,UserAdmin)

admin.site.unregister(Group)