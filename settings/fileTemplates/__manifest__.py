# -*- coding: utf-8 -*-
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# AmosERP odoo11.0
# QQ:35350428
# 邮件:35350428@qq.com
# 手机：13584935775
# 作者：'amos'
# 公司网址： www.odoo.pw  www.100china.cn www.amoserp.com
# Copyright 昆山一百计算机有限公司 2012-2018 Amos
# 日期：2018/09/12 15:01
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
{
    'name': 'AmosERP 仓库',
    'summary': '库存',
    'version': '1.0',
    'category': '仓库',
    'sequence': 40001,
    'author': 'Amos',
    'website': 'http://www.odoo.pw',
    'depends': ['base', 'web', 'Amos_Base', 'Amos_Product','hd_base'],
    'data': [
        'sequence.xml',
        'data/res_col_data.xml',

        'security/security.xml',
        'security/ir.model.access.csv',

        'wizard/inventory_product_wizard.xml',

        'views/stock_picking_tested_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'description': """
""",
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: