# Jazzmin Customizations 🎨

**The ultimate plug-and-play Django app for Jazzmin admin theme**

A comprehensive, reusable app that supercharges your Django Jazzmin admin with:
- ✅ **RTL Support** - Perfect layout for Arabic, Urdu, Hebrew, Persian
- ✅ **Sidebar Search** - Real-time search functionality  
- ✅ **Custom Menus** - Organize models into custom categories
- ✅ **Zero Configuration** - Works out of the box!

---

## 🚀 Quick Install (4 Steps)

### 1. Install the App

Install directly from GitHub:

```bash
pip install git+https://github.com/Muhammadinaam/django-jazzmin-customizations.git
```

Or if you have the source code, copy the `jazzmin_customizations` folder to your project

### 2. Add to INSTALLED_APPS

In your `settings.py`, add the app **before** your main app:

```python
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    # ... other Django apps ...
    'jazzmin_customizations',  # Add this!
    'apps.main',                # Your main app
]
```

### 3. Configure Templates

Add the context processor to your `TEMPLATES['OPTIONS']`:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,  # This will automatically find templates in installed apps
        'OPTIONS': {
            'context_processors': [
                # ... Django defaults ...
                'jazzmin_customizations.context_processors.rtl_languages',  # For RTL
            ],
        },
    },
]
```

### 4. Configure Jazzmin Settings

Update your Jazzmin settings:

```python
JAZZMIN_SETTINGS = {
    # ... your other settings ...
    
    # Enable sidebar search and RTL CSS
    "custom_css": "jazzmin_custom_sidebar/sidebar_search.css",
    "custom_js": "jazzmin_custom_sidebar/sidebar_search.js",
    
    # Enable language chooser (optional)
    "language_chooser": True,
}

# Define RTL languages
RTL_LANGUAGES = ['ar', 'ur', 'fa', 'he']  # Arabic, Urdu, Persian, Hebrew

# Define custom admin menu (optional)
CUSTOM_ADMIN_MENU = {
    'User Management': [
        'auth.User',
        'auth.Group',
    ],
    'Your App': [
        'main.YourModel',
        'main.AnotherModel',
    ],
}
```

### 4. Collect Static Files & Restart

```bash
python manage.py collectstatic
python manage.py runserver
```

**Done! 🎉** Visit your admin panel to see:
- Searchable sidebar
- Custom menu organization
- Perfect RTL layout (when using RTL languages)

---

## Features

### 🌍 RTL Support

**Automatic RTL layout detection for:**
- Arabic (العربية)
- Urdu (اردو)
- Persian (فارسی)
- Hebrew (עברית)

**Includes:**
- ✅ 755 lines of AdminLTE RTL CSS fixes
- ✅ Sidebar positioning (right side)
- ✅ Content flow (right-to-left)
- ✅ Form alignment
- ✅ Table layout
- ✅ Buttons and dropdowns
- ✅ All UI elements

**How it works:**
1. User switches to RTL language in admin
2. App detects language via `RTL_LANGUAGES` setting
3. Custom CSS loads automatically
4. `dir="rtl"` attribute set on HTML
5. Perfect RTL layout! 🎉

---

### 🔍 Sidebar Search

**Real-time sidebar search functionality:**
- Type to filter menu items instantly
- Searches across all categories
- Clean, modern UI
- Shows/hides items as you type

**How it works:**
1. Search box appears at top of sidebar
2. User types query
3. JavaScript filters menu items in real-time
4. Only matching items shown

---

### 📋 Custom Menu Organization

**Organize your admin models into custom categories:**

```python
CUSTOM_ADMIN_MENU = {
    'User Management': [
        'auth.User',
        'auth.Group',
    ],
    'HR & Profiles': [
        'main.Profile',
        'main.WorkExperience',
        'main.Education',
    ],
    'Jobs': [
        'main.Job',
        'main.Company',
        'main.Application',
    ],
    'Tools': [
        {
            'name': 'Resume Builder',
            'url': '/resumes/',
            'icon': 'fas fa-file-alt',
            'permissions': ['main.view_profile']
        },
        {
            'name': 'Reports',
            'url': '/admin/reports/',
            'icon': 'fas fa-chart-bar',
        }
    ]
}
```

**Features:**
- Group models by category
- Custom links with icons
- Permission-based visibility
- Clean, organized sidebar

---

## Configuration Options

### RTL Languages

Define which languages trigger RTL mode:

```python
RTL_LANGUAGES = [
    'ar',  # Arabic
    'ur',  # Urdu
    'fa',  # Persian/Farsi
    'he',  # Hebrew
]
```

### Custom Menu Structure

```python
CUSTOM_ADMIN_MENU = {
    'Category Name': [
        'app.Model',  # Model as string
        {
            'name': 'Custom Link',  # Custom link with options
            'url': '/path/',
            'icon': 'fas fa-icon',
            'permissions': ['app.permission_codename'],  # Optional
        }
    ]
}
```

### Jazzmin Settings

```python
JAZZMIN_SETTINGS = {
    # ... other settings ...
    
    # Required for this app
    "custom_css": "jazzmin_custom_sidebar/sidebar_search.css",
    "custom_js": "jazzmin_custom_sidebar/sidebar_search.js",
    
    # Optional but recommended
    "language_chooser": True,  # Show language selector
    "show_version": False,     # Hide Django version
}
```

---

## File Structure

```
jazzmin_customizations/
├── __init__.py
├── apps.py                                    # App configuration
├── admin.py                                   # Custom menu logic
├── context_processors.py                      # RTL context processor
├── README.md                                  # This file
├── static/
│   ├── admin/
│   │   └── css/
│   │       └── rtl_admin.css                 # RTL fixes (755 lines!)
│   └── jazzmin_custom_sidebar/
│       ├── sidebar_search.css                # Search styling
│       └── sidebar_search.js                 # Search functionality
└── templates/
    └── admin/
        └── base_site.html                    # Custom admin template
