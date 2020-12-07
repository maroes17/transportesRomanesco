from odoo import models, fields, api

class TipoDocumento(models.Model):
    _name = 'flota.tipo_documento'
    
    tipo = fields.Char(string="Tipo",required=True) 
    chofer_ids = fields.One2many(
        'flota.chofer',
        'tipo_documento_id',
        string="documentos")
    
    total_chofer = fields.Integer(string="Total de conductores", compute="_total_conductores")
    
    @api.one
    def _total_conductores(self):
        self.total_chofer = len(self.chofer_ids)
    

class ciudadChofer(models.Model):
    _name = 'flota.ciudad_chofer'

    nombre = fields.Char(string='nombre', required=True)
    chofer_ids = fields.One2many(
        'flota.chofer',
        'ciudad_id',
        string='ciudades'
    )
    
    total_chofer = fields.Integer(string="Total de conductores", compute="_total_conductores")
    
    @api.one
    def _total_conductores(self):
        self.total_chofer = len(self.chofer_ids)

class chofer(models.Model):
    _name = 'flota.chofer'

    
    nombre = fields.Char(string='nombre', required=True)
    tipo_documento_id = fields.Many2one('flota.tipo_documento',string="Tipo de Documento")
    num_documento = fields.Char(string='num_documento', required=True)
    
    ciudad_id = fields.Many2one('flota.ciudad_chofer',string='Ciudad')
    telefono = fields.Integer(string='telefono')