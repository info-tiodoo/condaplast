# -*- coding: utf-8 -*-
{
    'name': "Extend Product - Condaplast",
    'version' : '10.0.1.1.2',
    'description': """
        - Add 'Marca' field to Product variant search views
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.pt",
    'category': 'Accounting',
    'depends': ['gst_condaplast_product'],
    'data': [
        'views/product_product_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}