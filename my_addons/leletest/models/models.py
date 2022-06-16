# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api


class Students(models.Model):
    _name = "leletest.students"
    _description = "leletest 学生信息表"
    
    name = fields.Char(string="姓名")
    sex = fields.Selection([("woman",'女'),('nan','男')], string="性别")
    age = fields.Integer(string="年龄")
    national_id = fields.Many2one('models.Models', string="民族")
    phone = fields.Char(string="手机号")
    qq = fields.Char(string="QQ号码")
    wechat = fields.Char(string="微信")
    ssn = fields.Char(string="身份证号码")

class Nationals(models.Models):
    _name = "leletest.nationals"
    _description = "leletest 民族列表"
    name = fields.Char(string="名称")
    student_id = fields.One2Many('leletest.students', string="学生")


# class leletest(models.Model):
#     _name = 'leletest.leletest'
#     _description = 'leletest.leletest'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
