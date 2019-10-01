# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, fmt_money, flt, nowdate, getdate

no_cache = 1
no_sitemap = 1

def get_context(context):

	homepage = frappe.get_doc('Website Home Page')
	context.title = homepage.title or homepage.company
	if homepage.main_section == None:
		context.main_section = ''

	
	if homepage.slideshow:
		context.slideshow = homepage.slideshow
		context.update(get_slideshow_details(homepage.slideshow))
		
	for itemgroup in homepage.products_groups:
		route = frappe.db.get_value('Item Group', itemgroup.item_group_name, 'route')
		if route:
			itemgroup.route = '/' + route
	
	for itemagents in homepage.agents:
		route = frappe.db.get_value('Agents Details', itemagents.agents_name, 'route')
		if route:
			itemagents.route = '/' + route
		image = frappe.db.get_value('Agents Details', itemagents.agents_name, 'image')
		if image:
			itemagents.image = image
	
	context.homepage = homepage
	return context

def get_slideshow_details(slideshow):

	slideshow = frappe.get_doc("Website Slideshow", slideshow)
	if not slideshow:
		return {}

	return {
		"slides": slideshow.get({"doctype":"Website Slideshow Item"}),
		"slideshow_header": slideshow.header or ""
	}

