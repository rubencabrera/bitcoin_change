# -*- coding: utf-8 -*-

from openerp import models, fields, api
import logging
# from datetime import datetime
#Get the logger
_logger = logging.getLogger(__name__)

# Importamos la api de bitcoin, debe estar ya instalada en el sistema.
# En caso contrario loggeamos el error.
# Se incluye la api como dependencia externa en el manifiesto. 
try:
    from bitpay.bitpay_client import Client
except ImportError:
    # Aquí deberíamos usar el log de error de odoo
    _logger.error("Dependency missing, couldn't find bitpay-py2. Make sure your sysadmin installs it.")
    

