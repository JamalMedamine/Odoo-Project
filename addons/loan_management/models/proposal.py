from odoo import models
from . import base

class Proposal(base.Base):
    _name = 'loan.proposal'
    _description = 'Loan Proposal'
    
    
    interest_rate = models.Float(string='Interest Rate', required=True)
    status = models.Selection([
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft')