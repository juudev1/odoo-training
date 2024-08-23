# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Bon de Consum',
    'version' : '1.1',
    'summary': 'Bon de Consum',
    'sequence': 10,
    'description': "",
    'category': 'Uncategorized',
    #'website': 'http://172.28.99.139:8069/',
    #'images' : ['static/description/icon.png'],
    'application': False,
    'depends' : ['mrp','mail','analytic'],
    "data": [
        "security/ir.model.access.csv",
        "views/bon_consum_views.xml"
        
    ]
}