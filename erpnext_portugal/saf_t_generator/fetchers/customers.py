import frappe

def get_customers(company):
    customers = frappe.get_all("Customer", filters={"disabled": 0}, fields=[
        "name", "customer_name", "tax_id", "customer_group", "territory"
    ])

    results = []
    for c in customers:
        address = frappe.get_value("Dynamic Link", {
            "link_doctype": "Customer",
            "link_name": c.name,
            "parenttype": "Address"
        }, "parent")
        address_doc = frappe.get_doc("Address", address) if address else None
        results.append({
            "CustomerID": c.name,
            "CustomerTaxID": c.tax_id or "",
            "CompanyName": c.customer_name,
            "BillingAddress": address_doc.get("address_line1") if address_doc else "",
            "Country": address_doc.get("country") if address_doc else "PT"
        })
    return results