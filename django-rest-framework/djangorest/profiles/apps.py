from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    name = 'profiles'
    # verbose_name = _('profiles')

    def ready(self):
        import profiles.signals  # noqa

