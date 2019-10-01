# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
no_cache = 1
no_sitemap = 1

def get_context(context):
	context.doc = frappe.get_doc("Website About Us Settings", "About Us Settings")
	docslideshow = context.doc.slideshow
	# if static page, get static content
	if docslideshow:
		slideshow = frappe.get_doc("Website Slideshow", docslideshow)
		context.slideshow = docslideshow
		context.slides = slideshow.get({"doctype":"Website Slideshow Item"})
		context.slideshow_header = slideshow.header or ""
	
	if context.doc.show_sidebar and context.doc.show_sidebar != "0":
		context.show_sidebar = context.doc.show_sidebar
		context.website_sidebar = context.doc.website_sidebar
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]

	return context
