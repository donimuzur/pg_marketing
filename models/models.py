from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
import logging
import base64
import os

_logger = logging.getLogger(__name__)

class MasterAreaProfile(models.Model):
    _name = 'master.area'
    _description = 'Master Area Profile'
    
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
   
 
class DbKios(models.Model):
    _name = 'db.kios'
    _description = 'Database Kios'
    
    name= fields.Char(string='Kios Name')
    kios_id = fields.Char(string='Kios ID')
    kios_address = fields.Char(string='Kios Address')
    kios_owner = fields.Char(string='Kios Address')
    kios_tlpn = fields.Char(string='No Telfn')
    kios_npwp = fields.Char(string='No NPWP')
    kios_namanpwp = fields.Char(string='Nama NPWP')
    kios_koordinat = fields.Char(string='Koordinat')
    kios_emp = fields.Char(string='Kios Employee')
    kios_supervisor = fields.Char(string='Kios Supervisor')
    area_id = fields.Many2one('master.area', required=True,
                                 store=True,
                                 index=False
                                 )