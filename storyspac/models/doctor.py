from odoo import fields,api,models,_


class Doctor(models.Model):
    _name='storyspac_doctor'

    name=fields.Char(string='Name',required=True)
    gender = fields.Selection([('male','Male'),('female','Female')],default='male',string='Gender')
    user_id = fields.Many2one('res.users',string='Related User')


