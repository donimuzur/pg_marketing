# -*- coding: utf-8 -*-
{
    'name': "PG DB marketing",
    
    'summary': """
        Database Marketing
    """,

    'author': "Polowijo Gosari Indonesia",
    'website': "http://www.polowijogosari.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/master_area.xml',
        'views/db_kios.xml',
        'views/db_penjualan.xml',
    ],
}

