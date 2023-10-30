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
    attendance_student_id = fields.Many2one('attandance.class', string='Attendance Student Id')
