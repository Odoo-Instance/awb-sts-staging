# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'AWB Support Ticketing System',
    'summary': "AWB Support Ticketing System Custom",
    'version': '15.0.1.0.0',
    'author': "Achieve Without Borders, Inc.",
    'website': "https://www.achievewithoutborders.com/",
    'description': """
HELPDESK
====================
AWB Support Ticketing System """,
    'category': 'Support',
    'depends': ['helpdesk', 'website_helpdesk_form'],
    'data': [
        'views/helpdesk_ticket_view.xml',
        'views/helpdesk_templates.xml',
        #'views/helpdesk_templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
