# Hero Slideshow Setup Guide for Arabic

## How to Add Arabic Text to Hero Slideshow

The hero section displays content from the **Website Slideshow** DocType. To add Arabic content:

### Steps:

1. **Login as Administrator**

2. **Go to Website Slideshow**

    - Search for "Website Slideshow" in the search bar
    - Or navigate: Setup → Website → Website Slideshow

3. **Open "Hero Section" Slideshow**

    - Find and open the slideshow named "Hero Section"

4. **Edit Slides**

    - Each slide has these fields:
        - **Image**: Upload your slide background image
        - **Heading**: Main title (shows in large white text)
        - **Description**: Subtitle/description text
        - **URL**: Optional link for "Learn More" button

5. **Add Arabic Content**

    - In the **Heading** field, enter Arabic text like:

        ```
        خدمات محاسبة وضرائب موثوقة
        ```

    - In the **Description** field, enter Arabic text like:
        ```
        خدمات تقارير مالية محترفة، والامتثال الضريبي، والاستشارات التجارية مصممة لمساعدة عملك على الازدهار في سوق المملكة العربية السعودية الديناميكي
        ```

6. **Save Changes**
    - Click Save
    - Refresh your website homepage to see changes

### Example Arabic Slideshow Content:

**Slide 1:**

-   **Heading**: `خدمات محاسبة وضرائب موثوقة`
-   **Description**: `خدمات تقارير مالية محترفة، والامتثال الضريبي، والاستشارات التجارية مصممة لمساعدة عملك على الازدهار في سوق المملكة العربية السعودية الديناميكي`

**Slide 2:**

-   **Heading**: `خدمات استشارية مالية متميزة`
-   **Description**: `نساعدك في اتخاذ القرارات المالية الصحيحة من خلال فريق من الخبراء المعتمدين`

**Slide 3:**

-   **Heading**: `شريكك الموثوق في النجاح المالي`
-   **Description**: `نقدم حلولاً مالية متكاملة تلبي احتياجات عملك وتضمن نموه المستدام`

### Current Slide Content:

From the screenshot, the current slide shows:

-   **Heading**: "Trusted Accounting & Tax Services"
-   **Description**: "Professional financial reporting, tax compliance, and business advisory services designed to help your business thrive in Saudi Arabia's dynamic market."

These need to be replaced with Arabic text in the Website Slideshow settings.

### Buttons:

The buttons are already translated:

-   "عرض الدورات" (View Courses) ✓
-   "تعلم المزيد" (Learn More) ✓

### Arrow Styling:

✅ **FIXED** - Arrows now use theme colors:

-   Default: White/transparent background
-   Hover: Theme primary color (blue)
-   Indicators: Active dot shows theme primary color

### Clearing Cache:

After updating the slideshow:

```bash
bench --site [your-site] clear-cache
```

Or from UI: Go to → **Tools → Clear Cache**

---

**Note:** The slideshow content is **managed by administrators** through the Website Slideshow DocType. This allows non-technical users to update hero content without touching code.
