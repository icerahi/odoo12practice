# -*- coding: utf-8 -*-
from odoo import http

# class PracticeModule(http.Controller):
#     @http.route('/practice_module/practice_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/practice_module/practice_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('practice_module.listing', {
#             'root': '/practice_module/practice_module',
#             'objects': http.request.env['practice_module.practice_module'].search([]),
#         })

#     @http.route('/practice_module/practice_module/objects/<model("practice_module.practice_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('practice_module.object', {
#             'object': obj
#         })