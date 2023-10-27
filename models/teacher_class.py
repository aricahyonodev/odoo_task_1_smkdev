from odoo import models, fields

class TeacherClass(models.Model):
    _name = 'teacher.class'
    _description = 'Teacher Class'

    #basic
    teacher_id = fields.Char(string='NIP')
    full_name = fields.Char(string='Nama Lengkap')
    gender = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    date_of_birth = fields.Date(string='Tanggal Lahir')
    address = fields.Text(string='Alamat')
    phone_number = fields.Char(string='Nomor Telepon')