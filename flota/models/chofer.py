from odoo import models, fields, api

class TipoDocumento(models.Model):
    _name = 'flota.tipo_documento'
    _rec_name = 'tipo'
    _description = 'Tipo de documento de identificación'
    
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
    _rec_name = 'nombre'
    _description = 'Ciudades a las cuales pertenecen los conductores'

    nombre = fields.Char(string='Nombre', required=True)
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
    _rec_name = 'nombre'
    _description = 'Modelo de Chofer'

    
    nombre = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    
    tipo_documento_id = fields.Many2one('flota.tipo_documento',string="Tipo de Documento")
    num_documento = fields.Char(string='Número de Documento', required=True)
    ciudad_id = fields.Many2one('flota.ciudad_chofer',string='Ciudad')
    
    image = fields.Binary(string='Imagen')
    