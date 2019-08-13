# -*- coding: utf-8 -*-
{
    'name': "Modul Mahal Buatan Orang Cilengsi",

    'summary': """
        ini modul cuma nambah 1 field doang""",

    'description': """
        ini modul cuma nambah 1 field doang. kenapa mahal? karena di buat oleh orang cilengsi
    """,

    'author': "PT. PT",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'apps',
    'version': '0.1',
    'price': 999,
    'currency': 'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
