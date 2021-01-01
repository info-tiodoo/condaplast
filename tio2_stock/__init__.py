# -*- coding: utf-8 -*-

from. import models

from odoo import api, SUPERUSER_ID

def _update_pickings(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for record in env['stock.picking'].search([]):
        for line in record.pack_operation_product_ids:
            description = "%s %s" % (line.code_cliente, line.desc_cliente)
            record.write({'more_cliente': description})