from odoo import models


class Base(models.AbstractModel):
    _name = 'loan.base'
    _description = 'Base Model for Loan Management'


    # receiver
    # receptor   
    name = models.CharField(string='Proposal Name', required=True)
    amount = models.Float(string='Amount', required=True)
    term = models.Integer(string='Term (months)', required=True)