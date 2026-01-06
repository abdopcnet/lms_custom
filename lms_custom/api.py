import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def subscribe_newsletter(email):
	"""Subscribe email to newsletter"""
	try:
		if not email:
			frappe.throw(_("Email is required"))

		# Validate email format
		import re
		email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
		if not re.match(email_regex, email):
			frappe.throw(_("Invalid email format"))

		# Get or create default newsletter email group
		email_group_name = "Website Subscribers"
		if not frappe.db.exists("Email Group", email_group_name):
			email_group = frappe.get_doc({
				"doctype": "Email Group",
				"title": email_group_name
			})
			email_group.insert(ignore_permissions=True)

		# Check if email already subscribed to this group
		existing_member = frappe.db.get_value(
			"Email Group Member",
			{"email": email, "email_group": email_group_name},
			"name"
		)
		
		if existing_member:
			return {
				"success": False,
				"message": _("Email already subscribed")
			}

		# Create email group member
		member = frappe.get_doc({
			"doctype": "Email Group Member",
			"email": email,
			"email_group": email_group_name,
			"unsubscribed": 0
		})
		member.insert(ignore_permissions=True)
		frappe.db.commit()

		return {
			"success": True,
			"message": _("Successfully subscribed to newsletter")
		}

	except Exception as e:
		frappe.log_error("[api.py] method: subscribe_newsletter", "Newsletter API")
		frappe.throw(_("Failed to subscribe. Please try again."))
