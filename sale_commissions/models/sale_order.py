from odoo import models, api  
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        results = []
        for order in self:
            res = super(SaleOrder, order).action_confirm()
            results.append(res)

            salesperson = order.user_id.partner_id

            # Verificar si el vendedor tiene un porcentaje de comisión definido
            if not salesperson.commission_percentage:
                raise UserError("El vendedor '%s' no tiene un porcentaje de comisión definido en su ficha." % salesperson.name)

            commission_percent = salesperson.commission_percentage

            # Cálculo de la comisión: Monto_Venta * (Porcentaje / 100)
            commission_amount = order.amount_total * (commission_percent / 100.0)

            # Crear el registro de la comisión
            self.env['sale.commission'].create({
                'sale_id': order.id,
                'partner_id': salesperson.id,
                'commission_percentage': commission_percent,
                'commission_amount': commission_amount,
            })

        # Devolver el resultado de la confirmación; si solo hay uno, devolver su resultado, si no, devolver la lista
        if not results:
            return None
        if len(results) == 1:
            return results[0]
        return results
    