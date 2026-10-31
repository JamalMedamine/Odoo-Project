from odoo import fields, models


class Proposal(models.Model):
    _name = 'loan.proposal'
    _description = 'Loan Proposal'

    name = fields.Char(string='Proposal Name', required=True)
    amount = fields.Float(string='Amount', required=True)
    term = fields.Integer(string='Term (months)', required=True)
    interest_rate = fields.Float(string='Interest Rate', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')