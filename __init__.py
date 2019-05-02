# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RestaurantEligibility
                                 A QGIS plugin
 Check if a building is eligible for catering services.
                             -------------------
        begin                : 2019-04-29
        copyright            : (C) 2019 by Yifang Zhao
        email                : yifangzhao951618@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RestaurantEligibility class from file RestaurantEligibility.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .restaurant_eligibility import RestaurantEligibility
    return RestaurantEligibility(iface)
