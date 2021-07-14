from django.contrib import admin
from .models import Book, Lease, Member
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'qty')


class LeaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'status', 'lease_date')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'email_id', 'phone')


admin.site.register(Book, BookAdmin)
admin.site.register(Lease, LeaseAdmin)
admin.site.register(Member, MemberAdmin)