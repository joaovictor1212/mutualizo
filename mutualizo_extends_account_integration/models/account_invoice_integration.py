from odoo import models, api, _ , fields, http
from odoo.exceptions import ValidationError, UserError
from datetime import datetime, date


class AccountInvoiceIntegration(models.Model):
    _name = 'account.invoice.integration'
    _description = 'Invoice Integration'
    _rec_name = 'invoice_id'



    invoice_id = fields.Many2one(comodel_name="account.move", string='Fatura')

    external_system_id = fields.Char(string="External ID")

    status = fields.Selection(selection=[('pending','Pendente'),('sucess','Sucesso'),('error','Erro')], string="Status")

    response_message = fields.Text(string="Resposta")

