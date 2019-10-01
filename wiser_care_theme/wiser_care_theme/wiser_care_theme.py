from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_request_site_address, encode
from frappe.model.document import Document
from six.moves.urllib.parse import quote
from frappe.website.router import resolve_route
from frappe.website.doctype.website_theme.website_theme import add_website_theme

@frappe.whitelist(allow_guest=True)
def update_website_context(context):
	context = frappe._dict({
		'website_languages_items': get_website_languages_items()
	})
	
	settings = frappe.get_single("Website Settings")
	for k in ["enable_multilanguage_support","display_language_picker_in_top_bar"]:
		if hasattr(settings, k):
			context[k] = settings.get(k)
	
	return context
	
def get_website_languages_items():
	all_language_items = frappe.db.sql("""\
		select * from `tabWebsite Languages`
		where parent='Website Settings' 
		order by idx asc""", as_dict=1)

	website_languages_items = [d for d in all_language_items]
	return website_languages_items