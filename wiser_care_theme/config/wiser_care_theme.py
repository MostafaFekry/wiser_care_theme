from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Website Settings",
					"description": _("Setup of top navigation bar, footer and logo."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Wiser Website Settings",
					"description": _("Setup site Language."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Home Page",
					"description": _("Settings for website home page"),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website About Us Settings",
					"description": _("Settings for About Us Page."),
				},
				{
					"type": "doctype",
					"name": "Website Contact Us Settings",
					"description": _("Settings for Contact Us Page."),
				},
				{
					"type": "doctype",
					"name": "Coming Soon Settings",
					"description": _("Settings for Coming Soon Page."),
				},
				
			]
		},
		{
			"label": _("Web Item Details"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Item",
				},
				{
					"type": "doctype",
					"name": "Item Group",
					"icon": "fa fa-sitemap",
					"label": _("Item Group"),
					"link": "Tree/Item Group",
				},
				{
					"type": "doctype",
					"name": "Medication Type",
					"description": _("Set medication type items."),
				},
				{
					"type": "doctype",
					"name": "Agents",
					"description": _("Set agents."),
				},
				{
					"type": "doctype",
					"name": "Agents Details",
					"description": _("Set agents details."),
				},
				{
					"type": "doctype",
					"name": "Species Settings",
					"description": _("Set species settings."),
				},
				{
					"type": "doctype",
					"name": "Species",
					"description": _("Set species."),
				},				
			]
		},
		{
			"label": _("Web Site"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Web Page",
					"description": _("Content web page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Slideshow",
					"description": _("Embed image slideshows in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Route Meta",
					"description": _("Add meta tags to your web pages"),
				},
				{
					"type": "doctype",
					"name": "Exhibitions",
					"description": _("Add exhibition to your exhibitions web page"),
				},
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "report",
					"name": "Customer Ledger Statement",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Supplier Ledger Statement",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
			]
		},

	]