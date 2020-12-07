
from odoo import models, fields, api


class marca(models.Model):
    _name = 'flota.marca'
    
    tipo = fields.Char(string="Marca",required=True) 
    camiones_ids = fields.One2many(
        'flota.camion',
        'marca_id',
        string="marca")
    
    total_camiones = fields.Integer(string="Total de camiones", compute="_total_camiones")
    
    @api.one
    def _total_camiones(self):
        self.total_camiones = len(self.camiones_ids)
    
    
class modelo(models.Model):
    _name = 'flota.modelo'
    
    tipo = fields.Char(string="Modelo",required=True) 
    camiones_ids = fields.One2many(
        'flota.camion',
        'modelo_id',
        string="modelo")
    
    total_camiones = fields.Integer(string="Total de camiones", compute="_total_camiones")
    
    @api.one
    def _total_camiones(self):
        self.total_camiones = len(self.camiones_ids)
        
        

class camion(models.Model):
    _name = 'flota.camion'

    
    marca = fields.Many2one('flota.marca',string='Marca')
    modelo = fields.Many2one('flota.modelo',string='Modelo')
    patente = fields.Char(string='patente', required=True)
    chasis = fields.Integer(string='chasis')
    color = fields.Char(string='color', required=True)
    cilindrada = fields.Float(string='cilindrada')
    autonomia = fields.Float(string='autonomia')
    año = fields.integer(string='año')
    kilometraje = fields.Integer(string='kilometraje', required=True)
    