from odoo import fields, models, api, _
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
    ticket_number = fields.Char(string="Ticket Number")
    x_studio_text_field_qmex6 = fields.Char(string="Resolution")
    product_version = fields.Selection([('Odoo', 'Odoo'),
                                         ('UHH', 'UHH'),
                                         ('Netsuite', 'Netsuite'),
                                         ('Google', 'Google')], string="Product")

    @api.model
    def create(self, vals):
        common_seq = self.env['ir.sequence'].next_by_code('helpdesk.ticket')
        if vals.get('product_version') == 'Odoo':
            od_seq = self.env['ir.sequence'].next_by_code('seq_odoo_support_ticket')
            vals['ticket_number'] = 'OD' + str(common_seq) + str(od_seq)
        if vals.get('product_version') == 'UHH':
            uhh_seq = self.env['ir.sequence'].next_by_code('seq_uhh_support_ticket')
            vals['ticket_number'] = 'UH' + str(common_seq) + str(uhh_seq)
        if vals.get('product_version') == 'Netsuite':
            ns_seq = self.env['ir.sequence'].next_by_code('seq_netsuite_support_ticket')
            vals['ticket_number'] = 'NS' + str(common_seq) + str(ns_seq)
        if vals.get('product_version') == 'Google':
            go_seq = self.env['ir.sequence'].next_by_code('seq_google_support_ticket')
            vals['ticket_number'] = 'GO' + str(common_seq) + str(go_seq)
        res = super(HelpdeskTicket, self).create(vals)
        return res

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

