# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class SaleOrderTO2(models.Model):
    _inherit = "sale.order"

    code_cliente = fields.Char(related='order_line.code_cliente')
    desc_cliente = fields.Char(related='order_line.desc_cliente')
