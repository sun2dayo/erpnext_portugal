import frappe

def get_invoices(company, start_date, end_date):
    invoices = frappe.get_all("Sales Invoice", filters={
        "company": company,
        "posting_date": ["between", [start_date, end_date]],
        "docstatus": 1
    }, fields=[
        "name", "customer", "posting_date", "net_total", "total", "taxes_and_charges"
    ])
    return invoices