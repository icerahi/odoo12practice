
from odoo import api,models,fields, _  
from odoo.exceptions import ValidationError

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    demo_name = fields.Char(string='Demo Name')


class StoryspacUsers(models.Model):
    _name='storyspac_users'
    _description='Storyspac Users '
    #_rec_name = 'date_of_birth'
    _inherit = ['mail.thread','mail.activity.mixin'] # for chatter
    _order = 'id desc'


    @api.constrains('age')
    def check_age(self):
        for f in self:
            if f.age<=5:
                raise ValidationError('The age must be bigger then 5!')

    @api.depends('age')
    def set_age_group(self):
        for f in self:
            if f.age:
                if f.age<18:
                    f.age_group='minor'
                else:
                    f.age_group='major'

    def set_default_gender(self):
        return 'male'



    name = fields.Char(string='Name',track_visibility='always')
    date_of_birth = fields.Date(string='Date Of Birth')
    bio = fields.Text(string='BIO')
    age = fields.Integer(string='Age', track_visibility='always')
    active = fields.Boolean(string='Active',default=True)
    salary = fields.Integer(string='Salary')
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')],default=set_default_gender)
    image = fields.Binary(string='Image',track_visibility='always')
    name_sec = fields.Char(string='Order Reference',required=True,copy=False,readonly=True,
                           index=True,default=lambda self: _('New'))
    age_group=fields.Selection([('minor','Minor'),('major','Major')],string='Age Group',compute='set_age_group')
    booking_count = fields.Integer(string='Booking',compute='get_booking_count')
    doctor_id = fields.Many2one('storyspac_doctor',string='Doctor')
    doctor_gender = fields.Selection([('male','Male'),('female','Female')],string='Doctor Gender')

    #display many2one field text customly with name and age
    def name_get(self):
        res =[]
        for f in self:
            res.append((f.id, '{} ({})'.format(f.name,f.age)))
        return res

    @api.onchange('doctor_id')
    def set_doctor_gender(self):
        for f in self:
            if f.doctor_id:
                f.doctor_gender=f.doctor_id.gender

    def get_booking_count(self):
        count=self.env['storyspac_booking'].search_count([('user_id','=',self.id)])
        self.booking_count=count


    @api.multi
    def open_user_booking(self):
        users=self.env['res.users'].search([('active','=',True)])
        users=[user.id for user in users]
        print(users)

        return {
            'name': 'User Booking',
            'res_model': 'storyspac_booking',
            'domain': [('user_id','=',self.id)],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }

    @api.model
    def create(self, vals):
        if vals.get('name_sec',_('New'))==('New'):
            vals['name_sec'] = self.env['ir.sequence'].next_by_code('storyspac_users.sequence') or _('New')
        result=super(StoryspacUsers, self).create(vals)
        return result








