# -*- coding: utf-8 -*-
##############################################################################
#
#    ERP Artists
#    Copyright (C) 2025-TODAY ERP Artists (<https://www.erpartists.com>).
#    Author: ERP Artists (<https://www.erpartists.com>)
#
##############################################################################
{
    "name": "Multi Company Base",
    "version": "19.0.1.0.0",
    "category": "base",
    "summary": "Provides a base for adding multi-company support to models.",
    "description": """
Multi Company Base
==================

Multi Company Base provides a common foundation for adding multi-company
support to custom Odoo models.

Instead of implementing company-related logic in every module, this module
offers a reusable base that simplifies the development of multi-company
applications. It helps developers create models that work correctly across
multiple companies while following Odoo's standard multi-company behavior.

This module is intended to be used as a dependency for other ERP Artists
modules that require company-specific data and access control.

Features
--------
* Provides a reusable base for multi-company development.
* Simplifies adding company support to custom models.
* Follows Odoo's standard multi-company behavior.
* Helps maintain consistent company-based access across modules.
* Reduces duplicate development effort.
* Easy to extend for custom business applications.""",
    "author": "ERP Artists",
    "website": "https://www.erpartists.com",
    "license": "LGPL-3",
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 0.00,
    'currency': 'USD',
}
