from odoo import models, fields, api

class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'

    #basic
    name = fields.Char(string='Kode Siswa')
    full_name = fields.Char(string='Nama Lengkap')
    gender = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    date_of_birth = fields.Date(string='Tanggal Lahir')
    address = fields.Text(string='Alamat')
    phone_number = fields.Char(string='Nomor Telepon')

    lesson_line_ids = fields.One2many('lesson.line', 'student_id',string='Lesson Id')
    # lesson_code = fields.Char(string='Kode Pelajaran', compute="_compute_total_student")
    # lesson_name = fields.Char(string='Nama Pelajaran', compute="_compute_total_student")
    
    # @api.depends("lesson_line_ids")
    # def _compute_total_student(self):
    #     for rec in self:
    #         rec.lesson_code = self.lesson_line_ids.lesson_line_id.name
    #         rec.lesson_name = self.lesson_line_ids.lesson_line_id.lesson_name
