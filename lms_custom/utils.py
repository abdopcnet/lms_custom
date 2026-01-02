import frappe


def update_website_context(context):
    """Add custom context to all website pages"""
    # Add your custom brand settings
    context.brand_name = frappe.db.get_single_value(
        "Website Settings", "app_name") or "My LMS"
    context.brand_logo = frappe.db.get_single_value(
        "Website Settings", "banner_image")

    # Add user info if logged in
    if frappe.session.user != "Guest":
        user = frappe.db.get_value(
            "User",
            frappe.session.user,
            ["full_name", "user_image", "username"],
            as_dict=True
        )
        if user:
            context.full_name = user.full_name
            context.user_image = user.user_image
            context.username = user.username

            # Check user roles
            roles = frappe.get_roles(frappe.session.user)
            context.is_instructor = "Course Creator" in roles
            context.is_moderator = "Moderator" in roles
            context.is_system_user = frappe.db.get_value(
                "User", frappe.session.user, "user_type") == "System User"
