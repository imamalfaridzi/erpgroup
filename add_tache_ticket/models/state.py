# Copyright 2016-2017 Akretion (http://www.akretion.com)
# Copyright 2016-2017 Camptocamp (http://www.camptocamp.com/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import xml.etree.ElementTree as xee
from odoo import api, exceptions, fields, models, _
from datetime import datetime
from odoo.exceptions import AccessError, UserError, ValidationError

class HelpdeskTicketaddtask(models.Model):
    _inherit = 'helpdesk.ticket'



    def add_task(self):
      task = self.env['project.task']
      if self.project_id and self.user_id and self.name:
        c_task = task.create(
           {'project_id': self.project_id.id,
           'name':self.name,
           'user_id':self.user_id.id,
           'description':self.description,
            
            })
        self.task_id = c_task.id
      else:
         raise UserError('Verifier les champs : Titre, Projet, Assigné à ...')

