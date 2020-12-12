# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Empresa(models.Model):
     _name = 'facturas.empresa'
     _description = 'Modelo de empresa'
     _rec_name= 'namep'
    #datos propietario
     namep = fields.Char(string="Nombre Propietario", required=True)
     rutp = fields.Char(string="Rut Propietario", required=True)
     direccionp = fields.Char(string="Direccion Propietario",required=True)
     telefonop = fields.Char(string="Telefono Propietario",required=True)