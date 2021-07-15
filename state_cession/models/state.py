# Copyright 2016-2017 Akretion (http://www.akretion.com)
# Copyright 2016-2017 Camptocamp (http://www.camptocamp.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import xml.etree.ElementTree as xee
from odoo import api, exceptions, fields, models, _
from datetime import datetime

class cedeAffcession(models.Model):
    _inherit = 'account.move'

    state2 = fields.Selection(selection=[
            ('normal', 'Normal'),
            ('cede', 'Cédé'),
        ], string='Status cession', tracking=True,
        default='normal')
