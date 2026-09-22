# -*- coding: utf-8 -*-
##############################################################################
#
#    ERP Artists
#    Copyright (C) 2025-TODAY ERP Artists (<https://www.erpartists.com>).
#    Author: ERP Artists (<https://www.erpartists.com>)
#
##############################################################################
{
    "name": "Product multi-company",
    "version": "19.0.1.0.0",
    "category": "Product Management",
    "summary": "Select individually the product template visibility on each " "company",
    "description": """
Product Multi-Company
=====================

Product Multi-Company extends Odoo's Product Management by allowing you to
control the visibility of each product template across multiple companies.

Instead of making every product available to all companies, this module lets
you assign one or more companies to a product template. Users will only see
products that are available for their active company, making it easier to
maintain separate product catalogs while working in a shared multi-company
environment.

Products without any company restriction can remain available to all
companies, providing the flexibility to manage both shared and
company-specific products from a single database.

The module integrates seamlessly with Odoo's Product application and the
Multi-Company framework without changing the standard product management
workflow.
""",
    "author": "ERP Artists",
    "website": "https://www.erpartists.com",
    "license": "LGPL-3",
    "depends": ["ea_base_multi_company", "product"],
    "data": ["views/product_template_view.xml"],
    "post_init_hook": "post_init_hook",
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 0.00,
    'currency': 'USD',
}
