# -*- coding: utf-8 -*-

from odoo import fields, _, api, models
from odoo.exceptions import ValidationError, UserError





class AccountMove(models.Model):
    _inherit = "account.move"
    
    
    currency_id = fields.Many2one(comodel_name='res.currency', string="Moeda Transação")