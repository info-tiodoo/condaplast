# -*- coding: utf-8 -*-

from. import models

from odoo import api, SUPERUSER_ID

def _update_suppliers(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    for record in env['purchase.order'].search([]):
        for line in record.order_line:
            description = "%s %s" % (line.cod_proov, line.desc_proov)
            record.write({'more_cliente': description})