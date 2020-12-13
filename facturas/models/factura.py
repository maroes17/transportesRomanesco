# -*- coding: utf-8 -*-

from odoo import models, fields, api

class FacturaPrueba(models.Model):
     _name = 'facturas.factura'
     _description = 'Modelo de factura'
     _rec_name= 'id'
     #FECHA DE FACTURACIÓN 

     fecha = fields.Date("Fecha de Facturacion")

     ##FORANEAS
     field_empresa = fields.Many2one('facturas.empresa', string="Datos de empresa")

     field_cliente = fields.Many2one('facturas.cliente', string="Datos del cliente")

     #METODO DE PAGO
     
     metodo = fields.Many2one('facturas.metodo', string="Metodo de pago")

     #DESCRIPCION PRODUCTO O SERVICIO

     

     descriptionproduct = fields.Many2one('viajes.hojaderuta', string="Producto")

     #PRECIO CALCULOS

     precio = fields.Integer(string="Precio")

    

     @api.multi
     def compute_iva(self):
          self.iva = self.precio * 0.19
     
     iva = fields.Float('IVA', compute= compute_iva)


     def compute_total(self):
          self.preciototal = self.precio + self.iva

     preciototal = fields.Float('Precio Total', compute= compute_total)

  
     




   




