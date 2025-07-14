# Copyright (c) 2025, Ibrahim Sultan and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Driver(Document):
	def before_save(self):
		self.full_name = self.first_name

		if self.last_name:
			self.full_name += f" {self.last_name}" 
		

	def send_alert(self):
		print("i am an alert!")