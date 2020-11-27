# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class PurchaseOrderTO2(models.Model):
    _inherit = "purchase.order"

    cod_proov = fields.Char(related='order_line.cod_proov')
    desc_proov = fields.Char(related='order_line.desc_proov')
