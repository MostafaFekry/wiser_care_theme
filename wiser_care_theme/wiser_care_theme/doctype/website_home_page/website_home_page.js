// Copyright (c) 2019, Systematic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Website Home Page', {
	setup: function(frm) {
		frm.fields_dict["products_groups"].grid.get_field("item_group_name").get_query = function(){
			return {
				filters: {'show_in_website': 1}
			}
		},
		frm.fields_dict["agents"].grid.get_field("agents_name").get_query = function(){
			return {
				filters: {'published': 1}
			}
		}
	},
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Homepage Products Groups', {
	item_group_name: function(frm, cdt, cdn) {
		var featured_product_group = frappe.model.get_doc(cdt, cdn);
		if (featured_product_group.item_group_name) {
			frappe.call({
				method: 'frappe.client.get_value',
				args: {
					'doctype': 'Item Group',
					'filters': {'item_group_name': featured_product_group.item_group_name},
					'fieldname': [
						'description',
						'image'
					]
				},
				callback: function(r) {
					if (!r.exc) {
						$.extend(featured_product_group, r.message);
						if (r.message.description) {
							featured_product_group.description = r.message.description;
						}
						frm.refresh_field('Homepage Products Groups');
					}
				}
			});
		}
	}
});

frappe.ui.form.on('Homepage Agents', {
	agents_name: function(frm, cdt, cdn) {
		var featured_agents_name = frappe.model.get_doc(cdt, cdn);
		if (featured_agents_name.agents_name) {
			frappe.call({
				method: 'frappe.client.get_value',
				args: {
					'doctype': 'Agents Details',
					'filters': {'agent_name': featured_agents_name.agents_name},
					'fieldname': [
						'image'
					]
				},
				callback: function(r) {
					if (!r.exc) {
						$.extend(featured_agents_name, r.message);
						if (r.message.image) {
							featured_agents_name.image = r.message.image;
						}
						frm.refresh_field('Homepage Agents');
					}
				}
			});
		}
	}
});
