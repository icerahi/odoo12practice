from odoo import models,api,fields,_


class StoyspacBooking(models.Model):
    _name='storyspac_booking'
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = 'Storyspac Booking Model'

    serial = fields.Char(string='Booking Serial',index=True,readonly=True,copy=False,
                         required=True,default=lambda self:_('New'))

    user_id = fields.Many2one('storyspac_users',string='User Name',required=True)
    age = fields.Integer(string='Age',related='user_id.age')
    date = fields.Date(string='Booking date',required=True)
    note = fields.Text(string='Booking note')
    facalities = fields.Text(string='Facalities')
    doctor_id = fields.Many2one('storyspac_doctor',string='Doctor')

    booking_lines = fields.One2many('storyspac_booking.lines','booking_id',string='Booking Lines')

    state = fields.Selection([
        ('draft','Draft'),
        ('confirm','Confirm'),
        ('done','Done'),
        ('cancel','Cancelled')
    ],string='status',readonly=True,default='draft')

    def confirm_button(self):
        for f in self:
            f.state='confirm'
    def done_button(self):
        for f in self:
            f.state='done'
    def cancel_button(self):
        for f in self:
            f.state='draft'

    @api.model
    def create(self, vals_list):
        if vals_list.get('serial',_('New'))=='New':
            vals_list['serial']=self.env['ir.sequence'].next_by_code('storyspac_booking.serial') or _('New')
        result=super(StoyspacBooking, self).create(vals_list)
        return result


#lines
class StoryspacBookingLines(models.Model):
    _name='storyspac_booking.lines'
    _description = 'Booking lines'

    product_id = fields.Many2one('product.product',string='Medicine')
    product_qty = fields.Integer(string='Quantity')
    booking_id = fields.Many2one('storyspac_booking',string='Booking ID')