```

---

## How It Works

### RTL Detection Flow

```
1. User visits admin
2. User switches to Arabic/Urdu
3. Template checks: {% if LANGUAGE_CODE in RTL_LANGUAGES %}
4. Yes? → Load rtl_admin.css
5. Set dir="rtl" on HTML element
6. Admin displays perfectly in RTL!
```

### Sidebar Search Flow

```
1. Admin loads
2. JavaScript adds search box
3. User types in search box
4. JavaScript filters menu items
5. Only matching items displayed
```

### Custom Menu Flow

```
1. Django loads admin
2. App patches admin.site.get_app_list()
3. Custom logic reads CUSTOM_ADMIN_MENU setting
4. Reorganizes models into categories
5. Sidebar displays custom structure
```

---

## Requirements

```bash
pip install django-jazzmin
```

**Compatible with:**
- Django 3.2, 4.0, 4.1, 4.2, 5.0+
- Python 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
- Jazzmin (all versions)

---

## Usage Examples

### Example 1: Basic Setup

```python
# settings.py
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'jazzmin_customizations',
]

TEMPLATES = [{
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            # ... defaults ...
            'jazzmin_customizations.context_processors.rtl_languages',
        ],
    },
}]

JAZZMIN_SETTINGS = {
    "custom_css": "jazzmin_custom_sidebar/sidebar_search.css",
    "custom_js": "jazzmin_custom_sidebar/sidebar_search.js",
}

RTL_LANGUAGES = ['ar', 'ur']
```

### Example 2: With Custom Menu

```python
CUSTOM_ADMIN_MENU = {
    'Users': ['auth.User', 'auth.Group'],
    'Content': ['blog.Post', 'blog.Category'],
}
```

### Example 3: Full Multilingual Project

```python
LANGUAGES = [
    ('en', 'English'),
    ('es', 'Español'),
    ('ar', 'العربية'),
]

RTL_LANGUAGES = ['ar']

MIDDLEWARE = [
    # ... defaults ...
    'django.middleware.locale.LocaleMiddleware',
]

