from odoo import fields, models, api
from odoo.exceptions import UserError, AccessError

# class HelpdeskTicket(models.Model):
#     _inherit = 'helpdesk.ticket'
#
#     priority_level = fields.Selection(string="Priority", selection=[('trivial', 'Trivial'), ('minor', 'Minor'), ('major', 'Major'), ('critical', 'Critical')])
#     product = fields.Selection(string="Product", selection=[('odoo', 'Odoo'), ('uhh', 'UHH'), ('netsuite', 'Netsuite'), ('google', 'Google')])
#     resolution = fields.Text(string="Resolution")


class HelpdeskStage(models.Model):
    _inherit = 'helpdesk.stage'

    legend_blue = fields.Char('Blue Kanban Label', translate=True)


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'


    kanban_state = fields.Selection(selection_add=[('blue', 'Blue')], string='Kanban State',
                                    ondelete={'blue': lambda recs: recs.write({'kanban_state': 'exist'})})
    legend_blue = fields.Char(related='stage_id.legend_blue', string='Kanban Completed Explanation', readonly=True,
                                related_sudo=False)

    @api.depends('stage_id', 'kanban_state')
    def _compute_kanban_state_label(self):
        for ticket in self:
            if ticket.kanban_state == 'normal':
                ticket.kanban_state_label = ticket.legend_normal
            elif ticket.kanban_state == 'blocked':
                ticket.kanban_state_label = ticket.legend_blocked
            elif ticket.kanban_state == 'blue':
                ticket.kanban_state_label = ticket.legend_blue
            else:
                ticket.kanban_state_label = ticket.legend_done

