# -*- coding: utf-8 -*-
# Copyright (c) 2019, Systematic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.website.utils import delete_page_cache

class WebsiteHomePage(Document):
	def validate(self):
		if not self.products_groups:
			self.setup_items_groups()

	def setup_items_groups(self):
		for d in frappe.get_all('Item Group', fields=['item_group_name', 'description', 'image'],
			filters={'show_in_website': 1}, limit=1):

			doc = frappe.get_doc('Item Group', d.item_group_name)
			if not doc.route:
				# set missing route
				doc.save()
			self.append('products_groups', dict(item_group_name=d.item_group_name,
				description=d.description, image=d.image))
