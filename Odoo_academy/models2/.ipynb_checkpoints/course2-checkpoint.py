#-*- coding: utf- 8 -*-
from odoo import  models, fields, api

class Course2(models.Model):
    
    _name = 'academy.course2'
    _description = 'Course2 info'
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    level =fields.Selection(string='Level',
                           selection =[('beginner','Beginner'),
                                       ('intermediate','Intermediate'),
                                       ('advanced','Advanced')],
                           copy=False)
    
    active = fields.Boolean(string='Active', default='True')