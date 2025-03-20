# -*- coding: utf-8 -*-
"""
Created on Tue Apr 12 13:54:12 2022

@author: dingq
"""
# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

from caplib.datetime import *
from caplib.market import *
from caplib.market import create_snowball_auto_callable_note

class TestMarket(unittest.TestCase):
    def setUp(self) -> None:
        hol_serial_numbers =[44654, 44954]
        sbd_serial_numbers = [44655]
        # Convert list of serial numbers to datetime objects
        holidays = [datetime.fromordinal(sn) for sn in hol_serial_numbers]
        specials = [datetime.fromordinal(sn) for sn in sbd_serial_numbers]
        create_calendar('CAL_CFETS', holidays, specials)
        
    def test_create_time_series(self):
        expected = b'\n\x07\x08\xe6\x0f\x10\x03\x18\x03\n\x07\x08\xe6\x0f\x10\x03\x18\x04\x12\x18\x08\x02\x10\x01\x1a\x10{\x14\xaeG\xe1z\x84?\xb8\x1e\x85\xebQ\xb8\x9e? \x01"\tSHIBOR_3M'
        dates = [datetime(2022, 3, 3), datetime(2022, 3, 4)]
        values = [0.01, 0.03]
        test = create_time_series(dates, values, 'TS_FORWARD_MODE', 'shibor_3m')
        self.assertEqual(test.SerializeToString(), expected)

    def test_to_time_series_mode(self):
        expected = TimeSeries.Mode.TS_FORWARD_MODE
        test = to_time_series_mode('TS_FORWARD_MODE')
        self.assertEqual(test, expected)

    def test_to_ccy_pair(self):
        expected = b'\n\x05\n\x03USD\x12\x05\n\x03CNY'
        test = to_ccy_pair('usdcny')
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_foreign_exchange_rate(self):
        expected = b'\t\x87\xa7W\xca2\xc4\x1a@\x12\x03CNY\x1a\x03USD'
        test = create_foreign_exchange_rate(6.6916, "CNY", "USD")
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_fx_spot_rate(self):
        expected = b'\n\x13\t\x87\xa7W\xca2\xc4\x1a@\x12\x03CNY\x1a\x03USD\x12\x07\x08\xe6\x0f\x10\x03\x18\t\x1a\x07\x08\xe6\x0f\x10\x03\x18\t'
        foreign_exchange_rate = create_foreign_exchange_rate(6.6916, "CNY", "USD")
        test = create_fx_spot_rate(foreign_exchange_rate, datetime(2022, 3, 9), datetime(2022, 3, 9))
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_fx_spot_template(self):
        expected = b'\x08\xb9\x17\x12\nTestFxSpot\x1a\x0e\n\x05\n\x03USD\x12\x05\n\x03CNY \x012\x04\x08\x01\x10\x01:\tCAL_CFETS'
        test = create_fx_spot_template(inst_name="TestFxSpot",
                                       currency_pair="USDCNY",
                                       spot_day_convention="FOLLOWING",
                                       calendars=["CAL_CFETS"],
                                       spot_delay="1d")
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_american_option(self):
        result = create_american_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            strike=100.000,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)
 
    def test_create_european_option(self):
        result = create_european_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike=100.000,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_digital_option(self):
        result = create_digital_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike=100.000,
            cash=10000.00,
            asset=0.0,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_asian_option(self):
        result = create_asian_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike_type='ATM',
            strike=100.000,
            avg_method='ARITHMETIC',
            obs_type='CONTINUOUS',
            fixing_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)  

    def test_create_one_touch_option(self):
        result = create_one_touch_option(
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP',
            barrier_value=105.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            cash=10000.00,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_double_touch_option(self):
        result = create_double_touch_option(
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='UP',
            lower_barrier_value=105.000,
            upper_barrier_type='DOWN',
            upper_barrier_value=95.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            lower_cash=10000.00,
            upper_cash=10000.00,
            lower_asset=0.0,
            upper_asset=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',            
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_single_barrier_option(self):
        result = create_single_barrier_option(
            payoff_type='CALL',
            strike=100.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP',
            barrier_value=105.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            cash=10000.00,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)  

    def test_create_double_barrier_option(self):
        result = create_double_barrier_option(
            payoff_type='CALL',
            strike=100.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='UP',
            lower_barrier_value=105.000,
            upper_barrier_type='DOWN',
            upper_barrier_value=95.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            lower_cash=10000.00,
            upper_cash=10000.00,
            lower_asset=0.0,
            upper_asset=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',            
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)  

    def test_create_single_shark_fin_option(self):
        result = create_single_shark_fin_option(
            payoff_type='CALL',
            strike=100.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            gearing=1.000,
            performance_type='STANDARD',
            barrier_type='UP',
            barrier_value=105.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            cash_rebate=10000.00,
            asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_double_shark_fin_option(self):
        result = create_double_shark_fin_option(
            lower_strike=100.000,
            upper_strike=100.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            gearing=1.000,
            performance_type='STANDARD',
            lower_barrier_type='UP',
            lower_barrier_value=105.000,
            upper_barrier_type='DOWN',
            upper_barrier_value=95.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            lower_cash_rebate=10000.00,
            upper_cash_rebate=10000.00,
            lower_asset_rebate=0.0,
            upper_asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')        
        self.assertEqual(result, None)

    def test_create_range_accrual_option(self):        
        result = create_range_accrual_option(
            expiry_date=datetime(2020, 8, 19),
            delivery_date=datetime(2020, 8, 20),
            asset=100.000,
            cash=100.000,
            lower_barrier=100.000,
            upper_barrier=100.000,
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')        
        self.assertEqual(result, None)

    def test_create_air_bag_option(self):
        result = create_air_bag_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_strike=100.000,
            upper_strike=100.000,
            lower_participation=1.000,
            upper_participation=1.000,
            knock_in_strike=100.000,
            barrier_type='UP',
            barrier_value=105.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)
        
    def test_create_ping_pong_option(self):
        result = create_ping_pong_option(
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='UP',
            lower_barrier_value=105.000,
            upper_barrier_type='DOWN',
            upper_barrier_value=95.000,
            barrier_obs_type='CONTINUOUS',
            obs_schedule=['2020-02-20', '2020-04-20', '2020-06-20'],
            payment_type='CASH',
            cash=10000.00,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_collar_option(self):
        result = create_collar_option(
            payoff_type='CALL',
            lower_gearing=1.000,
            upper_gearing=1.000,
            lower_strike=100.000,
            upper_strike=100.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_snowball_auto_callable_note(self):
        result = create_snowball_auto_callable_note(
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 21),
            day_count='ACT_365_FIXED',
            knock_out_barrier_type='UP_OUT',
            knock_out_barrier_value=69699.000,
            knock_in_barrier_type='DOWN_IN',
            knock_in_barrier_value=53104.000,
            long_short='SELL',
            knock_in_payoff_type='PUT',
            knock_in_payoff_strike=66380.000,
            knock_in_payoff_gearing=1.000,
            reference_price=66380.000,
            expiry=datetime(2020, 8, 22),
            delivery=datetime(2020, 8, 22),
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

    def test_create_phoenix_auto_callable_note(self):
        result = create_phoenix_auto_callable_note(
            coupon_payoff_type='CALL',
            coupon_strike=66380.000,
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 22),
            day_count='ACT_365_FIXED',
            knock_out_barrier_type='UP_OUT',
            knock_out_barrier_value=73018.000,
            knock_in_barrier_type='DOWN_IN',
            knock_in_barrier_value=59742.000,
            long_short='SELL',
            knock_in_payoff_type='PUT',
            knock_in_payoff_strike=56423.000,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            settlement_days=1,
            nominal=1000000.00,
            payoff_ccy='CNY',
            underlying_type='COMMODITY',
            underlying_ccy='CNY',
            underlying='CU2209')
        self.assertEqual(result, None)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMarket)
    unittest.TextTestRunner(verbosity=2).run(suite)
