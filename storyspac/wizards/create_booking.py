from odoo import fields,api,models,_

class CreateBooking(models.TransientModel):
    _name = 'create_booking'

    user_id = fields.Many2one('storyspac_users',string='User')
    booking_date = fields.Date(string='Booking Date')

    #creating record from the code after clicking custom button
    def create_booking(self):
        vals={
            'user_id':self.user_id.id,
            'date':self.booking_date,
            'note':'create from the booking wizards',
        }
        self.env['storyspac_booking'].create(vals)
