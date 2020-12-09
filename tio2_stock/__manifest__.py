# -*- coding: utf-8 -*-
{
    'name': "Extend Stock - Condaplast",
    'version' : '10.0.1.1.2',
    'description': """
        - Add 'Code' and 'Description' fields to Stock picking search view
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.pt",
    'category': 'Accounting',
    'depends': ['gst_condaplast_stock'],
    'data': [
        'views/stock_picking_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}