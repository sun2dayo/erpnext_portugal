import frappe
import datetime

def get_header(company, start_date, end_date):
    company_doc = frappe.get_doc("Company", company)

    return {
        "audit_file_version": "1.04_01",
        "company_tax_id": company_doc.tax_id or "",
        "company_name": company_doc.company_name,
        "fiscal_year": start_date.year,
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "currency": company_doc.default_currency or "EUR",
        "software_cert_no": "XXXX",  # Substituir pelo número real
        "product_id": "ERPNextPT",
        "product_version": "v1.0",
        "system_entry_date": datetime.datetime.now().isoformat(),
        "header_comment": "Exportação gerada automaticamente"
    }