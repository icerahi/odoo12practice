
{
    'name': "StorySpac",

    'summary': """
        Custom Odoo module for Initial practice by Rahi""",

    'description': """
        Simple working for practice and learning
    """,

    'author': "Rahi",
    'website': "https://www.fb.com/icerahi/",
    'category': 'Tools',
    'version': '1.0',
    'depends': [
        'base',
        'mail',
        'sale',
      
    ],
    'data': [
        'security/security.xml',
        'data/data.xml', # loading default data
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'wizards/create_booking.xml',
        'views/user.xml',
        'views/booking.xml',
        'views/doctor.xml',


    ],
    'license': "",
    'installable': True,
    'application': True,
    'sequence': 1,
}
