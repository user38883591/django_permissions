from django.apps import AppConfig
from django.conf import settings


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Authentication'

    def ready (self):
        from django.contrib.auth.models import Group
        from django.db.models.signals import post_save

        def add_to_default_group(sender,**kwargs):
            User = kwargs ["instance"]
            if kwargs['instance']:
                group,ok =Group.objects.create_or_get(name="default")
                group.user_set.add(User)

        post_save.connect(add_to_default_group,sender=settings.AUTH_USER_MODEL)
