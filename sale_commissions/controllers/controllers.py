# from odoo import http


# class SaleCommissions(http.Controller):
#     @http.route('/sale_commissions/sale_commissions', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_commissions/sale_commissions/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_commissions.listing', {
#             'root': '/sale_commissions/sale_commissions',
#             'objects': http.request.env['sale_commissions.sale_commissions'].search([]),
#         })

#     @http.route('/sale_commissions/sale_commissions/objects/<model("sale_commissions.sale_commissions"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_commissions.object', {
#             'object': obj
#         })

