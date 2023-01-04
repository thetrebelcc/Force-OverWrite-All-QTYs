# -*- coding: utf-8 -*-
# from odoo import http


# class Firstmod(http.Controller):
#     @http.route('/firstmod/firstmod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/firstmod/firstmod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('firstmod.listing', {
#             'root': '/firstmod/firstmod',
#             'objects': http.request.env['firstmod.firstmod'].search([]),
#         })

#     @http.route('/firstmod/firstmod/objects/<model("firstmod.firstmod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('firstmod.object', {
#             'object': obj
#         })
