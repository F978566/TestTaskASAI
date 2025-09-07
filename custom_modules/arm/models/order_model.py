from enum import Enum
from odoo import fields, models
from odoo.api import UserError

class OrderStatus(Enum):
    READY_TO_WORK = "ready_to_work"
    READY = "ready"
    IN_PROGRESS = "in_progress"
    DEFECTED = "defected"

class OrderModel(models.Model):
    _name = "website.order_model"
    _description = "Order Model"
    
    name = fields.Char(
        string="name",
        required=True,
    )
    order_number = fields.Integer()
    create_date = fields.Datetime(
        string="Custom Creation Date",
        default=lambda _: fields.Datetime.now(), # type: ignore
        readonly=True,
    )
    description = fields.Char(
        string="description",
        required=False,
    )
    files = fields.Binary(
        string="Order Files",
        attachment=True,
    )
    status = fields.Selection(
        selection=[(status.value, status.name.title()) for status in OrderStatus], # type: ignore
        string="Order Status",
        default=OrderStatus.READY_TO_WORK.value,
        required=True,
    )
    file_name = fields.Char(
        string="File Name",
        help="Name of the uploaded file",
    )
    defect_reason = fields.Text(string='Defect Reason')
    
    def action_take_in_work(self):
        self.write({
            'status': 'in_progress',
        })

    def action_mark_ready(self):
        self.write({
            'status': 'ready',
        })

    def action_mark_defected(self):
        self.write({
            'status': 'defected',
        })
    
    def action_download_file(self):
        self.ensure_one()
        if not self.files:
            return False
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{self._name}/{self.id}/files/{self.file_name or "download"}?download=true',
            'target': 'self',
        }
    
    def action_show_description(self):
        self.ensure_one()
        if not self.description:
            raise UserError("No description available for this order.")
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': f'Description for {self.name}',
                'message': self.description if self.status != OrderStatus.DEFECTED.value else self.defect_reason,
                'type': 'info',  # Can be 'success', 'warning', 'info', 'danger'
                'sticky': True,  # Keeps the popup open until user closes it
            }
        }
    
    def action_mark_defected(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'defect.reason.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('arm.view_defect_reason_wizard_form').id,
            'target': 'new',
            'context': {'active_id': self.id},
        }

    def action_mark_ready_to_work(self):
        self.write({
            'status': 'ready_to_work',
        })