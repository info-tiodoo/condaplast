# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountReconcileModel(models.Model):
    _inherit = "account.reconcile.model"

    product_id = fields.Many2one('product.product', string='Product',
        ondelete='restrict', index=True)
    second_product_id = fields.Many2one('product.product', string='Product',
        ondelete='restrict', index=True)