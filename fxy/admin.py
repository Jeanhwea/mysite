from django.contrib import admin

# Register your models here.

from .models import Person, Group, Membership

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'shirt_size',
    ]
    list_display = (
        'name',
        'shirt_size',
    )

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = [
        'name',
    ]
    list_display = (
        'name',
    )

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    fields = [
        'person',
        'group',
        'joined_at',
        'invite_reason',
    ]
    list_display = (
        'person',
        'group',
        'joined_at',
    )
