from odoo import models, fields, api

class DefectReasonWizard(models.TransientModel):
    _name = 'defect.reason.wizard'
    _description = 'Defect Reason Wizard'

    defect_reason = fields.Text(string='Defect Reason', required=True)
    order_id = fields.Many2one('website.order_model', string='Order', default=lambda self: self._context.get('active_id'))

    def action_confirm(self):
        self.ensure_one()
        order = self.order_id
        if order:
            order.write({
                'status': 'defected',
                'defect_reason': self.defect_reason
            })
        return {'type': 'ir.actions.act_window_close'}