
from odoo import models, fields, api

class Costos(models.Model):
    _name = 'viajes.gastos'
    _rec_name = 'id_viaje'

    id_viaje = fields.Many2one('viajes.hojaderuta', string='N° de viaje', required=True)
    moneda = fields.Selection([('EU', 'Euro'), ('CLP', 'Peso Chileno'),
                             ('USD', 'Dolar')], string='Moneda', required=True)
    chofer = fields.Many2one(sitring='Chofer', comodel_name='res.partner')
    fecha = fields.Datetime('Fecha', related='id_viaje.fecha')
    ruta_id = fields.Many2one('viajes.trayecto', string='Ruta', required=True)
    notas_viajes = fields.Text(string='Notas')
    
