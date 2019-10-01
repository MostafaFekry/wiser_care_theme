# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version
from frappe import _

app_name = "wiser_care_theme"
app_title = "Wiser Care Theme"
app_publisher = "MostafaFekry"
app_description = "Custom site for Wiser Care"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mostafa.fekry@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wiser_care_theme/css/wiser_care_theme.css"
# app_include_js = "/assets/wiser_care_theme/js/wiser_care_theme.js"

# include js, css files in header of web template
# web_include_css = "/assets/wiser_care_theme/css/wiser_care_theme.css"
# web_include_js = "/assets/wiser_care_theme/js/wiser_care_theme.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wiser_care_theme.utils.get_home_page"

# website
update_website_context = "wiser_care_theme.wiser_care_theme.utils.update_website_context"

# fixtures
fixtures = [{"dt": "Custom Field", "filters": [["name", "in", [
		"Customer-location",
		"Customer-المركز",
		"Company-cheques_under_collection_account",
		"Delivery Note-delivery_document_no",
		"Sales Invoice-delivery_document_no",
		"Payment Entry-payment_document_no",
		"Territory-territory_code",
		"Item-agent_name",
		"Item-medication_type",
		"Company History-title",
		"Company History-column_break_3",
		"Company History-image",
		"About Us Team Member-position",
		"Item-species_name",
		"Item Website Specification-arabic_description",
		"Website Slideshow Item-column_break_4",
		"Website Slideshow Item-link_tilte",
		"Website Slideshow Item-link_path",
		"Website Slideshow Item-link_target",
		"Website Slideshow Item-set_position",
		"Company History-old_year",
		"Sales Invoice-due_date_payment"
	]]]},
    {"dt": "Language", "filters": [["name", "in", [
		"en",
		"ar"
    ]]]},
    {"dt": "Website Languages", "filters": [["name", "in", [
		"en",
		"ar"
    ]]]},
    {"dt": "Top Bar Item"},
    {"dt": "Website Home Page"},
    {"dt": "Website About Us Settings"},
    {"dt": "Website Contact Us Settings"}
]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = [,"Agents Details", "Exhibitions", "Species"]

# Installation
# ------------

# before_install = "wiser_care_theme.install.before_install"
# after_install = "wiser_care_theme.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wiser_care_theme.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wiser_care_theme.tasks.all"
# 	],
# 	"daily": [
# 		"wiser_care_theme.tasks.daily"
# 	],
# 	"hourly": [
# 		"wiser_care_theme.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wiser_care_theme.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wiser_care_theme.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wiser_care_theme.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wiser_care_theme.event.get_events"
# }

