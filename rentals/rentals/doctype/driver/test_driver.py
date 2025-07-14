# Copyright (c) 2025, Ibrahim Sultan and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


# class TestDriver(FrappeTestCase):
	
# 	def test_driver_full_name(self):
# 		pass 

# 	def test_driver_full_name_if_last_name_not_set(self):
# 		pass

class TestDriver(FrappeTestCase):
    
    def test_driver_full_name(self):
        driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "John",
            "last_name": "Doe",
            "license_number":"TASNEEM"
        })
        driver.insert()

        self.assertEqual(driver.full_name, "John Doe")

    def test_driver_full_name_if_last_name_not_set(self):
        driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Alice",
            "license_number":"TASNEEM"
        })
        driver.insert()

        self.assertEqual(driver.full_name, "Alice")