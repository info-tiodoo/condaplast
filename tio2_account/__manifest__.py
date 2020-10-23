# -*- coding: utf-8 -*-
{
    'name': "Extend Invoicing - Condaplast",
    'version' : '10.0.1.1.1',
    'summary': """
        Add 'Product' field to Reconciliation model
    """,
    'sequence': 30,
    'author': "TiOdoo",
    'website': "http://tiodoo.es",
    'category': 'Accounting',
    'depends': ['account', 'l10n_es'],
    'data': [
        'views/reconciliation_asset.xml',
        'views/account_reconcile_model_view.xml',
    ],
    'demo': [
        
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}