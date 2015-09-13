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
    


class BitcoinTransaction(models.Model):
    """
    Objeto transacción de bitcoin. 
    No es un objeto que queramos editar a mano.
    """
    _name = 'bitcoin.transaction'

    _rec_name = 'price'
    # bitpay api (2.3.3) returns a unicode string
    # Incluir un campo name, computado a partir de una combinación de otros. 
    btc_due = fields.Float(compute='_compute_transaction')
    btc_paid = fields.Float(compute='_compute_transaction')
    btc_price = fields.Float(compute='_compute_transaction')
    currency = fields.Float(compute='_compute_transaction')
    current_time = fields.Float(compute='_compute_transaction')
    exchange_rate = fields.Float(compute='_compute_transaction')
    exception_status = fields.Float(compute='_compute_transaction')
    expriation_time = fields.Float(compute='_compute_transaction')
    transaction_id = fields.Float(compute='_compute_transaction')
    invoice_time = fields.Float(compute='_compute_transaction')
    payment_url_21 = fields.Float(compute='_compute_transaction')
    payment_url_72 = fields.Float(compute='_compute_transaction')
    price = fields.Float()
    rate = fields.Float(compute='_compute_transaction')
    status = fields.Float(compute='_compute_transaction')
    token = fields.Float(compute='_compute_transaction')
    url = fields.Float(compute='_compute_transaction')

    # Realizamos la transacción. De momento sin tener en cuenta la moneda
    @api.depends('price')
    def _compute_transaction(self):

class BitcoinExchangeRate(models.Model):
    """
    Saves data about exchange rates on different exchange providers. 
    """
    _name = 'bitcoin.exchange.rate'

    # No es necesario, tenemos el momento de la creación del registro y con eso nos vale. 
    # date = fields.DateTime(
    provider = fields.Many2one(comodel_name= 'bitcoin.exchange',string="Exchange provider")
    rate= fields.Float()


class BitcoinExchangeProvider(models.Model):
    """
    Bitcoin exchange entities which whom we operate
    """

    _name = 'bitcoin.exchange'

    name = fields.Char(string="Exchange entity name", required=True)
    # ¿Token, pubKey...?



