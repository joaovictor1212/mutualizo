# -*- coding: utf-8 -*-

from odoo import fields, _, api, models
from odoo.exceptions import ValidationError, UserError





class AccountMove(models.Model):
    _inherit = "account.move"
    
    
    currency_id = fields.Many2one(comodel_name='res.currency', string="Moeda Transação")
    
    
    @api.model
    def create(self, vals):
        currency_exchange_ids = []
        res = super(AccountMove, self).create(vals)
        if 'currency_id' in vals:
            
            if res.company_id and res.company_id.currency_id != res.currency_id:
                currency_exchange_ids = self.env['account.foreign.exchange.rate'].search([])
            
                if currency_exchange_ids:
                    for currency_exchange_id in currency_exchange_ids:
                        
                        if currency_exchange_id.currency_to_id == res.currency_id:
                            res.currency_id = currency_exchange_id.currency_from_id
                            res.amount_total = res.amount_total * currency_exchange_id.exchange_rate
                            res.amount_untaxed = res.amount_untaxed * currency_exchange_id.exchange_rate
                        
                        else:
                            raise ValidationError("A moeda selecionada não tem taxa de conversão cadastrada.")
                else:
                    raise ValidationError("Necessário cadastrar as taxas de câmbio, para faturas com moeda diferente da companhia.")
                    
        
        return res
