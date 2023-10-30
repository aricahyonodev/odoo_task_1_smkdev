from odoo import models, fields, api

class BuildingClass(models.Model):
    _name = 'building.class'
    _description = 'Building Class'

    #form
    name = fields.Char(string='Kode Bangunan',)
    building_name = fields.Char(string='Nama Bangunan')
    number_of_rooms = fields.Integer(string='Total Ruangan')
    number_of_floors = fields.Integer(string='Total Lantai')
   
    #relations
    building_line_ids = fields.One2many('building.line', 'building_line_id', string="Building Line")

class BuildingLine(models.Model):
    _name = 'building.line'
    _description = 'Building Line'

    # relation
    building_line_id = fields.Many2one('building.class', string="Building")
    room_id = fields.Many2one('room.class', string="Room")
    room_name = fields.Char(string='Nama Ruangan', related='room_id.room_name')
    room_capacity = fields.Integer(string='Kapasitas', related='room_id.room_capacity')