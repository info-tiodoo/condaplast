# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrderTO2(models.Model):
    _inherit = "purchase.order"

    more_cliente = fields.Char('Producto Proveedor')

    @api.onchange('order_line')
    def onchange_all_cliente(self):
        self.more_cliente = ''.join("%s %s" %
                                    (line.cod_proov, line.desc_proov)
                                    for line in self.order_line)
