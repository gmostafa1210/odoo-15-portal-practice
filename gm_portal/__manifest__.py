# -*- encoding: utf-8 -*-
##############################################################
#                                                            #
#   G. Mostafa                                               #
#   Copyright (C) 2024 (https://gmostafa1210.github.io/)     #
#                                                            #
##############################################################

{
    'name': 'Portal Practice',
    'version': '15.0.1.0',
    'sequence': 1,
    'category': 'Portal',
    'summary': 'Portal Practice Summary',
    'description': """Portal Practice Description.""",
    'author': 'Golam Mostafa',
    'website': 'https://gmostafa1210.github.io/',
    'depends': [
        'base', 'portal',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/student_views.xml',
        # 'views/portal_template_views.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
