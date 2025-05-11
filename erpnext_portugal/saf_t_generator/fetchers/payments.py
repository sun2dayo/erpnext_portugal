import frappe

def get_payments(company, start_date, end_date):
    payments = frappe.get_all("Payment Entry", filters={
        "company": company,
        "posting_date": ["between", [start_date, end_date]],
        "docstatus": 1,
        "payment_type": "Receive"
    }, fields=[
        "name", "party", "paid_amount", "posting_date", "reference_no"
    ])
    return payments