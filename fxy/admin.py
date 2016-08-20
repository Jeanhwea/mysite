from django.contrib import admin

# Register your models here.

from .models import Member, Person, Group, Membership

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    fields = [
        'first_name',
        'last_name',
        'birth_date',
    ]
    list_display = (
        'full_name',
        'first_name',
        'last_name',
        'birth_date',
    )

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

