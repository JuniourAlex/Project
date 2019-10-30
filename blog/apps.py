from django.apps import AppConfig


class WebAppConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals
