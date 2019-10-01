# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
no_cache = 1
no_sitemap = 1

def get_context(context):
	context.doc = frappe.get_doc("About Us Settings", "About Us Settings")
	
	docslideshow = context.doc.slideshow
	# if static page, get static content
	if docslideshow:
		slideshow = frappe.get_doc("Website Slideshow", docslideshow)
		context.slideshow = docslideshow
		context.slides = slideshow.get({"doctype":"Website Slideshow Item"})
		context.slideshow_header = slideshow.header or ""
	
	exhibitions_item = frappe.db.sql("""\
		select exhibition_name,starts_on,ends_on,location,description,route,image,last_exhibitions_start_on from `tabExhibitions`
		where published=1
		order by starts_on desc""", as_dict=1)
		
	context.exhibitions_item_details = [d for d in exhibitions_item]
			
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]

	return context
