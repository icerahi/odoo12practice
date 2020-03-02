from odoo import fields,api,models,_
from odoo.exceptions import ValidationError


class Ticket(models.Model):
    _name='practice_module.ticket'
    _description = 'Ticket'
    _inherit = ['mail.activity.mixin','mail.thread']
    _order = 'id desc'

    serial = fields.Char(string='Serial',index=True,copy=False,readonly=True,required=True,
                         default=lambda self:_('New'))
    name = fields.Many2one('practice_module.practice_module',string='Name',required=True)
    age = fields.Integer(string='Age')
    age_group = fields.Selection([('boro','Boro'),('choto','Choto'),('buro','Buro')],compute='set_age_group')

    ticket_lines = fields.One2many('ticket.lines','ticket_id',string='Ticket Lines')
    @api.constrains('age')
    def check_age(self):
        for f in self:
            if f.age:
                if f.age<5:
                    ValidationError('Age must be large then 5 !')

    @api.depends('age')
    def set_age_group(self):
        for f in self:
            if f.age:
                if f.age <= 18:
                    f.age_group='choto'
                if 18<f.age <=40:
                    f.age_group='boro'
                if f.age>40:
                    f.age_group='buro'

    @api.model
    def create(self, vals_list):
        if vals_list.get('serial',_('New')) == 'New':
            vals_list['serial']=self.env['ir.sequence'].next_by_code('ticket.sequence') or _('New')
        result=super(Ticket, self).create(vals_list)
        return result


class TicketLines(models.Model):
    _name = 'ticket.lines'
    _description = 'Ticket Lines'

    seat_type = fields.Selection([('sovon','Sovon'),('s_char','S_Chair'),('ac','AC')],string='Seat Type')
    qty = fields.Integer(string='Quantity')
    ticket_id = fields.Many2one('practice_module.ticket',string='Ticket ID')