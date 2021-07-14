import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['profile_pic', 'member', 'address', 'user', 'city', 'state', 'country', 'zip']


class LeaseFilter(django_filters.FilterSet):
    class Meta:
        model = Lease
        fields = '__all__'
        exclude = ['member']


class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = '__all__'
