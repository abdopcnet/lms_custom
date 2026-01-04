import frappe

def get_context(context):
	"""Fetch footer data with proper permissions for guest users"""
	# Frontend logging: console.log('[footer.py] method: get_context')
	
	# Get popular courses for footer - bypass permissions for guest users
	footer_courses = frappe.get_all(
		'LMS Course',
		filters={'published': 1},
		fields=['name', 'title'],
		order_by='enrollments desc',
		limit=3,
		ignore_permissions=True
	)
	
	context.footer_courses = footer_courses
	
	return context
