from odoo import models, fields, api, SUPERUSER_ID
from uuid import uuid4

class BonConsum(models.TransientModel):
    _name = "bon.consum"
    
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date to")
    analytic_account_id = fields.Many2one(comodel_name="account.analytic.account")
    
    #generamos laccion del boton de impresion
    def action_print_report(self):
        consults = self.env["mrp.production"].search([])
        print(self.env.context)
        self.with_context(field1="test").Pruebcontexto()
        print("//////////////registros ////////////////",consults)
    
    def Pruebcontexto(self):
        print(self.env.context)