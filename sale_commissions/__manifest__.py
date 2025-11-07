{
    'name': "Comisiones de Venta",
    'version': '0.1',
    'summary': 'Módulo para la gestión automática de comisiones de venta.',
    'description': """
        Permite definir un porcentaje de comisión por vendedor y
        genera automáticamente el registro de la comisión al confirmar una venta.
    """,
    'author': "Douglas Guzman",
    'category': 'Sales',
    'depends': ['base', 'sale'], # Depende de los módulos base y de venta
    'data': [
        'security/ir.model.access.csv',

        # Vistas y menú
        'views/res_partner_views.xml',
        'views/sale_commission_views.xml',
        'views/menu.xml',

        # Reportes
        'reports/report_sale_commission_template.xml',
        'reports/report.xml',
    ],
    'installable': True,
    'application': False,
}


