from odoo import models, fields, api

class TipoGasto(models.Model):
    _name = 'flota.tipo_gasto'
    
    tipo = fields.Char(string="Tipo",required=True) 



class GastoCamion(models.Model):
    _name = 'flota.gastoCamion'
    
    moneda = fields.Selection([('EU', 'Euro'), ('CLP', 'Peso Chileno'),
                             ('USD', 'Dolar')], string='Moneda', required=True)
    
    tipo_gasto = fields.Many2one('flota.tipo_gasto',string="Tipo de Gasto")
    
    precio = fields.Float(string='precio', required=True)
    fecha = fields.Date(string='fecha', required=True)