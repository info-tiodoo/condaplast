# -*- coding: utf-8 -*-
{
    'name': "Extend Sale - Condaplast",
    'version' : '10.0.1.1.1',
    'description': """
        - Add Customer 'Code' and 'Description' fields to Sale order search view
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.pt",
    'category': 'Accounting',
    'depends': ['sale'], #['gst_condaplast_sale'],
    'data': [
        'views/sale_order_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': '_update_customers',
}