JAZZMIN_SETTINGS = {
    "language_chooser": True,
    "custom_css": "jazzmin_custom_sidebar/sidebar_search.css",
    "custom_js": "jazzmin_custom_sidebar/sidebar_search.js",
}
```

---

## Troubleshooting

### RTL CSS Not Loading

**Check 1:** Is app in `INSTALLED_APPS`?
```python
INSTALLED_APPS = ['jazzmin_customizations']
```

**Check 2:** Is `APP_DIRS` enabled?
```python
TEMPLATES = [{
    'APP_DIRS': True,
}]
```

**Check 3:** Is `RTL_LANGUAGES` defined?
```python
RTL_LANGUAGES = ['ar', 'ur']
```

**Check 4:** Did you restart server?

### Sidebar Search Not Working

**Check 1:** Are CSS and JS loaded?
```python
JAZZMIN_SETTINGS = {
    "custom_css": "jazzmin_custom_sidebar/sidebar_search.css",
    "custom_js": "jazzmin_custom_sidebar/sidebar_search.js",
}
```

**Check 2:** Did you collect static files?
```bash
python manage.py collectstatic
```

**Check 3:** Check browser console for errors

### Custom Menu Not Showing

**Check 1:** Is `CUSTOM_ADMIN_MENU` defined in settings?

**Check 2:** Are model strings correct? Format: `'app_label.ModelName'`

**Check 3:** Did you restart server?

### Layout Still Broken (RTL)

- Clear browser cache (Ctrl+Shift+R)
- Check browser console for CSS loading errors
- Verify you're on an RTL language URL
- Inspect HTML for `dir="rtl"` attribute

---

## Customization

### Adding More RTL Languages

Just update `settings.py`:

```python
RTL_LANGUAGES = [
    'ar',  # Arabic
    'ur',  # Urdu
    'fa',  # Persian
    'he',  # Hebrew
    'yi',  # Yiddish
]
```

### Customizing RTL CSS

Edit `static/admin/css/rtl_admin.css` to tweak RTL styles.

### Customizing Search Box Styling

Edit `static/jazzmin_custom_sidebar/sidebar_search.css`.

### Customizing Search Behavior

Edit `static/jazzmin_custom_sidebar/sidebar_search.js`.

---

## Use in Other Projects

**This app is completely self-contained!**

```bash
# Install in any Django project
pip install git+https://github.com/Muhammadinaam/django-jazzmin-customizations.git

# Or install a specific version
pip install git+https://github.com/Muhammadinaam/django-jazzmin-customizations.git@v1.0.0
```

Then follow the Quick Install steps above. That's it! 🎉

---

## Why Use This App?

### ✅ All-in-One
- RTL support + Sidebar search + Custom menus
- One app to manage all Jazzmin customizations

### ✅ Plug-and-Play
- Copy folder → Update settings → Done!
- No complex configuration

### ✅ Production-Ready
- 755 lines of tested RTL CSS
- Used in real projects
- Zero dependencies (except Jazzmin)

### ✅ Maintainable
- All customizations in one place
- Clean, documented code
- Easy to update

### ✅ Reusable
- Copy to any Django project
- Works with any Jazzmin setup
- No project-specific code

---

## Credits

- RTL CSS based on [AdminLTE RTL](https://github.com/rtlcss/rtlcss) by SajjadMoosavi
- Sidebar search: Custom implementation
- Custom menu: Custom implementation

---

## License

Free to use in your projects! MIT License

---

## What's Included?

| Feature | Description | Lines of Code |
|---------|-------------|---------------|
| RTL CSS | Complete AdminLTE RTL fixes | 755 |
| Sidebar Search | Real-time filtering | ~100 |
| Custom Menu | Model organization | ~150 |
| Admin Template | Base site override | ~20 |
| Context Processor | RTL detection | ~20 |
| **Total** | Complete Jazzmin enhancement | **~1,045** |

---

## Testing Checklist

After installation, verify:

- [ ] Admin loads without errors
- [ ] Sidebar search box appears
- [ ] Search filters menu items
- [ ] Custom menu categories show (if configured)
- [ ] Switch to RTL language (Arabic/Urdu)
- [ ] Admin sidebar moves to right side
- [ ] Content flows right-to-left
- [ ] Forms and tables aligned correctly
- [ ] Switch back to LTR language (English)
- [ ] Layout returns to normal

---

## Development Workflow 🔧

### For Package Maintainers

If you want to modify or extend this app:

**1. Local Development (Recommended)**
- Keep the app in your Django project root (e.g., `backend/jazzmin_customizations/`)
- Develop and test as a normal Django app
- Use `'jazzmin_customizations'` in INSTALLED_APPS
- Import paths are identical to pip-installed version ✨

**2. Publishing Updates**
```bash
# Make changes, test locally
cd jazzmin_customizations/

# Commit to git
git add .
git commit -m "Add new feature"
git push origin main

# Release new version
git tag -a v1.1.0 -m "Version 1.1.0"
git push origin v1.1.0
```

**3. Installing in Other Projects**
```bash
# Install from GitHub
pip install git+https://github.com/Muhammadinaam/django-jazzmin-customizations.git@v1.1.0

# Use without 'apps.' prefix
INSTALLED_APPS = ['jazzmin_customizations']
```

**4. Editable Installation (Advanced)**
```bash
# For active cross-project development
pip install -e /path/to/jazzmin_customizations
```

### Version Management
- **1.0.x** → Bug fixes (patch)
- **1.x.0** → New features (minor)  
- **x.0.0** → Breaking changes (major)

---

**Made with ❤️ for the Django community**

**Need help?** Check the troubleshooting section above or review your settings configuration.

🚀 **Happy coding!**

