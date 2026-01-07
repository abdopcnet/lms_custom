# How to Update Hero Slideshow Content in Arabic

## Overview

The hero section slideshow content (heading and description text) is stored in the **Website Slideshow** DocType in the Frappe database. To change the English text to Arabic, you need to edit this content through the Desk interface.

## Step-by-Step Guide

### 1. Login to Frappe Desk

1. Open your browser and go to your site URL
2. Login with your administrator credentials
3. You'll see the Frappe Desk interface

### 2. Navigate to Website Slideshow

**Option A: Using Awesome Bar (Quick Search)**

1. Press `Ctrl + K` (or `Cmd + K` on Mac) to open the Awesome Bar
2. Type "Website Slideshow"
3. Click on "Website Slideshow" from the results

**Option B: Using Menu**

1. Click on the search icon in the top navigation
2. Type "Website Slideshow"
3. Click on "Website Slideshow" DocType

### 3. Open the Hero Section Slideshow

1. You'll see a list of website slideshows
2. Find and click on **"Hero Section"**
3. This will open the slideshow editing form

### 4. Update Slide Content to Arabic

For each slide in the slideshow:

#### Slide 1 Example (Current English):

```
Heading: Trusted Accounting & Tax Services
Description: At Ibrahim Al-Salmi, Certified Public Accountants, we provide exceptional accounting, auditing, and tax services tailored to your specific financial needs...
```

#### Change to Arabic:

```
Heading: خدمات محاسبة وضرائب موثوقة
Description: في إبراهيم السلمي، محاسبون قانونيون معتمدون، نقدم خدمات محاسبة ومراجعة وضرائب استثنائية مصممة خصيصًا لتلبية احتياجاتك المالية...
```

### 5. Edit Each Slide

1. In the "Slideshow Items" table, click on each row to edit
2. Update the following fields:
    - **Heading**: Replace English text with Arabic heading
    - **Description**: Replace English text with Arabic description
    - **URL**: Keep as is (e.g., "/courses" or your custom link)
    - **Image**: Keep the current image or upload new one

### 6. Save Changes

1. After editing all slides, click the **"Save"** button at the top
2. The system will save your changes to the database

### 7. Clear Cache and View Changes

1. To see changes immediately, clear the website cache:
    ```bash
    cd /home/frappe/frappe-bench
    bench --site [your-site-name] clear-cache
    ```
2. Or click the "Clear Cache" button in Desk
3. Refresh your website homepage to see the Arabic content

## Sample Arabic Content for Hero Slides

### Slide 1: Accounting Services

```
Heading: خدمات محاسبة وضرائب موثوقة
Description: في إبراهيم السلمي، محاسبون قانونيون معتمدون، نقدم خدمات محاسبة ومراجعة وضرائب استثنائية مصممة خصيصًا لتلبية احتياجاتك المالية. معترف بنا كواحدة من شركات المراجعة والمحاسبة الرائدة في المملكة.
URL: /courses
```

### Slide 2: Professional Consulting

```
Heading: استشارات مهنية متخصصة
Description: نوفر خدمات استشارات أعمال احترافية لمساعدتك على اتخاذ قرارات استراتيجية مستنيرة وتحقيق أهدافك. فريقنا من الخبراء المعتمدين جاهز لخدمتك.
URL: /about
```

### Slide 3: Expert Team

```
Heading: فريق من الخبراء المعتمدين
Description: فريقنا من المحاسبين القانونيين المعتمدين والمستشارين الماليين ذوي الخبرة يضمن أعلى مستويات الجودة والاحترافية في جميع خدماتنا.
URL: /team
```

## Important Notes

### Language Detection

-   The website automatically detects the user's language preference
-   If the site language is set to Arabic (`ar`), all **translated strings** will show in Arabic
-   However, **database content** (like slideshow text) must be manually entered in Arabic

### Translation vs Database Content

-   **Translated Strings**: Buttons, labels, navigation (handled by translation system)
    -   Example: "Learn More" button → automatically shows "تعلم المزيد"
-   **Database Content**: Slideshow headings, descriptions (stored in database)
    -   Example: Slideshow heading → must be manually updated to Arabic

### RTL (Right-to-Left) Layout

-   The RTL CSS automatically handles text alignment
-   Arabic content will be properly aligned from right to left
-   No additional configuration needed once content is in Arabic

## Troubleshooting

### Content Still Shows English

1. **Problem**: Updated content but still seeing English

    - **Solution**: Clear browser cache and website cache

    ```bash
    bench --site [site-name] clear-cache
    bench --site [site-name] clear-website-cache
    ```

2. **Problem**: Text alignment is wrong

    - **Solution**: Make sure `rtl.css` is loaded and language is set to `ar`
    - Check browser's language preference

3. **Problem**: Changes not saving
    - **Solution**: Check user permissions (need Website Manager role)
    - Try refreshing the form and saving again

### Multiple Language Support

If you want to support both English and Arabic:

**Option 1: Duplicate Slideshows**

1. Create two slideshows: "Hero Section EN" and "Hero Section AR"
2. Modify the template to load based on language
3. Use conditional logic in the template

**Option 2: Use Description Field for Both**

1. Store both languages in the description
2. Parse and display based on user's language preference
3. Requires custom code modification

## Quick Command Reference

```bash
# Clear all cache
bench --site [site-name] clear-cache

# Clear website cache only
bench --site [site-name] clear-website-cache

# Rebuild website assets
bench build --app lms_custom

# Restart bench
bench restart
```

## Additional Resources

-   Frappe Documentation: https://frappeframework.com/docs
-   Website Slideshow DocType: Located in Frappe Core → Website
-   Translation Guide: See `ARABIC_RTL_SETUP.md` in this directory

---

**Applied Rules:** 1. General Rules & Formatting (AGENTS.md) 2. DocType Search Instructions (AGENTS.md) 3. Database Info Instructions (AGENTS.md)
