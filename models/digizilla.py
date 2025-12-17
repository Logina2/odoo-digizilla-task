from odoo import fields, models

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla Assessment Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender', tracking=True)
    country_id = fields.Many2one('res.country', string='Country', tracking=True)
    joining_date = fields.Date(string='Joining Date', tracking=True)
    
    # Assuming 'Tags' refers to a many2many relationship, similar to partner tags
    tag_ids = fields.Many2many('res.partner.category', string='Tags', tracking=True)
    
    # Customers (multiple values from odoo default customers model - res.partner)
    customer_ids = fields.Many2many('res.partner', string='Customers', tracking=True)
    
    # Company* (one value from Odoo default Companies official model - res.company)
    company_id = fields.Many2one('res.company', string='Company', required=True, tracking=True)
    
    # Notes (a long text field in a new tab named Notes)
    notes = fields.Text(string='Notes')
    
    # Comments (a short text field in a new tab named Comments)
    comments = fields.Char(string='Comments')
    
    # The mail.thread and mail.activity.mixin inheritance handles the "Messages and logger" requirement.
    # The tracking=True on fields ensures changes are logged.
