# -*- coding: utf-8 -*-
# Copyright (c) 2019, Systematic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

class Exhibitions(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/exhibitions_details.html",
		condition_field = "publish",
		page_title_field = "exhibition_name",
		no_cache = 1
	)
	def validate(self):
		if not self.route:
			self.route = 'events/' +self.scrub(self.exhibition_name)
		super(Exhibitions, self).validate()
	
	def get_context(self, context):
		context.description = self.description
		context.title = self.exhibition_name
		context.header = self.exhibition_name
		context.content = self.content
		

		
		exhibition_images_items = frappe.db.sql("""\
		select I.title, I.image
		from `tabExhibitions Images` I
		where I.parent = '{exhibition_name}' order by I.idx asc""".format(exhibition_name=self.name), as_dict=1)
		
		exhibition_images_items = [d for d in exhibition_images_items]		
		
		context.update({
			"parents": [{"name": frappe._("Home"), "route":"/"},{"name": frappe._("Events"), "route":"/events"}],
			"exhibition_image": self.image,
			"exhibition_starts_on": self.starts_on,
			"exhibition_ends_on": self.ends_on,
			"exhibition_location": self.location,
			"exhibition_images_items": exhibition_images_items,
		})
		
		# if static page, get static content
		if self.slideshow:
			context.update(get_slideshow(self))
			
		return context
