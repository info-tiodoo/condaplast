# -*- coding: utf-8 -*-
{
    'name': "Extend Purchase - Condaplast",
    'version' : '10.0.1.1.1',
    'description': """
        - Add Supplier 'Code' and 'Description' fields to Purchase order search view
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.pt",
    'category': 'Accounting',
    'depends': ['gst_condaplast_purchase'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}