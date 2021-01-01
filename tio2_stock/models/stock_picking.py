# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockPickingTO2(models.Model):
    _inherit = "stock.picking"

    more_cliente = fields.Char('Producto Cliente/Proveedor')

    @api.onchange('pack_operation_product_ids')
    def onchange_all_cliente(self):
        self.more_cliente = ''.join("%s %s" %
                                    (line.code_cliente, line.desc_cliente)
                                    for line in self.pack_operation_product_ids)
