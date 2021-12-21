import base64
import threading

from odoo import models, fields, tools, api, _
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

    
        img_path = get_module_resource('base', 'static/img', 'company_image.png')

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
        res = super(DbKios,self).create(values)
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

    partner_latitude = fields.Float(string='Geo Latitude', digits=(16, 5))
    partner_longitude = fields.Float(string='Geo Longitude', digits=(16, 5))
    date_localization = fields.Date(string='Geolocation Date')
    
    # image: all image fields are base64 encoded and PIL-supported
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
    image_medium = fields.Binary("Medium-sized image", attachment=True,
        help="Medium-sized image of this contact. It is automatically "\
             "resized as a 128x128px image, with aspect ratio preserved. "\
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary("Small-sized image", attachment=True,
        help="Small-sized image of this contact. It is automatically "\
             "resized as a 64x64px image, with aspect ratio preserved. "\
             "Use this field anywhere a small image is required.")

    area_id = fields.Many2one('master.area', string='Kecamatan', required=True)

    province_name = fields.Char('Province', related='area_id.province_name')
    district_prov_name = fields.Char('District Province Name', related='area_id.district_prov_name')
    city_name = fields.Char('City Name', related='area_id.city_name')
    
