app_name = "erpnext_portugal"
app_title = "ERPNext Portugal"
app_publisher = "NovaDX - Octávio Daio"
app_description = "Localização fiscal portuguesa para ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "apps@novadx.eu"
app_license = "MIT"

# Inclui JS personalizado na interface
#app_include_js = "/assets/erpnext_portugal/js/company_saft_export.js"

# Associar o JS diretamente ao Doctype Company (sem build)
doctype_js = {
    "Company": "public/js/company_saft_export.js"
}

# Fixtures (opcional)
# fixtures = ["Custom Field", "Property Setter"]

# Scripts de instalação (se necessário futuramente)
# after_install = "erpnext_portugal.setup.after_install"