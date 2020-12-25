# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HojaDeRuta(models.Model):
    _name = 'viajes.hojaderuta'
    _rec_name = 'id_viaje'

    descripcion = fields.Char(string='Descripción')
    id_viaje = fields.Char(string='N° de viaje', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    fecha = fields.Datetime(string='Fecha')
    tipo_carga = fields.Selection([('R', 'Remolque'), ('SR', 'Semirremolque'),
                             ('S', 'Sin remolque')], string='Tipo', required=True)
    estado = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Image')
    id_cliente = fields.Many2one('facturas.cliente', string="Cliente")
    id_chofer = fields.Many2one('flota.chofer', string="Chofer")
    id_camion = fields.Many2one('flota.camion', string="Camion")
    ruta = fields.Many2one('viajes.trayecto', string='Ruta', required=True)
    conteo_gastos = fields.Integer(string='Gastos Chofer', compute='get_conteo_gastos')

    # Función del botón estado
    def toggle_state(self):
        self.estado = not self.estado

    # Función de la secuencia, ingreso de viajes
    @api.model
    def create(self, vals):
        if vals.get('id_viaje', _('New')) == _('New'):
            vals['id_viaje'] = self.env['ir.sequence'].next_by_code('viajes.hojaderuta.sequence') or _('New')
        result = super(HojaDeRuta, self).create(vals)
        return result 

    # Función de botón Gastos
    @api.multi
    def open_ruta_costos(self):
        return {
            'name': _('Gastos por viajes'),
            'domain': [('id_viaje', '=', self.id)],
            'view_type': 'form', 
            'res_model': 'viajes.gastos',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',        
        }


class Direccion(models.Model):
     _name = 'viajes.direccion'
     _rec_name = 'nombre'
     nombre = fields.Char(string='Nombre', required=True)

class LugarDeCarga(models.Model):
     _name = 'viajes.lugar_carga'
     _rec_name = 'nombre'
     nombre = fields.Char(string='Nombre', required=True)


class Trayectos(models.Model):
    _name = 'viajes.trayecto'
    _rec_name = 'nombre'
    nombre = fields.Char(string='Nombre del trayecto')
    direccion_salida = fields.Many2one('viajes.direccion', string='Dirección salida')
    direccion_llegada = fields.Many2one('viajes.direccion', string='Direccion llegada')
    carga = fields.Many2one('viajes.lugar_carga', string='Punto de carga')
    descarga = fields.Many2one('viajes.lugar_carga', string='Punto de descarga')
    distancia = fields.Integer(string='Distancia KM')




    
