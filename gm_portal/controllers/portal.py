# -*- encoding: utf-8 -*-
############################################################
#                                                          #
#   G. Mostafa                                             #
#   Copyright (C) 2024 (https://gmostafa1210.github.io/)   #
#                                                          #
############################################################

from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.http import request


class GmCustomerPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        res = super()._prepare_home_portal_values(counters)
        res['student_count'] = request.env['gm.student'].sudo().search_count([])
        return res