from odoo import models, fields, api, _


class DbPenjualan(models.Model):
    _name = 'db.penjualan'
    _description = 'Database Penjualan'

    name = fields.Many2one('db.kios', string='Kios Name', required=True)
    kios_address = fields.Char('Kios Address', related='name.kios_address')
    kec_name = fields.Char('Kecamatan Name', related='name.area_id.name')
    province_name = fields.Char('Province Name', related='name.area_id.province_name')
    emp_name = fields.Char(string='Employee Name')
    month = fields.Selection([
                        (1, 'January'),
                        (2, 'February'),
                        (3, 'March'),
                        (4, 'April'),
                        (5, 'Mey'),
                        (6, 'Juny'),
                        (7, 'July'),
                        (8, 'August'),
                        (9, 'Septmber'),
                        (10, 'October'),
                        (11, 'November'),
                        (12, 'December')
                        ],required=True)
    year = fields.Integer(string='Year',required=True)
    product= fields.Char(string='Product',required=True)
    stocks = fields.Integer(string='Stocks')
    sales = fields.Integer(string='Sales')

    