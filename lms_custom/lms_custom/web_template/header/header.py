import frappe
from frappe import _


def get_context(context):
    """Get context for header template"""

    # Brand information
    context.brand_name = frappe.db.get_single_value(
        "Website Settings", "app_name") or "Learning"
    context.brand_html = frappe.db.get_single_value(
        "Website Settings", "brand_html")

    # User information
    if frappe.session.user != "Guest":
        user = frappe.get_doc("User", frappe.session.user)
        context.full_name = user.full_name
        context.user_image = user.user_image
        context.username = user.username

        # Check user roles
        user_roles = frappe.get_roles(frappe.session.user)
        context.is_system_user = user.user_type == "System User"
        context.is_moderator = "Moderator" in user_roles
        context.is_instructor = "Instructor" in user_roles

        # Debug logging
        frappe.log_error(
            f"[header.py] User: {frappe.session.user}, Roles: {user_roles}", "Header Context")
    else:
        context.full_name = None
        context.user_image = None
        context.username = None
        context.is_system_user = False
        context.is_moderator = False
        context.is_instructor = False

    # Current route
    context.route = frappe.request.path or "/"

    return context
