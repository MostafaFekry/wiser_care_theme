# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.website.render

from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

no_cache = 1
no_sitemap = 1

def get_context(context):
	agents = frappe.get_doc('Agents')
	
	agents_item = frappe.db.sql("""\
		select agent_name,route,image from `tabAgents Details`
		where published=1
		order by idx asc""", as_dict=1)
		
	context.agents_item_details = [d for d in agents_item]

	if agents.slideshow:
		slideshow = frappe.get_doc("Website Slideshow", agents.slideshow)
		context.slideshow = agents.slideshow
		context.slides = slideshow.get({"doctype":"Website Slideshow Item"})
		context.slideshow_header = slideshow.header or ""

	context.title = agents.title
	context.main_section = agents.main_section
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]
	
	return context