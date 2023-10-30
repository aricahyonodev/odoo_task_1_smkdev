from odoo import fields, models, api    

class AttendanceClass(models.Model):
    _name = 'attendance.class'
    _description="Attendance Class"

    date_attendance = fields.Date(string="Tanggal Prensensi", default=fields.Date.today)
    attendance_lesson_id = fields.Many2one('lesson.class', string='Kode Pelajaran')
    lesson_name = fields.Char(string="Nama Pelajaran", related='attendance_lesson_id.lesson_name')
    #Lesson Guru
    lesson_teacher_code = fields.Char(string="Kode Guru", related='attendance_lesson_id.teacher_id.name')
    lesson_teacher_name = fields.Char(string="Nama Guru", related='attendance_lesson_id.teacher_name')
    #lesson Building
    lesson_room_code = fields.Char(string="Kode Ruangan", related='attendance_lesson_id.room_id.name')
    lesson_room_name = fields.Char(string="Nama Ruangan", related='attendance_lesson_id.room_name')
    lesson_building_code = fields.Char(string="Kode Gedung", related='attendance_lesson_id.building_id')
    lesson_building_name = fields.Char(string="Nama Gedung", related='attendance_lesson_id.building_name')
    presensi = fields.Char(string="Presensi")
    state = fields.Selection([('unfinished', 'Belum Selesai'), ('finished', 'Selesai')], string='State', default='unfinished')

   
    attendance_students = fields.One2many('student.class', 'attendance_student_id', string="Nama Murid", compute='_compute_student_name')
    @api.depends("attendance_lesson_id.lesson_line_ids.student_id")
    def _compute_student_name(self):
        for rec in self:
            rec.attendance_students = rec.attendance_lesson_id.lesson_line_ids.student_id

    #temp
    attendance_line_ids = fields.One2many('attendance.line', 'attendance_line_id', string="Attendance Line")


class AttendaceLine(models.Model):
    _name="attendance.line"
    _description="Attendance line"

    attendance_line_id = fields.Many2one('attendance.class', string="Kode Kehadiran")
    attendance_student_id = fields.Many2one('student.class', string="Student Name")
    attendance_status = fields.Selection([('absent', 'Tidak Hadir'),('attended', 'Hadir')], string='Status Kehadiran')
    attendance_reason = fields.Selection([('absent', 'Absen'),('sick','sakit'),('permit','izin')], string='Alasan')
