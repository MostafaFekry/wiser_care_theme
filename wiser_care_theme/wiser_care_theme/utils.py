# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import get_request_site_address, encode
from frappe.model.document import Document
from six.moves.urllib.parse import quote
from frappe.website.router import resolve_route
from erpnext.setup.doctype.item_group.item_group import get_group_item_count


def update_website_context(context):
	context["mostafa_test"] = frappe.form_dict._lang
	website_languages_request = frappe.form_dict._lang
	if website_languages_request:
		context["website_languages_request"] = website_languages_request
	else:
		context["website_languages_request"] = "en"
		website_languages_request = "en"
		
	context.update(get_website_languages_details(website_languages_request))
	context["website_languages_items"] = get_website_languages_items()
	
	website_settings = frappe.get_doc('Wiser Website Settings')
	context["enable_multilanguage_support"] = website_settings.enable_multilanguage_support
	context["display_language_picker_in_top_bar"] = website_settings.display_language_picker_in_top_bar
	
	context["facebook_link"] = website_settings.facebook_link
	context["linked_in_link"] = website_settings.linked_in_link
	context["twitter_link"] = website_settings.twitter_link
	context["instagram_link"] = website_settings.instagram_link
	context["google_link"] = website_settings.google_link
	
	# Mostafa return item groups sidebar items
	context["sidebarshow_item_group"] = sidebarshow_item_group()
	
	# Mostafa return medication type selected items
	context["medication_type"] = get_medication_type()
	
	
def get_website_languages_items():
	all_language_items = frappe.db.sql("""\
		select * from `tabWebsite Languages`
		where parent='Wiser Website Settings' 
		order by idx asc""", as_dict=1)

	website_languages_items = [d for d in all_language_items]
	return website_languages_items

def get_website_languages_details(website_languages_request="en"):
	website_languages_details = frappe.get_doc("Website Languages", website_languages_request)
	if not website_languages_details:
		return {}

	return {
		"website_languages_name": website_languages_details.language_name,
		"website_languages_flag": website_languages_details.language_flag,
		"banner_lang_html": website_languages_details.banner_lang_html,
		"newsletter_title": website_languages_details.newsletter_title,
		"newsletter_description": website_languages_details.newsletter_description,
		"newsletter_success_message": website_languages_details.newsletter_success_message,
		"newsletter_field": website_languages_details.newsletter_field,
		"newsletter_button": website_languages_details.newsletter_button,
		"social_tab_title": website_languages_details.social_tab_title,
		"location_tab_title": website_languages_details.location_tab_title,
		"location_details": website_languages_details.location_details,
		"opening_tab_title": website_languages_details.opening_tab_title,
		"opening_details": website_languages_details.opening_details,
		"call_tab_title": website_languages_details.call_tab_title,
		"call_details": website_languages_details.call_details,
		"website_languages_copyright": website_languages_details.copyright
	}

def sidebarshow_item_group():
	# Mostafa return item groups sidebar items
	item_group = frappe.db.sql("""\
		select IG.item_group_name,IG.show_in_website,IG.route,IG.is_group,IG.parent_item_group,IG.lft,IG.rgt from `tabItem Group` IG
		where IG.show_in_website=1 and IG.parent_item_group = 'Medicinal Effect'
		order by IG.lft asc""", as_dict=1)
		
	data = [d for d in item_group]
	
	sidebarshow_item_group = adjust_group_item_count_items(data)
	
	return sidebarshow_item_group
	
def adjust_group_item_count_items(data):
	adjusted_data = []

	for item in data:
		if not item.get('is_group'):
			item['item_item_group_count'] = get_group_item_count(item.get('item_group_name'))
		else:
			item['item_item_group_count'] = 0
		adjusted_data.append(item)

	return adjusted_data

# Mostafa return medication type selected items	
def get_medication_type(product_group=None):
	if product_group:
		item_group = frappe.get_cached_doc('Item Group', product_group)
		if item_group.is_group:
			# return child item groups if the type is of "Is Group"
			adjusted_data = []
			return adjusted_data
	
	#medication_type = frappe.db.sql("""\select MT.medication_type, MT.name, MT.image from `tabMedication Type` MT inner join `tabItem` I on MT.name = I.medication_type	and I.show_in_website = 1 and I.docstatus = 0 and (I.item_group = '{item_group_d}' or I.name in (select parent from `tabWebsite Item Group` where item_group = '{item_group_d}')) where MT.show_in_website =1 group by MT.medication_type order by MT.idx asc""".format(item_group_d=product_group), as_dict=1)

	medication_type = frappe.db.sql("""\
	select MT.medication_type, MT.name, MT.image from `tabMedication Type` MT inner join `tabItem` I on MT.name = I.medication_type	and I.show_in_website = 1 and I.docstatus = 0 where MT.show_in_website =1 group by MT.medication_type order by MT.idx asc""", as_dict=1)
	
	medication_type_item = [d for d in medication_type]
	
	return medication_type_item