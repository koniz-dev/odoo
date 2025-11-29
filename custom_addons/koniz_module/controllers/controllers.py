# from odoo import http


# class KonizModule(http.Controller):
#     @http.route('/koniz_module/koniz_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/koniz_module/koniz_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('koniz_module.listing', {
#             'root': '/koniz_module/koniz_module',
#             'objects': http.request.env['koniz_module.koniz_module'].search([]),
#         })

#     @http.route('/koniz_module/koniz_module/objects/<model("koniz_module.koniz_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('koniz_module.object', {
#             'object': obj
#         })

