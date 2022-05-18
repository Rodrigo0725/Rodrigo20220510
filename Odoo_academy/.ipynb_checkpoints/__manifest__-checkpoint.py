# -*- coding utf-8 -*-

{
    'name': 'Odoo Academy',
    
    'summary': """Academy app to manage Training""",
    
    'description': """"
        Academy Module to app manage Training:7
        - Courses
        - Sessions
        - Attendees
    """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Trining',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data':[
        'security/academy_security.xml',
        'security/ir.model.access.csv',
    ],
    
    'demo':[
        'demo/academy_demo.xml',
    ],
}