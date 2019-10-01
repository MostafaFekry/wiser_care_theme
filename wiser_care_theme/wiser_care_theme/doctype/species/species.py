# -*- coding: utf-8 -*-
# Copyright (c) 2019, Systematic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

class Species(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/species_details.html",
		condition_field = "publish",
		page_title_field = "species_name",
		no_cache = 1
	)
	def validate(self):
		if not self.route:
			self.route = 'species/' +self.scrub(self.species_name)
		super(Species, self).validate()
		
	def get_context(self, context):
		context.main_section = self.main_section
		context.title = self.species_name
		context.header = self.species_name
		
		species_item = frappe.db.sql("""\
		select name,species_name,route,image from `tabSpecies`
		where published=1
		order by idx asc""", as_dict=1)
		
		species_item_details = [d for d in species_item]
		species_item_details = adjust_species_count_items(species_item_details)
		
		medication_type = frappe.db.sql("""\
		select I.medication_type, I.name,  I.image from `tabMedication Type` I right join `tabItem` S on I.name = S.medication_type	and S.show_in_website = 1 and S.disabled = 0
		where I.show_in_website =1
		group by I.medication_type
		order by I.idx asc""", as_dict=1)
		
		species_medication_type = [d for d in medication_type]
		
		species_products_items = frappe.db.sql("""\
		select I.name, I.item_name, I.item_code, I.route, I.medication_type,S.medication_type as medication_type_name, I.image, I.website_image, I.thumbnail as website_description
		from `tabItem` I
		left join `tabMedication Type` S on I.medication_type = S.name
		where I.show_in_website = 1
			and I.disabled = 0
			and I.species_name = '{species_name_d}' order by S.idx asc""".format(species_name_d=self.name), as_dict=1)
		
		species_products_items = [d for d in species_products_items]
		
		
		context.update({
			"parents": [{"name": frappe._("Home"), "route":"/"},{"name": frappe._("Species"), "route":"/species"}],
			"species_image": self.image,
			"species_medication_type": species_medication_type,
			"species_sidebar_item": species_item_details,
			"species_products_items": species_products_items,
			"species_sidebar_title": "Species"
		})
		
		# if static page, get static content
		if self.slideshow:
			context.update(get_slideshow(self))
			
		return context


def adjust_species_count_items(data):
	adjusted_data = []

	for item in data:
		item['item_count'] = get_species_count(item.get('name'))
		adjusted_data.append(item)

	return adjusted_data
	
def get_species_count(species_name):
	return frappe.db.sql("""select count(*) as count from `tabItem`
		where docstatus = 0 and show_in_website = 1
		and species_name = '{species_name_d}' """ .format(species_name_d=species_name))[0][0]