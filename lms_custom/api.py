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


@frappe.whitelist(allow_guest=True)
def send_contact_message(lead_name, email_id, phone, subject, message):
	"""Handle contact form submissions from website"""
	try:
		# Validate required fields
		if not lead_name or not email_id or not subject or not message:
			frappe.throw(_("Please fill all required fields"))

		# Validate email format
		from frappe.utils import validate_email_address
		validate_email_address(email_id, throw=True)

		# Create a Communication record to store the message
		comm = frappe.get_doc({
			"doctype": "Communication",
			"sender": email_id,
			"sender_full_name": lead_name,
			"subject": f"Contact Form: {subject}",
			"content": f"""
				<div>
					<p><strong>Name:</strong> {lead_name}</p>
					<p><strong>Email:</strong> {email_id}</p>
					<p><strong>Phone:</strong> {phone or 'Not provided'}</p>
					<p><strong>Subject:</strong> {subject}</p>
					<hr>
					<p><strong>Message:</strong></p>
					<p>{message}</p>
				</div>
			""",
			"communication_type": "Communication",
			"communication_medium": "Email",
			"sent_or_received": "Received",
			"status": "Open"
		})
		comm.insert(ignore_permissions=True)
		frappe.db.commit()

		# Try to send notification email to admin (optional - won't fail if not configured)
		try:
			admin_email = frappe.db.get_single_value("System Settings", "email_footer_address")
			if admin_email:
				frappe.sendmail(
					recipients=[admin_email],
					subject=f"New Contact Form Submission: {subject}",
					message=f"""
						<h3>New Contact Form Submission</h3>
						<p><strong>Name:</strong> {lead_name}</p>
						<p><strong>Email:</strong> {email_id}</p>
						<p><strong>Phone:</strong> {phone or 'Not provided'}</p>
						<p><strong>Subject:</strong> {subject}</p>
						<hr>
						<p><strong>Message:</strong></p>
						<p>{message}</p>
					""",
					now=True
				)
		except Exception as email_error:
			# Log email error but don't fail the whole process
			frappe.log_error(f"[api.py] Email notification failed: {str(email_error)}", "Contact Form Email")

		return {
			"success": True,
			"message": "okay"
		}

	except Exception as e:
		frappe.log_error(f"[api.py] method: send_contact_message - {str(e)}", "Contact Form API")
		return {
			"success": False,
			"message": str(e)
		}
