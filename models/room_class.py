from odoo import models, fields

class RoomClass(models.Model):
    _name = 'room.class'
    _description = 'Room Class'

    #form
    room_id = fields.Char(string='NIR')
    room_name = fields.Char(string='Nama Lengkap')
    capacity = fields.Integer(string='Kapasitas')
