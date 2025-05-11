frappe.ui.form.on('Company', {
    refresh: function(frm) {
        frm.add_custom_button(__('Exportar SAF-T (PT)'), function() {
            frappe.call({
                method: 'erpnext_portugal.saf_t_generator.generator.generate_saft',
                args: {
                    company: frm.doc.name,
                    start_date: frappe.datetime.year_start(),
                    end_date: frappe.datetime.year_end()
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint(__('Clique para descarregar o ficheiro SAF-T'));
                        window.open(r.message);  // link para download
                    } else {
                        frappe.msgprint(__('Falha ao gerar o ficheiro SAF-T.'));
                    }
                }
            });
        }, __('Exportações'));
    }
});