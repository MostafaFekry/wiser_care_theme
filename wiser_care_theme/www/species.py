# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
import frappe.website.render

from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

no_cache = 1
no_sitemap = 1

def get_context(context):
	species = frappe.get_doc('Species Settings')
	
	species_item = frappe.db.sql("""\
		select species_name,route,image from `tabSpecies`
		where published=1
		order by idx asc""", as_dict=1)
		
	context.species_item_details = [d for d in species_item]

	if species.slideshow:
		slideshow = frappe.get_doc("Website Slideshow", species.slideshow)
		context.slideshow = species.slideshow
		context.slides = slideshow.get({"doctype":"Website Slideshow Item"})
		context.slideshow_header = slideshow.header or ""

	context.title = species.species_title
	context.main_section = species.main_section
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]
	
	return context