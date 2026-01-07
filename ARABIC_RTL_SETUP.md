# Arabic RTL Setup Guide for LMS Custom

## Overview

The LMS Custom app is fully configured for Arabic Right-to-Left (RTL) display with comprehensive translations.

## Features Implemented

### 1. **Complete Arabic Translations**

-   All UI elements, buttons, and navigation items
-   About Us page content (Mission, Vision, Story, Values, Stats, Achievements)
-   Services section (Consulting, Bookkeeping, Auditing, Zakat & Tax)
-   Contact Us page
-   Newsletter subscription
-   Blog sections
-   Footer and Header components
-   Why Choose Us section
-   Hero carousel controls

### 2. **RTL Styling**

-   Automatic RTL direction detection
-   Complete CSS for RTL layout
-   Proper Arabic font rendering
-   Flipped navigation and menus
-   Responsive RTL design
-   Reversed arrows and icons
-   RTL-compatible Bootstrap components

### 3. **Automatic Language Detection**

The system automatically:

-   Detects Arabic language setting
-   Sets `dir="rtl"` on HTML element
-   Applies RTL CSS styles
-   Uses Arabic translations

## How to Enable Arabic Language

### Method 1: Set Default Language in System Settings (Recommended)

1. Login as Administrator
2. Go to: **Setup → System Settings**
3. Set **Language** field to `ar` (Arabic)
4. Save
5. Refresh your browser

### Method 2: Set Language per User

1. Go to **User Profile**
2. Edit user document
3. Set **Language** field to `ar`
4. Save
5. Logout and login again

### Method 3: Set Language for Website (Guest Users)

1. Login as Administrator
2. Go to: **Website Settings**
3. Under **Branding**, set **Language** to `ar`
4. Save
5. Clear cache: `bench --site [site_name] clear-cache`

## Verify RTL is Working

After setting the language to Arabic, you should see:

1. ✅ All text in Arabic
2. ✅ Layout flipped to RTL
3. ✅ Navigation menu on the right
4. ✅ User dropdown on the left
5. ✅ Arrows pointing in correct direction
6. ✅ Text aligned to the right
7. ✅ Proper Arabic font rendering

## Testing RTL Layout

To test the RTL layout without changing language:

```javascript
// In browser console:
document.documentElement.setAttribute('dir', 'rtl');
document.documentElement.setAttribute('lang', 'ar');
document.body.classList.add('rtl');
location.reload();
```

## Files Modified for Arabic RTL

### Translation Files:

-   `/apps/lms_custom/lms_custom/translations/ar.csv` - All Arabic translations
-   `/apps/lms/lms/translations/ar.csv` - LMS core translations

### CSS Files:

-   `/apps/lms_custom/lms_custom/public/css/rtl.css` - Complete RTL styling

### JavaScript Files:

-   `/apps/lms_custom/lms_custom/public/js/rtl_setup.js` - Automatic RTL detection

### HTML Templates Updated:

-   `header/header.html` - Navigation and user menu
-   `footer/footer.html` - Footer and newsletter
-   `about/about.html` - Complete About Us page
-   `hero_/hero_.html` - Hero carousel
-   `our_service/our_service.html` - Services section
-   `why_choose_us/why_choose_us.html` - Why Choose Us section
-   `blog_section/blog_section.html` - Blog listings
-   `contact_us_section/contact_us_section.html` - Contact information

## Troubleshooting

### Issue: Text is not in Arabic

**Solution:**

1. Check language setting in System Settings or User profile
2. Clear browser cache
3. Run: `bench --site [site_name] clear-cache`
4. Rebuild: `bench build --app lms_custom`

### Issue: Layout is not RTL

**Solution:**

1. Check browser console for JavaScript errors
2. Verify `rtl.css` is loaded
3. Verify `rtl_setup.js` is loaded
4. Check HTML element has `dir="rtl"` attribute

### Issue: Some elements still LTR

**Solution:**

1. Specific elements may need custom RTL CSS
2. Add custom rules to `/apps/lms_custom/lms_custom/public/css/rtl.css`
3. Rebuild: `bench build --app lms_custom`

### Issue: Translations not showing

**Solution:**

1. Rebuild translations: `bench build --app lms_custom`
2. Clear cache: `bench --site [site_name] clear-cache`
3. Restart bench: `bench restart`

## Build Commands

```bash
# Build lms_custom app
cd /home/frappe/frappe-bench
bench build --app lms_custom

# Clear cache
bench --site [site_name] clear-cache

# Restart bench
bench restart
```

## Browser Support

RTL layout is fully supported in:

-   ✅ Chrome/Edge (Latest)
-   ✅ Firefox (Latest)
-   ✅ Safari (Latest)
-   ✅ Mobile browsers (iOS/Android)

## Additional Configuration

### Custom RTL Styling

Add your custom RTL rules to `/apps/lms_custom/lms_custom/public/css/rtl.css`:

```css
html[lang='ar'] .your-class,
html[dir='rtl'] .your-class {
	/* Your RTL styles */
}
```

### Custom Translations

Add more translations to `/apps/lms_custom/lms_custom/translations/ar.csv`:

```csv
source,target,context
Your English Text,النص العربي الخاص بك,
```

Then rebuild:

```bash
bench build --app lms_custom
```

## Support

For issues or questions:

1. Check console for errors (F12)
2. Verify all files are properly loaded
3. Check Frappe/ERPNext logs
4. Contact support with error details

---

**Last Updated:** January 6, 2026
**Version:** 1.0
