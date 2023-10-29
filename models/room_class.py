from odoo import models, fields

class RoomClass(models.Model):
    _name = 'room.class'
    _description = 'Room Class'
 
    name = fields.Char(string='Kode Ruangan')
    room_name = fields.Char(string='Nama Ruangan')
    room_capacity = fields.Integer(string='Kapasitas')

    #relation
    # building_ids = fields.One2many('building.class', 'room_building_id',string='Gedung')
    # building_id = fields.Many2one('building.class',string='Gedung')
    building_ids = fields.One2many('building.line', 'room_id',string='Gedung')
    building_id = fields.Char(string='Nama Gedung', related='building_ids.building_line_id.name')
    building_name = fields.Char(string='Nama Gedung', related='building_ids.building_line_id.building_name')

  

    # building_line_ids = ma('building.line', 'building_line_id', string='Building')
    # building_name = fields.Integer(string='Nama Gedung', related='building_line_id.building_name')
   