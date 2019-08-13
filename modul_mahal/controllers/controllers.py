# -*- coding: utf-8 -*-
from odoo import http

# class Fresh11(http.Controller):
#     @http.route('/fresh11/fresh11/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fresh11/fresh11/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fresh11.listing', {
#             'root': '/fresh11/fresh11',
#             'objects': http.request.env['fresh11.fresh11'].search([]),
#         })

#     @http.route('/fresh11/fresh11/objects/<model("fresh11.fresh11"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fresh11.object', {
#             'object': obj
#         })