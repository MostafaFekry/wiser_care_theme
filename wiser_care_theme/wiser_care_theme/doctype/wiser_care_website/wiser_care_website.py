# -*- coding: utf-8 -*-
# Copyright (c) 2019, Systematic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.model.document import Document

class WiserCareWebsite(Document):
	pass
	
def update_website_context(context):
	context = frappe._dict({
		'website_languages_items': get_website_languages_items()
	})
	
	settings = frappe.get_single("Website Settings")
	for k in ["enable_multilanguage_support","display_language_picker_in_top_bar"]:
		if hasattr(settings, k):
			context[k] = settings.get(k)
	
	
def get_website_languages_items():
	all_language_items = frappe.db.sql("""\
		select * from `tabWebsite Languages`
		where parent='Website Settings' 
		order by idx asc""", as_dict=1)

	website_languages_items = [d for d in all_language_items]
	return website_languages_items


	

