from odoo import fields, models


class Base(models.AbstractModel):
    _name = 'loan.base'
    _description = 'Base Model for Loan Management'


    # receiver
    # receptor   
    name = fields.Char(string='Proposal Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    term = fields.Integer(string='Term (months)', required=True)