# -*- coding: utf-8 -*-
{
    'name': "Force OverWrite All QTYs",

    'summary': """
       A scorched-earth solution to the problem of overwriting all the QTYs in the stock.quant model. Not elegant, but it works.""",

    'description': """
        Overwrite all the QTYs in a stock.quant. Primarily used to reset the QTYs in a stock.quant to 0.0 or deal with the "It is not possible to unreserve more products of ... than you have in stock." error.
        
    """,

    'author': "Fabian Anguiano",
    'website': "https://fabiananguiano.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],   

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
