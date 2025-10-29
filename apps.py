from django.apps import AppConfig


class JazzminCustomizationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jazzmin_customizations'
    verbose_name = 'Jazzmin Customizations'
    
    def ready(self):
        """
        Patch the admin site when the app is ready to add custom sidebar functionality
        """
        from django.contrib import admin
        from .admin import custom_get_app_list
        
        # Store the original method
        original_get_app_list = admin.site.get_app_list
        
        # Replace with our custom method that wraps the original
        def patched_get_app_list(request, app_label=None):
            return custom_get_app_list(admin.site, original_get_app_list, request, app_label)
        
        admin.site.get_app_list = patched_get_app_list

