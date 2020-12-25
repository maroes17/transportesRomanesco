from odoo import models, fields, api

class tipoGasto(models.Model):
    _name = 'flota.tipo_gasto'
    _rec_name = 'tipo'
    _description = 'Tipos de Gasto'
    tipo = fields.Char(string="Tipo") 
    

class gastocamion(models.Model):
    _name = 'flota.gastocamion'
    _rec_name = 'tipo_gasto_id'
    _description = 'Modelo de Gastos de los camiones'
    
    
    camion_id = fields.Many2one('flota.camion', string="Patente del camion")
    
    tipo_gasto_id = fields.Many2one('flota.tipo_gasto',string='Tipo de Gasto')
    
    moneda = fields.Selection([('EU', 'Euro'), ('CLP', 'Peso Chileno'),
                             ('USD', 'Dolar')], string='Moneda', required=True)
    precio = fields.Float(string='Precio', required=True)
    fecha = fields.Date(string='Fecha', required=True)
    comentario = fields.Text(string='Comentario')