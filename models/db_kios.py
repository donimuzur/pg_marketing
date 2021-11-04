from odoo import models, fields, api, _

 
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
    area_id = fields.Many2one('master.area', string='Kecamatan', required=True)

    province_name = fields.Char('Province', related='area_id.province_name')
    district_prov_name = fields.Char('District Province Name', related='area_id.district_prov_name')
    city_name = fields.Char('City Name', related='area_id.city_name')
    
    @api.model
    def create(self, values):
        area =  self.env['master.area'].search([('id', '=', values['area_id'])],limit=1)
        current_id = self.env['db.idgenerator'].search([('id', '=', 1)],limit=1)
        
        self.env.user.notify_info(current_id.number,'Hasil Penerimaan hari ini ', True)
        
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

        res = super(DbKios,self).create(values)
        return res