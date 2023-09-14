from odoo import models, api, _ , fields, http
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, date


class AccountForeignExchangeRate(models.Model):
    _name = 'account.foreign.exchange.rate'
    _description = 'Foreingn Exchange Rate'
    _rec_name = 'formatted_date'
    
    
    
    date = fields.Date(string="Data da taxa de Câmbio")
    
    currency_from_id = fields.Many2one(comodel_name='res.currency', string='Moeda de origem')
    currency_to_id = fields.Many2one(comodel_name='res.currency', string='Moeda de destino')
    
    exchange_rate = fields.Float(string='Taxa de Câmbio', default=0.00)
    
    
    
    # Campo calculado para exibir a data no formato brasileiro padrão
    formatted_date = fields.Char(string='Data Formatada', compute='_compute_formatted_date')
    
    @api.depends('date')
    def _compute_formatted_date(self):
        for record in self:
            if record.date:
                formatted_date = record.date.strftime('%d/%m/%Y')  # Formata a data para string
                record.formatted_date = formatted_date
            else:
                record.formatted_date = ""