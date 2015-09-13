# -*- coding: utf-8 -*-
{
    'name': "bitcoin_change",

    'summary': """
        Add bitcoin as a currency and enable exchange updates.""",

    'description': """
        Add bitcoin as a currency and enable exchange updates. 
    """,

    'author': "bisneSmart",
    'website': "http://www.bisnesmart.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Finance',
    'version': '0.1',
    'external_dependencies': ['python': 'bitpay-py2']

    # any module necessary for this one to work correctly
    'depends': ['base',
                'currency_rate_update',
                'currency_rate_date_check'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],

}