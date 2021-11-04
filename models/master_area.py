from odoo import models, fields, api, _

class MasterArea(models.Model):
    _name = 'master.area'
    _description = 'Master Area'
    
    zone_id = fields.Char(string='Zone ID')
    disrict_code= fields.Char(string='District Code')
    province_code= fields.Char(string='Province Code')
    province_name= fields.Char(string='Province Name')
    district_prov_code= fields.Char(string='District Province Code')
    district_prov_name= fields.Char(string='District Province Name')
    city_code= fields.Char(string='City Code')
    city_name= fields.Char(string='City Name')
    kec_code= fields.Char(string='Kecamatan Code')
    name = fields.Char(string='Kecamatan Name')
    num_villages= fields.Integer(string='No Of Villages', default='0')
    area_category= fields.Char(string='Area Category')
    farming_area= fields.Integer(string='Farming Area', default='0')
    corn_area=  fields.Integer(string='Corn Area', default='0')
    rice_area= fields.Integer(string='Rice Area', default='0')
    plantation_area= fields.Integer(string='Plantation Area', default='0')
    horticulture_area= fields.Integer(string='Horticulture Area', default='0')
    potential_market_area= fields.Integer(string='Potential Market Area', default='0')
   