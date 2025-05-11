# ERPNext Portugal

Localização fiscal portuguesa para ERPNext, incluindo exportação do ficheiro SAF-T (PT) conforme a Portaria n.º 321-A/2007.

## 📦 Funcionalidades

- Exportação do ficheiro SAF-T (PT) em formato XML
- Validação contra o schema XSD oficial da AT
- Botão direto na Empresa (Doctype `Company`) para gerar e descarregar o ficheiro

## 📁 Estrutura

- Geração do ficheiro SAF-T com dados reais do ERPNext
- Template XML com `jinja2`
- Ficheiros separados por secção: `Header`, `MasterFiles`, `GeneralLedgerEntries`, `SourceDocuments`

## 🚀 Instalação

```bash
# Clonar o repositório (exemplo)
cd ~/frappe-bench/apps
git clone https://github.com/teu-utilizador/erpnext_portugal.git

# Instalar no site desejado
bench --site nome_do_site install-app erpnext_portugal

# Recarregar o site (sem necessidade de bench build!)
bench --site nome_do_site clear-cache
bench --site nome_do_site reload-doc accounts doctype company
bench restart
```

## ✅ Requisitos

- Frappe >= 14.x
- ERPNext >= 14.x
- Python packages:
  - `lxml`
  - `jinja2`

Instalação das dependências (caso necessário):

```bash
pip install -r requirements.txt
```

## 🧪 Utilização

1. Aceda ao Doctype **Company**
2. Clique no botão **"Exportar SAF-T (PT)"**
3. O ficheiro XML será gerado, validado e descarregado automaticamente

## ⚖️ Licença

Este projeto é licenciado sob a [GNU General Public License v3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.pt-br.html).

---

Desenvolvido por **NovaDX - Octávio Daio** · 🇵🇹 🇸🇹 🇱🇺  
Para mais informações, contacte: `app@novadx.eu`