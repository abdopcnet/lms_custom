import frappe


def get_website_user_home_page(user):
    """Return home page for website users - override LMS default"""
    # Log to verify this is being called
    print(f"[lms_custom] get_website_user_home_page called for user: {user}")
    frappe.log_error(f'get_website_user_home_page called for user: {user}', 'LMS Custom Home Page')
    # Always return home page for all users
    return "/"


def on_session_creation(login_manager):
    """Override redirect after session creation - runs AFTER set_user_info"""
    try:
        print(f"[lms_custom] on_session_creation called for user: {login_manager.user}")
        
        # Get user type
        user_type = frappe.db.get_value("User", login_manager.user, "user_type")
        
        print(f"[lms_custom] User type: {user_type}")
        print(f"[lms_custom] Current home_page: {frappe.local.response.get('home_page')}")
        print(f"[lms_custom] Overriding home_page to /")
        
        # Override the home_page that was set by set_user_info
        frappe.local.response["home_page"] = "/"
        
        print(f"[lms_custom] Final home_page: {frappe.local.response.get('home_page')}")
        frappe.log_error(f'on_session_creation: Overrode home_page to / for user {login_manager.user}', 'LMS Custom Login')
            
    except Exception as e:
        print(f"[lms_custom] Error in on_session_creation: {str(e)}")
        frappe.log_error(f'[utils.py] method: on_session_creation - Error: {str(e)}', 'LMS Custom Login')


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
