from django.apps import apps
from easy_login.forms import EasyLoginForm
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.template import TemplateSyntaxError
from django.core.exceptions import ImproperlyConfigured


def easy_login(request):
    context = {}
    context.update(csrf(request))
    context['form'] = EasyLoginForm()
    context['current_user'] = request.user

    try:
        render_page = render_to_string("base.html", context)

    except TemplateSyntaxError:
        if not apps.is_installed("django.contrib.staticfiles"):
            raise ImproperlyConfigured(
                "The easy-login requires the staticfiles contrib app. "
                "Add 'django.contrib.staticfiles' to INSTALLED_APPS and "
                "define STATIC_URL in your settings."
            )
        else:
            raise

    return {"easy_login": render_page}
