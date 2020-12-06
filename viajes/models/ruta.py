# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class HojaDeRuta(models.Model):
    _name = 'viajes.hojaderuta'
    _rec_name = 'id_viaje'

    descripcion = fields.Char(string='Descripción')
    id_viaje = fields.Char(string='N° de viaje', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    cliente = fields.Char(string='Cliente')
    direccion_salida = fields.Char(string='Dirección salida')
    direccion_llegada = fields.Char(string='Direccion llegada')
    carga = fields.Char(string='Punto de carga')
    descarga = fields.Char(string='Punto de descarga')
    chofer = fields.Many2one(sitring='Chofer', comodel_name='res.partner')
    fecha = fields.Datetime(string='Fecha')
    tipo_carga = fields.Selection([('R', 'Remolque'), ('SR', 'Semirremolque'),
                             ('S', 'Sin remolque')], string='Tipo', required=True)
    estado = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string='Image')


    def toggle_state(self):
        self.estado = not self.estado

    @api.model
    def create(self, vals):
        if vals.get('id_viaje', _('New')) == _('New'):
            vals['id_viaje'] = self.env['ir.sequence'].next_by_code('viajes.hojaderuta.sequence') or _('New')
        result = super(HojaDeRuta, self).create(vals)
        return result 

# class viajes(models.Model):
#     _name = 'viajes.viajes'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
