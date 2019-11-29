
{
    'name': "uudp-analytic",

    'summary': """
       addon untuk menambahkan field ke suatu form (inherit)""",

    'description': """
        addon untuk menambahkan field ke suatu form (inherit)
    """,

    'author': "firmanrizaldiyusup@gmail.com",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','vit_uudp'],

    # always loaded
    'data': [
        'views/form_pengajuan.xml',
    ],

}