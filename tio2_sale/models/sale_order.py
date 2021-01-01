# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderTO2(models.Model):
    _inherit = "sale.order"

    more_cliente = fields.Char('Producto Cliente')

    @api.onchange('order_line')
    def onchange_all_cliente(self):
        self.more_cliente = ''.join("%s %s" %
                                    (line.code_cliente, line.desc_cliente)
                                    for line in self.order_line)