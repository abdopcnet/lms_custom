# Website Theme Integration Guide

## ✅ Successfully Connected!

Your [custom_theme.css](lms_custom/lms_custom/public/css/custom_theme.css) has been successfully integrated with the ERPNext Website Theme!

## What Was Done:

### 1. Website Theme Updated

The **Standard** Website Theme now includes your custom colors:

-   **Primary Color**: `#6d8ba1` (--primary)
-   **Text Color**: `#0d1012` (--text)
-   **Background Color**: `#f3f5f7` (--background)
-   **Light Color**: `#a0b6c6` (--secondary)
-   **Dark Color**: `#8aa8be` (--accent)

### 2. Custom SCSS Added

All your CSS variables and theme styles have been added to the Website Theme's Custom SCSS field, including:

-   CSS variables (--text, --background, --primary, --secondary, --accent)
-   Linear and radial gradients
-   Button styles
-   Link colors
-   Heading colors

### 3. Theme Files Generated

New theme CSS file created: `/files/website_theme/standard_7906dcd9.css`

## How to Update Theme in Future:

### Option 1: Using the Script (Recommended)

```bash
cd /home/frappe/frappe-bench
./update_theme.sh
```

### Option 2: Using Bench Console

```bash
bench --site erp.local console
```

Then in the console:

```python
from lms_custom.update_theme import update_website_theme
update_website_theme()
```

### Option 3: Manual Update via UI

1. Go to: **Website → Website Theme → Standard**
2. Update colors in the **Theme Configuration** tab
3. Add/edit CSS in the **Stylesheet** tab (Custom SCSS field)
4. Save

## Files Involved:

1. **custom_theme.css**: `/home/frappe/frappe-bench/apps/lms_custom/lms_custom/public/css/custom_theme.css`

    - Your custom theme colors and variables

2. **update_theme.py**: `/home/frappe/frappe-bench/apps/lms_custom/lms_custom/update_theme.py`

    - Python script to sync colors to Website Theme

3. **hooks.py**: `/home/frappe/frappe-bench/apps/lms_custom/lms_custom/hooks.py`
    - Includes custom_theme.css in web pages

## Testing:

1. Refresh your browser (Ctrl+F5 / Cmd+Shift+R)
2. Check the Website Theme in ERPNext:
    - Go to **Website → Website Theme → Standard**
    - See colors in **Theme Configuration** tab
    - See CSS in **Stylesheet** tab (Custom SCSS field)

## Next Steps:

Your theme is now active! All changes to colors should be made in:

-   **custom_theme.css** for custom app styles
-   **Website Theme → Standard** for ERPNext theme integration

After any changes, run:

```bash
bench build --app lms_custom
bench --site erp.local clear-website-cache
```

---

**Applied Rules:** 1. General Rules & Formatting (AGENTS.md)
