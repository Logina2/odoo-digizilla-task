{
    'name': 'Digizilla Assessment Module',
    'version': '17.0.1.0.0',
    'category': 'Custom',
    'summary': 'Developer Assessment Task for Digizilla Model',
    'author': 'Manus',
    'depends': [
        'base',
        'mail', # Required for the message logger
        'contacts', # Required for the Customers model (res.partner)
        'account', # Required for the Companies model (res.company) - often linked to account
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'reports/digizilla_report.xml',
        'reports/digizilla_report_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/digizilla_form_view.js',
        ],
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
