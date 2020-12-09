# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockPickingTO2(models.Model):
    _inherit = "stock.picking"

    code_cliente = fields.Char(related='pack_operation_product_ids.code_cliente')
    desc_cliente = fields.Char(related='pack_operation_product_ids.desc_cliente')
