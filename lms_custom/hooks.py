app_name = "lms_custom"
app_title = "Lms Custom"
app_publisher = "abdopcnet@gmail.om"
app_description = "Lms Custom"
app_email = "abdopcnet@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "lms_custom",
# 		"logo": "/assets/lms_custom/logo.png",
# 		"title": "Lms Custom",
# 		"route": "/lms_custom",
# 		"has_permission": "lms_custom.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/lms_custom/css/rtl.css"
app_include_js = "/assets/lms_custom/js/rtl_setup.js"

# ---------------
# include js, css files in header of web template
web_include_css = [
	"/assets/lms_custom/css/rtl.css"
]

web_include_js = [
    "/assets/lms_custom/js/rtl_setup.js"
]
# --------------------
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lms_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "lms_custom/public/icons.svg"

# Home Pages
# ----------
# -------------------------------
# # application home page (will override Website Settings)
# home_page = "home"

# Override home page for website users - return home page instead of /lms
get_website_user_home_page = "lms_custom.utils.get_website_user_home_page"

# # Website route rules to override LMS pages
# website_route_rules = [
#     {"from_route": "/", "to_route": "lms_custom_index"},
#     {"from_route": "/courses", "to_route": "courses"},
#     {"from_route": "/lms/courses", "to_route": "courses"},
#     {"from_route": "/lms/job-openings", "to_route": "jobs"},
#     {"from_route": "/lms/statistics", "to_route": "statistics"},
#     {"from_route": "/lms/batches", "to_route": "batches"},
# ]

# Override LMS backend functions with custom templates
# But keep using LMS data/API
# update_website_context = [
#     "lms_custom.utils.update_website_context",
# ]
# ------------
# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "lms_custom.utils.jinja_methods",
# 	"filters": "lms_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "lms_custom.install.before_install"
# after_install = "lms_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "lms_custom.uninstall.before_uninstall"
# after_uninstall = "lms_custom.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "lms_custom.utils.before_app_install"
# after_app_install = "lms_custom.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "lms_custom.utils.before_app_uninstall"
# after_app_uninstall = "lms_custom.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lms_custom.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Login Events
# -------------
# Override LMS login redirect to go to home page instead of /lms
# Using on_session_creation because it runs AFTER set_user_info
on_session_creation = "lms_custom.utils.on_session_creation"

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lms_custom.tasks.all"
# 	],
# 	"daily": [
# 		"lms_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"lms_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lms_custom.tasks.weekly"
# 	],
# 	"monthly": [
# 		"lms_custom.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "lms_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lms_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lms_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["lms_custom.utils.before_request"]
# after_request = ["lms_custom.utils.after_request"]

# Job Events
# ----------
# before_job = ["lms_custom.utils.before_job"]
# after_job = ["lms_custom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"lms_custom.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []
