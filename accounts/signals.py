from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Member
from django.contrib.auth.models import Group


def member_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='member')
        instance.groups.add(group)
        Member.objects.create(
            user=instance,
            name=instance.first_name,
            email_id=instance.email,
            )


post_save.connect(member_profile, sender=User)