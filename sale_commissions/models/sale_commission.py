from odoo import fields, models

class SaleCommission(models.Model):
    _name = 'sale.commission'
    _description = 'Registro de Comisiones de Venta'
    _order = 'date desc'

    name = fields.Char(
        string='Referencia',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('sale.commission') or 'Nuevo'
    )
    
    sale_id = fields.Many2one(
        'sale.order',
        string='Venta Relacionada', 
        required=True, 
        ondelete='cascade',
        readonly=True
    )
 
    partner_id = fields.Many2one(
        'res.partner',
        string='Vendedor',
        required=True,
        readonly=True
    )

    date = fields.Datetime(
        string='Fecha de Comisión',
        default=fields.Datetime.now,
        readonly=True
    )

    # Moneda se toma de la venta, o por defecto de la compañía
    currency_id = fields.Many2one(
        'res.currency',
        string='Moneda',
        related='sale_id.currency_id',
        store=True,
        readonly=True
    )

    amount_total = fields.Monetary(
        string='Monto Total de la Venta',
        currency_field='currency_id',
        related='sale_id.amount_total',
        readonly=True
    )

    commission_percentage = fields.Float(
        string='Porcentaje (%)',
        digits=(16, 2),
        readonly=True
    )

    # Monto total de la comisión
    commission_amount = fields.Monetary(
        string='Monto Total de la Comisión',
        currency_field='currency_id',
        readonly=True
    )

