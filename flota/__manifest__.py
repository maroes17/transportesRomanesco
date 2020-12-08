# -*- coding: utf-8 -*-
{
    'name': "flota",

    'summary': """
        Gesionar Flota de Vehiculos, en conjunto con los Conductores y gastos asociados""",

    'description': """
        El encargado tendrá a disposición diversas funcionalidades relacionadas con la administración
        de la flota de camiones que tiene Transportes Romanesco, hola hola, cambio
    """,

    'author': "Christian Vergara Retamal",
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
        'views/view_chofer.xml',
        'views/view_camion.xml',
        #'views/view_gastoCamion.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}