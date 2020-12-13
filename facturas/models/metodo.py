# -*- coding: utf-8 -*-

from odoo import models, fields, api


class metodoPago(models.Model):
     _name = 'facturas.metodo'
     _description = 'Modelo de metodos de pago'
     _rec_name= 'namem'
    #datos cliente
     namem = fields.Char(string="Metodo",required=True)
    