from odoo import models, fields, api


class KonizTask(models.Model):
    _name = 'koniz.task'
    _description = 'Koniz Task'

    name = fields.Char(string='Task Name', required=True)
    description = fields.Text(string='Description')
    is_done = fields.Boolean(string='Done', default=False)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string='Priority', default='medium')
    date_created = fields.Datetime(string='Created Date', default=fields.Datetime.now, readonly=True)

