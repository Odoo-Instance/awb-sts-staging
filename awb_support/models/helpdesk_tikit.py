from odoo import fields, models, api


# class HelpdeskTicket(models.Model):
#     _inherit = 'helpdesk.ticket'
#
#     priority_level = fields.Selection(string="Priority", selection=[('trivial', 'Trivial'), ('minor', 'Minor'), ('major', 'Major'), ('critical', 'Critical')])
#     product = fields.Selection(string="Product", selection=[('odoo', 'Odoo'), ('uhh', 'UHH'), ('netsuite', 'Netsuite'), ('google', 'Google')])
#     resolution = fields.Text(string="Resolution")


class HelpdeskStage(models.Model):
    _inherit = 'helpdesk.stage'

    legend_blue = fields.Char('Blue Kanban Label', translate=True)

