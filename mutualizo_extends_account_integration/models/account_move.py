
from odoo import fields, _, api, models
from odoo.exceptions import ValidationError, UserError





class AccountMove(models.Model):
    _inherit = "account.move"


    def action_post(self):
        res = super(AccountMove, self).action_post()

        for record in self:
            if record:
                pass

        return res