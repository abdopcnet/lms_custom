import frappe

def get_context(context):
	"""Fetch popular courses data with proper permissions for guest users"""
	# Frontend logging: console.log('[popular_courses.py] method: get_context')
	
	# Get popular categories - using raw SQL with explicit permission bypass
	popular_categories = frappe.db.sql("""
		SELECT c.category, COUNT(c.name) as course_count
		FROM `tabLMS Course` c
		WHERE c.published = 1
		AND c.category IS NOT NULL
		AND c.category != ''
		GROUP BY c.category
		ORDER BY course_count DESC
		LIMIT 6
	""", as_dict=True)
	
	# Get popular courses with explicit permission bypass for guest users
	popular_courses = frappe.get_all(
		'LMS Course',
		filters={'published': 1},
		fields=[
			'name', 'title', 'short_introduction', 'image', 'category',
			'enrollments', 'rating', 'lessons', 'course_price', 'currency',
			'paid_course', 'card_gradient'
		],
		order_by='enrollments desc',
		limit=3,
		ignore_permissions=True
	)
	
	# Enrich courses with instructor information
	for course in popular_courses:
		instructor_email = frappe.db.get_value(
			'Course Instructor',
			{'parent': course.name, 'parenttype': 'LMS Course'},
			'instructor'
		)
		course['instructor_name'] = frappe.db.get_value(
			'User', instructor_email, 'full_name'
		) if instructor_email else 'Unknown'
		course['rating_filled'] = int(course.get('rating') or 0)
		course['rating_empty'] = 5 - course['rating_filled']
	
	context.popular_categories = popular_categories
	context.popular_courses = popular_courses
	
	return context
