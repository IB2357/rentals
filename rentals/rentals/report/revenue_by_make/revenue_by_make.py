# Copyright (c) 2025, Ibrahim Sultan and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns = [
		{
			"fieldname":"make",
			"label":"Make",
			"fieldtype":"Data"
		},
		{
			"fieldname":"total_revenue",
			"label":"Total Revenue ",
			"fieldtype":"Currency",
			"options":"YER"
		}
	]

	data = frappe.get_all("Ride Booking", 
		fields=["SUM(total_amount) AS total_revenue", "vehicle.make"], 
		filters={"docstatus":1},
		group_by="make"
	)
	
	return columns, data
