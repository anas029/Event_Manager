from django.conf import settings


def email_settings(request):
    return {'EMAIL_SETTING': settings.EMAIL_CONFIRMATION_URI}
