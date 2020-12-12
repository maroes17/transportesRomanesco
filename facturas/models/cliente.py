# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Cliente(models.Model):
     _name = 'facturas.cliente'
     _description = 'Modelo de clientesssss'
     _rec_name= 'namec'
    #datos cliente
     namec = fields.Char(string="Nombre Cliente",required=True)
     rutc = fields.Char(string="Rut Cliente",required=True)
     domicilioc = fields.Char(string="Direccion Cliente",required=True)
     telefonoc = fields.Char(string="Telefono Cliente",required=True)