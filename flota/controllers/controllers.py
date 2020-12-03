# -*- coding: utf-8 -*-
from odoo import http

# class Flota(http.Controller):
#     @http.route('/flota/flota/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/flota/flota/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('flota.listing', {
#             'root': '/flota/flota',
#             'objects': http.request.env['flota.flota'].search([]),
#         })

#     @http.route('/flota/flota/objects/<model("flota.flota"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('flota.object', {
#             'object': obj
#         })