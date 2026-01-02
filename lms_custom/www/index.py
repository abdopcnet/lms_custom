import frappe


def get_context(context):
    """Homepage context - fetches data for main template"""

    # Get top 6 categories maximum
    categories = frappe.get_all(
        'LMS Category',
        fields=['name', 'category'],
        order_by='category asc',
        limit=6
    )

    # Check if a category filter is selected
    selected_category = frappe.form_dict.get('category')

    # Build course filters
    course_filters = {
        'published': 1,
        'status': 'Approved'
    }

    # Add category filter if selected
    if selected_category:
        course_filters['category'] = selected_category
        context.selected_category = selected_category

    # Get popular courses (published, featured, or most enrollments)
    courses = frappe.get_all(
        'LMS Course',
        filters=course_filters,
        fields=[
            'name',
            'title',
            'short_introduction',
            'image',
            'category',
            'tags',
            'enrollments',
            'rating'
        ],
        order_by='enrollments desc, rating desc',
        limit=3
    )

    # Process courses to add additional info
    for course in courses:
        # Get instructor name
        instructors = frappe.get_all(
            'Course Instructor',
            filters={'parent': course.name},
            fields=['instructor'],
            limit=1
        )
        course['instructor'] = instructors[0].instructor if instructors else 'Unknown'

        # Count lessons
        lesson_count = frappe.db.count(
            'Course Lesson',
            filters={'course': course.name}
        )
        course['lesson_count'] = lesson_count

        # Set default image if none
        if not course.get('image'):
            course['image'] = '/assets/lms_custom/img/placeholder.jpg'

        # Set icon color based on index
        colors = ['blue', 'orange', 'sky', 'pink']
        course['icon_color'] = colors[courses.index(course) % len(colors)]

        # Set default icon
        icons = ['icon-code-solid', 'icon-css3', 'icon-sitemap-solid']
        course['icon'] = icons[courses.index(course) % len(icons)]

        # Format price (assuming basic pricing)
        course['price'] = '$120 all course / $20 per month'

    context.categories = categories
    context.courses = courses
    context.no_cache = 1
    
    # Debug logging
    frappe.log_error(f"[index.py] method: get_context - Categories: {len(categories)}, Courses: {len(courses)}", "Homepage Context")

    return context
