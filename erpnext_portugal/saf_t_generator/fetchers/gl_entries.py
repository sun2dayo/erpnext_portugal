import frappe

def get_gl_entries(company, start_date, end_date):
    entries = frappe.get_all("GL Entry", filters={
        "company": company,
        "posting_date": ["between", [start_date, end_date]]
    }, fields=[
        "name", "account", "posting_date", "remarks",
        "debit", "credit", "voucher_type", "voucher_no"
    ])
    return entries