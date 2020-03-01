# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.

try:
    from trytond.modules.product_price_list.tests.test_product_price_list import suite  # noqa: E501
except ImportError:
    from .test_product_price_list import suite

__all__ = ['suite']
