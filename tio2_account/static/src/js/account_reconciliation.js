odoo.define('tio2_account.account_reconciliation_product', function (require) {
    "use strict";
    
    var core = require('web.core');
    var Model = require('web.Model');

    var FieldMany2One = core.form_widget_registry.get('many2one');

    var _t = core._t;
    
    var AccountReconciliation = require('account.reconciliation');
    console.log(AccountReconciliation);
    // Add a second button to reconcilation widget which only reconciles based on esr.
    AccountReconciliation.abstractReconciliation.include({
        
        init: function(parent, context) {
            this._super(parent);
        
            this.model_product_product = new Model("product.product");

            this.create_form_fields['product_id'] = {
                    id: "product_id",
                    index: 30,
                    corresponding_property: "product_id",   // a account.move.line field name
                    label: _t("Product"),
                    required: false,
                    constructor: FieldMany2One,
                    field_properties: {
                        relation: "product.product",
                        string: _t("Product"),
                        type: "many2one",
                    },
                }
        },

        fetchPresets: function() {  // line 198
            this._super(parent);
            
            var self = this;
            var deferred_last_update = self.model_presets.query(['write_date']).order_by('-write_date').first().then(function (data) {
                self.presets_last_write_date = (data ? data.write_date : undefined);
            });
            var deferred_presets = self.model_presets.query().order_by('-sequence', '-id').all().then(function (data) {
                self.presets = {};
                _(data).each(function(datum){
                    var preset = {
                        id: datum.id,
                        name: datum.name,
                        sequence: datum.sequence,
                        lines: [{
                            account_id: datum.account_id,
                            journal_id: datum.journal_id,
                            label: datum.label,
                            amount_type: datum.amount_type,
                            amount: datum.amount,
                            tax_id: datum.tax_id,
                            analytic_account_id: datum.analytic_account_id,
                            product_id: datum.product_id,
                        }]
                    };
                    if (datum.has_second_line) {
                        preset.lines.push({
                            account_id: datum.second_account_id,
                            journal_id: datum.second_journal_id,
                            label: datum.second_label,
                            amount_type: datum.second_amount_type,
                            amount: datum.second_amount,
                            tax_id: datum.second_tax_id,
                            analytic_account_id: datum.second_analytic_account_id,
                            product_id: datum.second_product_id,
                        });
                    }
                    self.presets[datum.id] = preset;
                });
            });
            return $.when(deferred_last_update, deferred_presets);
        },        
    });

    AccountReconciliation.abstractReconciliationLine.include({

        prepareCreatedMoveLinesForPersisting: function(lines) {
            this._super(lines);
            
            lines = _.filter(lines, function(line) { return !line.is_tax_line });
            return _.collect(lines, function(line) {
                var dict = {
                    account_id: line.account_id,
                    name: line.label
                };
                // Use amount_before_tax since the amount of the newly created line is adjusted to
                // reflect tax included in price in account_move_line.create()
                var amount = line.tax_id ? line.amount_before_tax: line.amount;
                dict['credit'] = (amount > 0 ? amount : 0);
                dict['debit'] = (amount < 0 ? -1 * amount : 0);
                if (line.tax_id) dict['tax_ids'] = [[4, line.tax_id, null]];
                if (line.analytic_account_id) dict['analytic_account_id'] = line.analytic_account_id;
                if (line.product_id) dict['product_id'] = line.product_id;
                return dict;
            });
        },
    });

});