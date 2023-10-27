from odoo import models, fields

class BuildingClass(models.Model):
    _name = 'lesson.class'
    _description = 'Lesson Class'

    #form
    lesson_id = fields.Char(string='NIM')
    lesson_name = fields.Char(string='Nama Pelajaran')
    total_learner_hours = fields.Integer(string='Total Jam Pelajaran')
