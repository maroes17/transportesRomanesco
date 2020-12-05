
from odoo import models, fields, api

class Costos(models.Model):
    _name = 'viajes.gastos'
    _rec_name = 'id_viaje'

    id_viaje = fields.Many2one('viajes.hojaderuta', string='N° de viaje', required=True)
    moneda = fields.Selection([('EU', 'Euro'), ('CLP', 'Peso Chileno'),
                             ('USD', 'Dolar')], string='Moneda', required=True)
    chofer = fields.Many2one(sitring='Chofer', comodel_name='res.partner')
    fecha = fields.Datetime('Fecha', related='id_viaje.fecha')
    notas_viajes = fields.Text(string='Notas')
    id_direccion_salida = fields.Char('Dirección salida', related='id_viaje.direccion_salida')
    id_direccion_llegada = fields.Char('Direccion llegada', related='id_viaje.direccion_llegada')