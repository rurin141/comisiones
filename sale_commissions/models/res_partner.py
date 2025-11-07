from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # Campo para definir el porcentaje de comisión del vendedor.
    commission_percentage = fields.Float(
        string="Porcentaje de Comisión (%)",
        digits=(16, 2), 
        default=0.0,
        help="Porcentaje de comisión que recibirá el vendedor por sus ventas."
    )

 