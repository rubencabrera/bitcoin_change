# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2009 CamptoCamp. All rights reserved.
#    @author Nicolas Bessi
#
#    Abstract class to fetch rates from Yahoo Financial
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

from currency_rate_update.services import Currency_getter_interface
import logging
_logger = logging.getLogger(__name__)


class bitpay_getter(Currency_getter_interface):
    """Implementation of Currency_getter_factory interface
    for bitpay service
    """
     supported_currency_array = [
        'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN',
        'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL',
        'BSD', 'BTC', 'BTN', 'BWP', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLP', 'CNY',
        'COP', 'CRC', 'CUP', 'CVE', 'CYP', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD',
        'EEK', 'EGP', 'ERN', 'ETB', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP',
        'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG',
        'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD',
        'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD',
        'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTL', 'LVL', 'LYD', 'MAD',
        'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MTL', 'MUR', 'MVR',
        'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD',
        'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON',
        'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP',
        'SLL', 'SOS', 'SPL', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS',
        'TMM', 'TND', 'TOP', 'TRY', 'TTD', 'TVD', 'TWD', 'TZS', 'UAH', 'UGX',
        'USD', 'UYU', 'UZS', 'VEB', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG',
        'XAU', 'XBT', 'XCD', 'XDR', 'XOF', 'XPD', 'XPF', 'XPT', 'YER', 'ZAR',
        'ZMK', 'ZWD'
    ]


    def get_updated_currency(self, currency_array, main_currency,
                             max_delta_days):
        """
        Get currency rates.
        - currency_array:
            array with the codes of the currencies which value
            we want to retrieve.
        """
        # If Bitcoin is our main currency, all the rates we obtain are right as
        # bitpay gives them to us. In any other case, we need to look for our
        # main currency and get the inverse of the bitcoin price.
        self.validate_cur(main_currency)
        map(lambda x: self.validate_cur(x),currency_array)
        # URL de la API de bitpay. Nos devuelve un diccionario (objeto JSON)
        # con las tasas de cambio de XBT (figura como BTC)
        url = ('https://bitpay.com/api/rates')
        if main_currency in currency_array:
            # Get the main currency of the company out of the ones we want
            # to retrieve.
            currency_array.remove(main_currency)
        _logger.debug("Bitpay rates service : connecting...")
        # Lo que obtenemos aquí es un string:
        import json
        res = json.loads(self.get_url(url))

        for currency_dictionary in res:
            if currency_dictionary['code'] in currency_array:
                self.updated_currency[currency_dictionary['code']] = \
                                                currency_dictionary['rate']

        # In bitpay's api, res is a list of dict elements with the following
        # structure (key, value):
        #     ('code', ISO currency code)
        #     ('name', currency name)
        #     ('rate', current Bitcoin price for this currency)

        # for curr in currency_array:
        #     self.validate_cur(curr)
        #
        #     # val = res.split(',')[1]
        #
        #     if val:
        #         self.updated_currency[curr] = val
        #     else:
        #         raise Exception('Could not update the %s' % (curr))

        return self.updated_currency, self.log_info
