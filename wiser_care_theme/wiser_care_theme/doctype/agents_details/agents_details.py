# -*- coding: utf-8 -*-
# Copyright (c) 2019, Systematic and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow

class AgentsDetails(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/agents_details.html",
		condition_field = "publish",
		page_title_field = "agent_name",
		no_cache = 1
	)
	def validate(self):
		if not self.route:
			self.route = 'agents/' +self.scrub(self.agent_name)
		super(AgentsDetails, self).validate()
		
	def get_context(self, context):
		context.main_section = self.main_section
		context.title = self.agent_name
		context.header = self.agent_name
		
		agents_item = frappe.db.sql("""\
		select name,agent_name,route,image from `tabAgents Details`
		where published=1
		order by idx asc""", as_dict=1)
		
		agents_item_details = [d for d in agents_item]
		agents_item_details = adjust_agents_count_items(agents_item_details)
		
		medication_type = frappe.db.sql("""\
		select I.medication_type, I.name,  I.image from `tabMedication Type` I right join `tabItem` S on I.name = S.medication_type	and S.show_in_website = 1 and S.disabled = 0
		where I.show_in_website =1
		group by I.medication_type
		order by I.idx asc""", as_dict=1)
		
		agents_medication_type = [d for d in medication_type]
		
		agents_products_items = frappe.db.sql("""\
		select I.name, I.item_name, I.item_code, I.route, I.medication_type,S.medication_type as medication_type_name, I.image, I.website_image, I.thumbnail as website_description
		from `tabItem` I
		left join `tabMedication Type` S on I.medication_type = S.name
		where I.show_in_website = 1
			and I.disabled = 0
			and I.agent_name = '{agent_name_d}' order by S.idx asc""".format(agent_name_d=self.name), as_dict=1)
		
		agents_products_items = [d for d in agents_products_items]
		
		
		context.update({
			"parents": [{"name": frappe._("Home"), "route":"/"},{"name": frappe._("Agents"), "route":"/agents"}],
			"agents_image": self.image,
			"agents_medication_type": agents_medication_type,
			"agent_sidebar_item": agents_item_details,
			"agents_products_items": agents_products_items,
			"agent_sidebar_title": "Agents"
		})
		
		# if static page, get static content
		if self.slideshow:
			context.update(get_slideshow(self))
			
		return context


def adjust_agents_count_items(data):
	adjusted_data = []

	for item in data:
		item['item_count'] = get_agents_count(item.get('name'))
		adjusted_data.append(item)

	return adjusted_data
	
def get_agents_count(agent_name):
	return frappe.db.sql("""select count(*) as count from `tabItem`
		where docstatus = 0 and show_in_website = 1
		and agent_name = '{agent_name_d}' """ .format(agent_name_d=agent_name))[0][0]