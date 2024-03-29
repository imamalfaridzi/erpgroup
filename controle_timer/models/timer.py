

from odoo.exceptions import Warning
from odoo import api, fields, models, _, SUPERUSER_ID
from odoo.exceptions import UserError



class ProjectTask_timer(models.Model):
    _inherit = 'project.task'

    # ---------------------------------------------------------
    # Timer Methods
    # ---------------------------------------------------------

    def action_timer_start(self):

        tasks = self.env["project.task"].search([('user_id','=',self.user_id.id)])
        check = False

        for task in tasks:
            if task.timesheet_timer_start != False and task.timesheet_timer_pause == False:
                check = True
        if check == False:

         self.ensure_one()
         if not self.timesheet_timer_first_start:
            self.write({'timesheet_timer_first_start': fields.Datetime.now()})
         return self.write({'timesheet_timer_start': fields.Datetime.now()})
        else:
            raise Warning("il y'a déja une tâche en cours !!")

    def action_timer_resume(self):

        tasks = self.env["project.task"].search([('user_id','=',self.user_id.id)])
        check = False

        for task in tasks:
            if task.timesheet_timer_start != False and task.timesheet_timer_pause == False:
                check = True
        if check == False:
          new_start = self.timesheet_timer_start + (fields.Datetime.now() - self.timesheet_timer_pause)
          self.write({
            'timesheet_timer_start': new_start,
            'timesheet_timer_pause': False
          })
        else:
            raise Warning("il y'a une tâche déja en cours !! ")
     

class Project_controle(models.Model):
    _inherit = "project.project"
    timesheet_timer_start = fields.Datetime("Timesheet Timer Start", compute="_timer_start")
    timesheet_timer_pause = fields.Datetime("Timesheet Timer Last Pause" , compute="_timer_pause")

    @api.depends('task_ids')
    def _timer_start(self):
        self.timesheet_timer_start = False
        if self.task_ids:
          for m in self.task_ids:
            if m.timesheet_timer_start: 
              self.timesheet_timer_start = m.timesheet_timer_start
            

    @api.depends('task_ids')
    def _timer_pause(self):
        self.timesheet_timer_pause = False
        if self.task_ids:
          for m in self.task_ids:
            if m.timesheet_timer_pause: 
              self.timesheet_timer_pause = m.timesheet_timer_pause
            
