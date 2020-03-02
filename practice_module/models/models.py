# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError

class StoryspacInherit(models.Model):
    _inherit = 'storyspac_users'

    country = fields.Char(string='Country')




class practice_module(models.Model):
    _name = 'practice_module.practice_module'
    #_rec_name = 'description'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Name',track_visibility='always')
    description = fields.Text(string='Description')
    profession = fields.Selection([('programmer','Programmer'),('designer','Designer'),('other','Other')],compute='set_profession',track_visibility='always')

    seq = fields.Char(string='Order Sequence',required=True,readonly=True,copy=False,index=True,
                      default=lambda self: ('New'))
    skills = fields.Selection([('java','Java'),('python','Python'),('photoshop','Photoshop')],string='Skills')
    total_ticket = fields.Integer(string='total_ticket',compute='user_total_ticket')
    @api.constrains('profession')
    def check_profession(self):
        for f in self:
            if f.profession == 'other':
                ValidationError("You can't set you profession other")

    @api.depends('skills')
    def set_profession(self):
        for f in self:
            if f.skills:
                if f.skills == 'java' or 'python' :
                    f.profession='programmer'
                if f.skills == 'photoshop':
                    f.profession='designer'

    @api.model
    def create(self, vals_list):
        if vals_list.get('seq',('New'))=="New":
            vals_list['seq']=self.env['ir.sequence'].next_by_code('practice_module.sequence') or ('New')
        result=super(practice_module, self).create(vals_list)

        return result

    def user_total_ticket(self):
        ticket=self.env['practice_module.ticket'].search_count([('name','=',self.id)])
        self.total_ticket=ticket

    @api.multi
    def user_ticket(self):
        return {
            'name':'User Ticket',
            'domain':[('name','=',self.id)],
            'view_type':'form',
            'view_mode':'tree,form',
            'res_model':'practice_module.ticket',
            'type':'ir.actions.act_window',
        }