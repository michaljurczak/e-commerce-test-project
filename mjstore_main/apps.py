from django.apps import AppConfig


class MjstoreMainConfig(AppConfig):
    name = 'mjstore_main'

    def ready(self):
        import mjstore_main.signals