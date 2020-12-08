
from odoo import models, fields, api


class marca(models.Model):
    _name = 'flota.marca'
    
    marca = fields.Char(string="Marca",required=True) 
    camiones_ids = fields.One2many(
        'flota.camion',
        'marca_id',
        string="MArcas")
    
    total_camiones = fields.Integer(string="Total de camiones", compute="_total_camiones")
    
    @api.one
    def _total_camiones(self):
        self.total_camiones = len(self.camiones_ids)
    
    
class modelo(models.Model):
    _name = 'flota.modelo'
    
    modelo = fields.Char(string="Modelo",required=True) 
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

    
    marca_id = fields.Many2one('flota.marca',string='Marca')
    modelo_id = fields.Many2one('flota.modelo',string='Modelo')
    patente = fields.Char(string='Patente', required=True)
    chasis = fields.Integer(string='Chasis')
    color = fields.Char(string='Color', required=True)
    cilindrada = fields.Float(string='Cilindrada')
    autonomia = fields.Float(string='Autonomía')
    año = fields.Integer(string='Año')
    kilometraje = fields.Integer(string='Kilometraje', required=True)
    