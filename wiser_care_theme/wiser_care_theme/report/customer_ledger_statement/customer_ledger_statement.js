// Copyright (c) 2016, MostafaFekry and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Customer Ledger Statement"] = {
	"filters": [
		{
			"fieldname":"company",
			"label": __("Company"),
			"fieldtype": "Link",
			"options": "Company",
			"default": frappe.defaults.get_user_default("Company"),
			"reqd": 1
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today(),
			"reqd": 1,
			"width": "60px"
		},
		{
			"fieldtype": "Break",
		},
		{
			"fieldname":"party",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer",
			"reqd": 1,
			on_change: function() {
				var parties = frappe.query_report.get_filter_value('party');
				const values = parties.split(/\s*,\s*/).filter(d => d);

				if(!parties || values.length>1) {
					frappe.query_report.set_filter_value('party_name', "");
					frappe.query_report.set_filter_value('territory', "");
					return;
				} else {
					var party = values[0];
					var fieldname = erpnext.utils.get_party_name("Customer") || "name";
					frappe.db.get_value("Customer", party, fieldname, function(value) {
						frappe.query_report.set_filter_value('party_name', value[fieldname]);
					});
					frappe.db.get_value("Customer", party, "territory", function(value) {
						frappe.query_report.set_filter_value('territory', value["territory"]);
					});

					
				}
			}
		},
		{
			"fieldname":"party_name",
			"label": __("Customer Name"),
			"fieldtype": "Read Only"
		},
		{
			"fieldname":"group_by",
			"label": __("Group by"),
			"fieldtype": "Select",
			"options": ["", __("Group by Voucher"), __("Group by Voucher (Consolidated)"),
				__("Group by Account"), __("Group by Party")],
			"default": __("Group by Voucher (Consolidated)"),
			"hidden": 1
		},
		{
			"fieldname":"territory",
			"label": __("Territory"),
			"fieldtype": "Read Only"
		}
	]
}
