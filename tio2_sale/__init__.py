# -*- coding: utf-8 -*-

from. import models

from odoo import api, SUPERUSER_ID

def _update_customers(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for record in env['sale.order'].search([]):
        for line in record.order_line:
            description = "%s %s" % (line.code_cliente, line.desc_cliente)
            record.write({'more_cliente': description})
