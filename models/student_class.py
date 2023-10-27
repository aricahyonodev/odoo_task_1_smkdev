from odoo import models, fields

class StudentClass(models.Model):
    _name = 'student.class'
    _description = 'Student Class'

    #basic
    student_id = fields.Char(string='NIS')
    full_name = fields.Char(string='Nama Lengkap')
    gender = fields.Selection([('male', 'Laki-Laki'), ('female', 'Perempuan')], string='Jenis Kelamin')
    date_of_birth = fields.Date(string='Tanggal Lahir')
    address = fields.Text(string='Alamat')
    phone_number = fields.Char(string='Nomor Telepon')