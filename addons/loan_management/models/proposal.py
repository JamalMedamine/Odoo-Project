from odoo import fields, models
from . import base

class Proposal(base.Base):
    _name = 'loan.proposal'
    _description = 'Loan Proposal'
    
    
    interest_rate = fields.Float(string='Interest Rate', required=True)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')