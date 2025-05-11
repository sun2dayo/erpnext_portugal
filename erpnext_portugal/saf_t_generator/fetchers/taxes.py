import frappe

def get_taxes():
    tax_templates = frappe.get_all("Sales Taxes and Charges Template", fields=["name"])
    taxes = []

    for tpl in tax_templates:
        doc = frappe.get_doc("Sales Taxes and Charges Template", tpl.name)
        for row in doc.taxes:
            taxes.append({
                "TaxType": "IVA",
                "TaxCountryRegion": "PT",
                "TaxCode": "NOR" if row.rate >= 6 else "RED",
                "Description": row.account_head,
                "TaxPercentage": row.rate
            })
    return taxes