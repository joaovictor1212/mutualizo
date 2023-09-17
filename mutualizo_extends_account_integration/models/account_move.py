
from odoo import fields, _, api, models
from odoo.exceptions import ValidationError, UserError
import requests
import json




class AccountMove(models.Model):
    _inherit = "account.move"


    def action_post(self):
        res = super(AccountMove, self).action_post()

        for record in self:
            if record:
                integration_data = {
                    'external_id' : record.id,
                }
            
             # Envie os dados para o sistema externo via API REST
            response = requests.post('URL_DO_SISTEMA_EXTERNO_API', json=integration_data)
            
            if response:
            # Atualize o registro no modelo account.invoice.integration
                integration_record = self.env['account.invoice.integration'].create({
                    'invoice_id': record.id,
                    'external_id': response.id,
                    'status': response.status_code,  # Status da resposta do sistema externo
                    'response_message': response.text  # Mensagem de resposta do sistema externo
                })

        return res