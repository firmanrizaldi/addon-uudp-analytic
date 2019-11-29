# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UUDP(models.Model):
    _name = 'uudp'
    _inherit = 'uudp'


    location_id = fields.Many2one(
        string='Location',
        comodel_name='account.analytic.tag',
    )

    
    business_id = fields.Many2one(
        string='Business',
        comodel_name='account.analytic.tag',
    )
    
    