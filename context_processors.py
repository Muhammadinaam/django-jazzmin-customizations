"""
Context processor to make RTL_LANGUAGES available in templates
"""
from django.conf import settings


def rtl_languages(request):
    """
    Make RTL_LANGUAGES setting available in all templates.
    This is used by the admin template to detect RTL languages.
    
    Usage in templates:
        {% if LANGUAGE_CODE in RTL_LANGUAGES %}
            <!-- RTL content -->
        {% endif %}
    """
    return {
        'RTL_LANGUAGES': getattr(settings, 'RTL_LANGUAGES', []),
    }

