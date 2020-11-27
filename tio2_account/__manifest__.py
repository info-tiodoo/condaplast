# -*- coding: utf-8 -*-
{
    'name': "Extend Invoicing - Condaplast",
    'version' : '10.0.1.3.1',
    'description': """
        - Add 'Product' field to Reconciliation model \n
        - Add 'Product' field to Invoice views \n
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.es",
    'category': 'Accounting',
    'depends': ['account', 'l10n_es'],
    'data': [
        'views/account_invoice_view.xml',
        'views/reconciliation_asset.xml',
        'views/account_reconcile_model_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}