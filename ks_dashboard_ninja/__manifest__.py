# -*- coding: utf-8 -*-
{
    'name': "Dashboard Ninja",

    'summary': """
    Revamp your Odoo Dashboard like never before! It is one of the best dashboard odoo apps in the market.
    """,

    'description': """
        Dashboard Ninja v12.0,
        Odoo Dashboard, 
        Dashboard,
	Dashboards,
        Odoo apps,
        Dashboard app,
        HR Dashboard,
        Sales Dashboard, 
        inventory Dashboard, 
        Lead Dashboard, 
        Opportunity Dashboard, 
        CRM Dashboard,
	    POS,
	    POS Dashboard,
	    Connectors,
	    Web Dynamic,
	    Report Import/Export,
	    Date Filter,
	    HR,
	    Sales,
	    Theme,
	    Tile Dashboard,
	    Dashboard Widgets,
	    Dashboard Manager,
	    Debranding,
	    Customize Dashboard,
	    Graph Dashboard,
	    Charts Dashboard,
	    Invoice Dashboard,
	    Project management,
        ksolves,
        ksolves apps,
        ksolves india pvt. ltd.
    """,

    'author': "Ksolves India Pvt. Ltd.",
    'license': 'OPL-1',
    'currency': 'EUR',
    'price': 249.00,
    'website': "https://www.ksolves.com",
    'maintainer': 'Ksolves India Pvt. Ltd.',
    'live_test_url': 'https://dashboardninja.kappso.com',
    'category': 'Tools',
    'version': '7.0.5',
    'support': 'sales@ksolves.com',
    'images': ['static/description/banner1.gif'],

    'depends': ['base', 'web', 'base_setup'],

    'data': [
        'security/ir.model.access.csv',
        'security/ks_security_groups.xml',
        'data/ks_default_data.xml',
        'views/ks_dashboard_ninja_view.xml',
        'views/ks_dashboard_ninja_item_view.xml',
        'views/ks_dashboard_ninja_assets.xml',
        'views/ks_dashboard_action.xml',
    ],

    'qweb': [
        'static/src/xml/ks_dashboard_ninja_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_templates.xml',
        'static/src/xml/ks_dashboard_ninja_item_theme.xml',
        'static/src/xml/ks_widget_toggle.xml',
        'static/src/xml/ks_dashboard_pro.xml',
        'static/src/xml/ks_import_list_view_template.xml',
        'static/src/xml/ks_quick_edit_view.xml',
    ],

    'demo': [
        'demo/ks_dashboard_ninja_demo.xml',
    ],

    'uninstall_hook': 'uninstall_hook',

}
