# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoiceTO2(models.Model):
    _inherit = "account.invoice"

    inv_product_id = fields.Many2one('product.product', related='invoice_line_ids.product_id', string='Productos')
    inv_line_name = fields.Text(related='invoice_line_ids.name', string='Vendedor/Descripción')
