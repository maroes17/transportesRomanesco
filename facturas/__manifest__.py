# -*- coding: utf-8 -*-
{
    'name': "facturas",

    'summary': """
      Creación de facturas""",

    'description': """
        Sistema que permite la creación de borradores de facturas con la finalidad de ser llevadas a servicios internos
    """,

    'author': "Daniel Sepúlveda Véliz",
    'website': "https://github.com/DanielSepulvedaVeliz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Finanzas',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/views.xml',
        #'views/templates.xml',
        'views/views_factura.xml',
        'views/views_cliente.xml',
        'views/views_empresa.xml',
        'views/views_metodo.xml',
        'views/report.xml',
        

        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}