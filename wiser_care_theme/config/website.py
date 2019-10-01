from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Portal"),
			"items": [
				{
					"type": "doctype",
					"name": "Website Home Page",
					"description": _("Settings for website home page"),
				}
			]
		},
		{
			"label": _("Agents"),
			"items": [
				{
					"type": "doctype",
					"name": "Agents",
					"description": _("Set default agents page data.")
				},
				{
					"type": "doctype",
					"name": "Agents Details",
					"description": _("Add agents details items.")
				}
			]
		},
		{
			"label": _("Items Categories"),
			"items": [
				{
					"type": "doctype",
					"name": "Medication Type",
					"description": _("Add Medication Type details items.")
				},
				{
					"type": "doctype",
					"name": "Species Settings",
					"description": _("Set Species agents page data.")
				},
				{
					"type": "doctype",
					"name": "Species",
					"description": _("Add Species details items.")
				}
			]
		},
		{
			"label": _("Exhibitions"),
			"items": [
				{
					"type": "doctype",
					"name": "Exhibitions",
					"description": _("Add Exhibitions details items.")
				}
			]
		}
	]
