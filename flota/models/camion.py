
from odoo import models, fields, api


class marca(models.Model):
    _name = 'flota.marca'
    _rec_name = 'marca'
    _description = 'Marcas de camiones'
    
    marca = fields.Char(string="Marca",required=True) 
    camiones_ids = fields.One2many(
        'flota.camion',
        'marca_id',
        string="Marcas")
    
    total_camiones = fields.Integer(string="Total de camiones", compute="_total_camiones")
    
    @api.one
    def _total_camiones(self):
        self.total_camiones = len(self.camiones_ids)
    
         

class camion(models.Model):
    _name = 'flota.camion'
    _rec_name = 'patente'
    _description = 'Modelo de Camión'

    patente = fields.Char(string='Patente', required=True)
    marca_id = fields.Many2one('flota.marca',string='Marca')
    modelo = fields.Char(string='Modelo', required=True)
    
    color = fields.Char(string='Color')
    cilindrada = fields.Float(string='Cilindrada (cc)')
    autonomia = fields.Float(string='Autonomía (kms)')
    chasis = fields.Integer(string='Número de chasis', required=True)
    año = fields.Integer(string='Año')
    kilometraje = fields.Integer(string='Kilometraje', required=True)
    
    image = fields.Binary(string='Imagen')
    