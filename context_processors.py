"""
Context processors for Jazzmin customizations
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


def jazzmin_custom_assets(request):
    """
    Support for multiple custom CSS and JS files in Jazzmin.
    
    Settings:
        JAZZMIN_CUSTOM_CSS = [
            'path/to/file1.css',
            'path/to/file2.css',
        ]
        
        JAZZMIN_CUSTOM_JS = [
            'path/to/file1.js',
            'path/to/file2.js',
        ]
    
    Backward compatible with Jazzmin's single file approach:
        JAZZMIN_SETTINGS = {
            'custom_css': 'path/to/file.css',
            'custom_js': 'path/to/file.js',
        }
    """
    custom_css = []
    custom_js = []
    
    # Check for new array-based settings first
    if hasattr(settings, 'JAZZMIN_CUSTOM_CSS'):
        css_setting = settings.JAZZMIN_CUSTOM_CSS
        if isinstance(css_setting, list):
            custom_css = css_setting
        elif isinstance(css_setting, str):
            custom_css = [css_setting]
    
    if hasattr(settings, 'JAZZMIN_CUSTOM_JS'):
        js_setting = settings.JAZZMIN_CUSTOM_JS
        if isinstance(js_setting, list):
            custom_js = js_setting
        elif isinstance(js_setting, str):
            custom_js = [js_setting]
    
    # Fallback to standard Jazzmin settings if arrays not provided
    if not custom_css:
        jazzmin_settings = getattr(settings, 'JAZZMIN_SETTINGS', {})
        if 'custom_css' in jazzmin_settings:
            custom_css = [jazzmin_settings['custom_css']]
    
    if not custom_js:
        jazzmin_settings = getattr(settings, 'JAZZMIN_SETTINGS', {})
        if 'custom_js' in jazzmin_settings:
            custom_js = [jazzmin_settings['custom_js']]
    
    return {
        'JAZZMIN_CUSTOM_CSS_FILES': custom_css,
        'JAZZMIN_CUSTOM_JS_FILES': custom_js,
    }

