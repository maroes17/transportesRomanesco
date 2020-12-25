
from odoo import models, fields, api

class Costos(models.Model):
    _name = 'viajes.gastos'
    _rec_name = 'id_viaje'
    _description = 'gastos de los viajes'

    moneda = fields.Selection([('EU', 'Euro'), ('CLP', 'Peso Chileno'),
                             ('USD', 'Dolar')], string='Moneda', required=True)
    chofer = fields.Many2one(sitring='Chofer', related ='id_viaje.id_chofer')
    fecha = fields.Datetime('Fecha', related='id_viaje.fecha')
    notas_viajes = fields.Text(string='Notas')
    viatico = fields.Float(string='Viatico')
    reembolso = fields.Float(string='Reembolso')
    prestamos = fields.Float(string='Préstamos')  
    otros = fields.Float(string='Otros gastos')
    combustible_efectivo = fields.Float(string='Combustible en efectivo')
    combustible_costo = fields.Float(string='Costo del combustible')
    combustible_litros = fields.Integer(string='Litros')
    ruta_id = fields.Many2one('viajes.trayecto', string='Ruta', required=True)
    id_viaje = fields.Many2one('viajes.hojaderuta', string='N° de viaje', required=True)

    @api.multi
    def compute_field(self):
        self.subtotal = self.viatico + self.reembolso + self.prestamos + self.otros + self.combustible_efectivo
        self.impuestos = self.subtotal * 0.19
        self.total = self.subtotal + self.impuestos
        self.combustible_subtotal = self.combustible_costo * self.combustible_litros
        self.combustible_impuestos = self.combustible_subtotal * 0.19
        self.combustible_total = self.combustible_impuestos + self.combustible_subtotal


    subtotal = fields.Float(string='Subtotal', compute = compute_field) 
    total = fields.Float(string='Total', compute = compute_field)
    impuestos = fields.Float(string='Impuestos', compute = compute_field)
    combustible_subtotal = fields.Float(string='Subtotal', compute = compute_field)
    combustible_impuestos = fields.Float(string='Impuestos', compute = compute_field)
    combustible_total = fields.Float(string='Total', compute = compute_field)


class ReporteGastos(models.AbstractModel):
    _name = 'report.viajes.report_gastos_card'

    @api.model
    def _get_report_values(self, docids, data=None):
        report_obj = self.env['ir.actions.report']
        report = report_obj._get_report_from_name('viajes.report_gastos_card')
        return {
            'doc_ids': docids,
            'doc_model': self.env['viajes.gastos'],
            'docs': self.env['viajes.gastos'].browse(docids)
        }


