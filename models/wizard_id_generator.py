from odoo import models, fields, api, _

class WizardIDGenerator(models.Model):
    _name = 'db.idgenerator'
    _description = 'ID Generator'

    name = fields.Char(string='City Code')
    number = fields.Integer(string='Number')
  