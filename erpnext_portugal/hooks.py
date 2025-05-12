# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from . import __version__ as app_version
except ImportError:
    app_version = "0.0.1"
app_name = "erpnext_portugal"
app_title = "ERPNext Portugal"
app_publisher = "NovaDX - Octávio Daio"
app_description = "Localização fiscal portuguesa para ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "apps@novadx.eu"
app_license = "GPL-3.0"
required_apps = ["erpnext"]

# Inclui JS personalizado na interface
#app_include_js = "/assets/erpnext_portugal/custom_scripts/company_saft_export.custom_scripts"

# Associar o JS diretamente ao Doctype Company (sem build)
doctype_js = {
    "Company": ["erpnext_portugal/custom_scripts/company_saft_export.js"]
}

# Fixtures (opcional)
# fixtures = ["Custom Field", "Property Setter"]

# Scripts de instalação (se necessário futuramente)
# after_install = "erpnext_portugal.setup.after_install"