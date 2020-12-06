# -*- coding: utf-8 -*-
{
    'name': "viajes",

    'summary': """
        Digitar los viajes y servicio asociado """,

    'description': """
        El encargado será capaz de anotar los viajes del servicio prestado junto con los gastos y costos necesarios.
    """,

    'author': "Matías Rojas",
    'website': "http://www.transromanesco.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_ruta.xml',
        'views/view_costos.xml',
        'views/view_trayecto.xml',
        'views/templates.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}