# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'AWB Support',
    'version' : '15.1',
    'summary': 'AWB Support',
    'sequence': 10,
    'description': """
HELPDESK
====================
AWB Support """,
    'category': 'Support',
    'depends' : ['helpdesk','website_helpdesk_form'],
    'data': [
        'views/helpdesk_ticket_view.xml',
        #'views/helpdesk_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
