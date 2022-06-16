# -*- coding: utf-8 -*-
# from odoo import http


# class Leletest(http.Controller):
#     @http.route('/leletest/leletest/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/leletest/leletest/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('leletest.listing', {
#             'root': '/leletest/leletest',
#             'objects': http.request.env['leletest.leletest'].search([]),
#         })

#     @http.route('/leletest/leletest/objects/<model("leletest.leletest"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('leletest.object', {
#             'object': obj
#         })
