import os
import datetime
import frappe
from jinja2 import Environment, FileSystemLoader
from lxml import etree

from erpnext_portugal.saf_t_generator.fetchers.header import get_header
from erpnext_portugal.saf_t_generator.fetchers.customers import get_customers
from erpnext_portugal.saf_t_generator.fetchers.items import get_items
from erpnext_portugal.saf_t_generator.fetchers.taxes import get_taxes
from erpnext_portugal.saf_t_generator.fetchers.gl_entries import get_gl_entries
from erpnext_portugal.saf_t_generator.fetchers.invoices import get_invoices
from erpnext_portugal.saf_t_generator.fetchers.payments import get_payments

def generate_saft(company, start_date, end_date, output_path="/tmp/saftpt.xml"):
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

    # Buscar os dados de cada secção
    context = {
        "header": get_header(company, start_date, end_date),
        "customers": get_customers(company),
        "products": get_items(),
        "taxes": get_taxes(),
        "gl_entries": get_gl_entries(company, start_date, end_date),
        "invoices": get_invoices(company, start_date, end_date),
        "payments": get_payments(company, start_date, end_date)
    }

    # Preparar o ambiente do template
    template_path = os.path.join(os.path.dirname(__file__), "templates")
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template("saft_template.xml.jinja")

    # Renderizar o XML
    from .renderer import render_saft_xml
    rendered_xml = render_saft_xml(context)

    # Validar contra XSD
    schema_path = os.path.join(os.path.dirname(__file__), "schema", "saftpt1.04_01.xsd")
    validate_saft(rendered_xml.encode("utf-8"), schema_path)

    # Guardar ficheiro
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_xml)

    return output_path

def validate_saft(xml_content, xsd_path):
    xml_doc = etree.fromstring(xml_content)
    with open(xsd_path, "rb") as xsd_file:
        xml_schema_doc = etree.parse(xsd_file)
        xml_schema = etree.XMLSchema(xml_schema_doc)

    if not xml_schema.validate(xml_doc):
        raise ValueError(f"Erro na validação SAF-T: {xml_schema.error_log}")
    return True

import frappe
from frappe.utils.response import build_response
from frappe import _

@frappe.whitelist()
def generate_saft(company, start_date, end_date):
    file_path = generate_saft_file(company, start_date, end_date)
    file_url = frappe.utils.file_manager.save_file(
        fname="saftpt.xml",
        content=open(file_path, 'rb').read(),
        dt=None,
        dn=None,
        is_private=0
    ).file_url
    return file_url



