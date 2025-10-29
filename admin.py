"""
Custom Admin Site for Django Jazzmin
Overrides get_app_list to provide custom menu structure
"""
from django.conf import settings


def custom_get_app_list(admin_site, original_get_app_list, request, app_label=None):
    """
    Custom get_app_list function to return custom grouped menu structure
    
    Args:
        admin_site: The admin site instance (with all registered models)
        original_get_app_list: The original get_app_list method
        request: The HTTP request
        app_label: Optional app label filter
    
    Returns:
        List of app dictionaries with custom grouping
    """
    # Get the default app list from Django using the ORIGINAL admin site
    default_app_list = original_get_app_list(request, app_label)
    
    # Get custom menu configuration from settings
    custom_menu_config = getattr(settings, 'CUSTOM_ADMIN_MENU', {})
    
    # If no custom menu is configured, return default
    if not custom_menu_config:
        return default_app_list
    
    # Create a map of models to their admin info from default list
    model_map = {}
    for app in default_app_list:
        for model in app.get('models', []):
            key = f"{app['app_label']}.{model['object_name']}"
            model_map[key] = {
                'name': model.get('name'),
                'object_name': model.get('object_name'),
                'perms': model.get('perms'),
                'admin_url': model.get('admin_url'),
                'add_url': model.get('add_url'),
                'app_label': app['app_label'],
            }
    
    # Build custom app list
    custom_app_list = []
    
    for group_name, items in custom_menu_config.items():
        app_dict = {
            'name': group_name,
            'app_label': group_name.lower().replace(' ', '_'),
            'app_url': '#',
            'has_module_perms': True,
            'models': [],
        }
        
        for item in items:
            if isinstance(item, dict):
                # Custom link
                if not item.get('permissions') or _has_permissions(request, item['permissions']):
                    app_dict['models'].append({
                        'name': item.get('name', 'Link'),
                        'object_name': item.get('name', 'Link'),
                        'admin_url': item.get('url', '#'),
                        'add_url': None,
                        'perms': {'add': False, 'change': False, 'delete': False, 'view': True},
                        'custom_link': True,
                    })
            else:
                # Model reference
                if isinstance(item, str):
                    model_key = item
                else:
                    # Model class
                    model_key = f"{item._meta.app_label}.{item.__name__}"
                
                # Get model info from model_map
                if model_key in model_map:
                    model_info = model_map[model_key]
                    # Check if user has permissions to view this model
                    if model_info['perms'].get('view') or model_info['perms'].get('change'):
                        app_dict['models'].append(model_info)
        
        # Only add the group if it has models
        if app_dict['models']:
            custom_app_list.append(app_dict)
    
    # Add any apps/models that weren't included in custom menu
    included_models = set()
    for group_name, items in custom_menu_config.items():
        for item in items:
            if isinstance(item, str):
                included_models.add(item)
            elif not isinstance(item, dict):
                included_models.add(f"{item._meta.app_label}.{item.__name__}")
    
    for app in default_app_list:
        remaining_models = []
        for model in app.get('models', []):
            model_key = f"{app['app_label']}.{model['object_name']}"
            if model_key not in included_models:
                remaining_models.append(model)
        
        if remaining_models:
            custom_app_list.append({
                'name': app['name'],
                'app_label': app['app_label'],
                'app_url': app.get('app_url', '#'),
                'has_module_perms': app.get('has_module_perms', True),
                'models': remaining_models,
            })
    
    return custom_app_list


def _has_permissions(request, permissions):
    """
    Check if user has any of the specified permissions
    """
    if not permissions:
        return True
    
    for perm in permissions:
        if request.user.has_perm(perm):
            return True
    
    return False

