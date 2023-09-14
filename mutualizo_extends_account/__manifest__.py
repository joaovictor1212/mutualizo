# -*- coding: utf-8 -*-
{
    'name': 'Account Foreign Exchange Rate',
    'version': '1.0',
    'summary': 'Summary of My Module',
    'depends': ['base','sale', 'account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account_foreign_exchange_rate.xml',
        'views/account_move.xml',
       
       
    ],
    
    'application': True,
    'installable': True,
}