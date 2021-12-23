import base64
import threading

from odoo import models, fields, tools, api, _
from odoo.modules.module import get_module_resource
from odoo.exceptions import UserError, ValidationError
from odoo.tools import pycompat
 
class DbKios(models.Model):
    _name = 'db.kios'
    _description = 'Database Kios'
    
    
    @api.model
    def _get_default_image(self):
        if getattr(threading.currentThread(), 'testing', False) or self._context.get('install_mode'):
            return False

        colorize, img_path, image = False, False, False
        img_path = get_module_resource('pg_marketing', 'static/image', 'default_kios_img.jpg')

        if img_path:
            with open(img_path, 'rb') as f:
                image = f.read()
        if image and colorize:
            image = tools.image_colorize(image)

        return tools.image_resize_image_big(base64.b64encode(image))


    @api.model
    def create(self, values):
        area =  self.env['master.area'].search([('id', '=', values['area_id'])],limit=1)
        current_id = self.env['db.idgenerator'].search([('id', '=', 1)],limit=1)
               
        next_id = 1
        if current_id :
            next_id = current_id.number +1
            current_id.write({'number' : next_id})
        else :
            self.env.cr.execute('''
                insert into db_idgenerator (name, number)
                values ('%s', %s)
                ''' % (area.city_code, next_id) )
            self.env.cr.commit()

        number_str = str(next_id)
        values['kios_id'] = '%s%s' % (area.city_code, number_str.zfill(3) )
        if not values['image']:
                values['image'] = self._get_default_image()
        tools.image_resize_images(values, sizes={'image': (1024, None)})
        
        try:
            if not values['partner_latitude']:
                values['partner_latitude']= self.partner_latitude
        except:
            values['partner_latitude']= self.partner_latitude
        
        try:
            if not values['partner_longitude']:
                values['partner_longitude']= self.partner_longitude
        except:
            values['partner_longitude']= self.partner_longitude        
        
        values['map_url'] = 'https://maps.google.com/?ll=%s,%s' % (values['partner_latitude'],  values['partner_longitude'])
        res = super(DbKios,self).create(values)
        return res

    @api.multi
    def write(self, values):
        try:
            if not values['partner_latitude']:
                values['partner_latitude']= self.partner_latitude
        except:
            values['partner_latitude']= self.partner_latitude
        
        try:
            if not values['partner_longitude']:
                values['partner_longitude']= self.partner_longitude
        except:
            values['partner_longitude']= self.partner_longitude        
        
        values['map_url'] = 'https://maps.google.com/?ll=%s,%s' % (values['partner_latitude'],  values['partner_longitude'])
        res = super(DbKios, self).write(values)
        return res

    name= fields.Char(string='Kios Name')
    kios_id = fields.Char(string='Kios ID')
    kios_address = fields.Char(string='Kios Address')
    kios_owner = fields.Char(string='Kios Owner')
    kios_tlpn = fields.Char(string='No Telfn')
    kios_npwp = fields.Char(string='No NPWP')
    kios_namanpwp = fields.Char(string='Nama NPWP')
    kios_emp = fields.Char(string='Kios Employee')
    kios_supervisor = fields.Char(string='Kios Supervisor')
    active = fields.Boolean(default=True)

    partner_latitude = fields.Float(string='Geo Latitude', digits=(16, 10), default=0)
    partner_longitude = fields.Float(string='Geo Longitude', digits=(16, 10), default=0)
    date_localization = fields.Date(string='Geolocation Date')
    map_url = fields.Char(string='Maps Url')
    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)

    area_id = fields.Many2one('master.area', string='Kecamatan', required=True)

    province_name = fields.Char('Province', related='area_id.province_name')
    district_prov_name = fields.Char('District Province Name', related='area_id.district_prov_name')
    city_name = fields.Char('City Name', related='area_id.city_name')
    
    @api.one
    def btn_view_google_map(self):
        return {
            'type': 'ir.actions.act_url',
            'name':'btn_view_google_map',
            'url': "https://maps.google.com/?ll=0,0",
            'target': 'self'
        } 
    

