from odoo import models, fields, api

class LessonClass(models.Model):
    _name = 'lesson.class'
    _description = 'Lesson Class'

    #lesson
    name = fields.Char(string='Kode Pelajaran')
    lesson_name = fields.Char(string='Nama Pelajaran')
    total_learner_hours = fields.Integer(string='Total Jam Pelajaran')

    #Room
    room_id = fields.Many2one('room.class', string='Kode Ruangan')
    room_name = fields.Char(string='Nama Ruangan', related='room_id.room_name')

    building_id = fields.Char(string='Kode Gedung', related='room_id.building_ids.building_line_id.name')
    building_name = fields.Char(string='Nama Gedung', related='room_id.building_ids.building_line_id.building_name')

    #Teacher
    teacher_id = fields.Many2one('teacher.class', string='Kode Guru')
    teacher_name = fields.Char(related='teacher_id.full_name', string='Nama Guru')
    
    #lesson line student
    lesson_line_ids = fields.One2many("lesson.line", "lesson_line_id", string="Lesson Line")
    total_student = fields.Char(string="Total Murid", compute="_compute_total_student")
    @api.depends("lesson_line_ids")
    def _compute_total_student(self):
        self.total_student = (len(self.lesson_line_ids))
        # self.total_student = "%s Murid" (str(len(self.lesson_line_ids)))

    # @api.onchange("partner_id")
    # def _onchange_partner_id(self):
    #     self.name = "Document for %s" % (self.partner_id.name)
    #     self.description = "Default description for %s" % (self.partner_id.name)
   

class LessonLine(models.Model):
    _name = 'lesson.line'
    _description = 'Lesson Line'

    lesson_line_id = fields.Many2one('lesson.class', string='Kode Pelajaran')
    student_id = fields.Many2one('student.class', string='Kode Murid')
    student_full_name = fields.Char(string='Nama Lengkap', related='student_id.full_name')
    student_phone_number = fields.Char(string='Nomor HP', related='student_id.phone_number')
    student_gender = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string='Jenis Kelamin', related='student_id.gender')
   