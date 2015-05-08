# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 credativ ltd (<http://www.credativ.co.uk>).
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp


class product_pricelist_item(osv.osv):
    _inherit = 'product.pricelist.item'

    _columns = {
        'discount': fields.float(
            'Discount (%)',
            digits_compute=dp.get_precision('Discount'),
            help="Default discount applied on a sale order line.",
        ),
    }

    _defaults = {
        'discount': 0.0,
    }

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
