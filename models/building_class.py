from odoo import models, fields

class BuildingClass(models.Model):
    _name = 'building.class'
    _description = 'Building Class'

    #form
    building_id = fields.Char(string='NIB')
    building_name = fields.Char(string='Nama Bangunan')
    number_of_rooms = fields.Integer(string='Total Ruangan')
    number_of_floors = fields.Integer(string='Total Lantai')
