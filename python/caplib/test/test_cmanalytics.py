import unittest
from datetime import datetime

from caplib.analytics import *
from caplib.cmarket import *
from caplib.cmanalytics import *
from caplib.market import *


class TestCmAnalytics(unittest.TestCase):

    def setUp(self):

        # Create calendar
        cal_cfets = 'CAL_CFETS'
        
        hol_serial_numbers =[44654, 44954]
        sbd_serial_numbers = [44655]
        # Convert list of serial numbers to datetime objects
        holidays = [datetime.fromordinal(sn) for sn in hol_serial_numbers]
        specials = [datetime.fromordinal(sn) for sn in sbd_serial_numbers]
        create_calendar(cal_cfets, holidays, specials)
        
        # Create default PDE and Monte Carlo Settings
        default_pde_settings = create_pde_settings()
        default_monte_carlo_settings = create_monte_carlo_settings()

        # Create Pricing Settings with BLACK_SCHOLES_MERTON model and ANALYTICAL method 
        self.bsm_model_settings = create_model_settings('BLACK_SCHOLES_MERTON')        
        self.bsm_analytical_pricing_settings = create_pricing_settings('CNY', False, self.bsm_model_settings, 'ANALYTICAL', default_pde_settings, default_monte_carlo_settings)

        # Create Pricing Settings with BLACK_SCHOLES_MERTON model and PDE method 
        self.bsm_pde_settings = create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP')
        self.bsm_pde_pricing_settings = create_pricing_settings('CNY', False, self.bsm_model_settings, 'PDE', self.bsm_pde_settings, default_monte_carlo_settings)

        # Create Pricing Settings with BLACK_SCHOLES_MERTON model and MONTE_CARLO method
        self.bsm_monte_carlo_settings = create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD',False, 1)
        self.bsm_mc_pricing_settings = create_pricing_settings('CNY', False, self.bsm_model_settings, 'MONTE_CARLO', default_pde_settings, self.bsm_monte_carlo_settings)

        # Create Pricing Settings with Duprie Local Vol model and PDE method 
        self.duprie_model_settings = create_model_settings('DUPRIE_LOCAL_VOL',[201,401,4, 0.001])
        self.duprie_pde_settings = create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP')
        self.duprie_pde_pricing_settings = create_pricing_settings('CNY', False, self.duprie_model_settings, 'PDE', self.duprie_pde_settings, default_monte_carlo_settings)

        # Create Pricing Settings with Duprie Local Vol model and MONTE_CARLO method
        self.duprie_monte_carlo_settings = create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD', False, 201)
        self.duprie_mc_pricing_settings = create_pricing_settings('CNY', False, self.duprie_model_settings, 'MONTE_CARLO', default_pde_settings, self.duprie_monte_carlo_settings)

        # Create Price Risk Settings
        self.price_risk_settings = create_price_risk_settings(delta=True, gamma=True, curvature=False, shift=1.0e-2, curvature_shift=5.0e-1, method='CENTRAL_DIFFERENCE_METHOD', scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE')
        # Create Vol Risk Settings
        self.vol_risk_settings = create_vol_risk_settings(vega=True, volga=True, shift=1.0e-2, method='CENTRAL_DIFFERENCE_METHOD', granularity='TERM_STRIKE_BUCKET_RISK', scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE')
        # Create Price Vol Risk Settings
        self.price_vol_risk_settings = create_price_vol_risk_settings(vanna=True, price_shift=1.0e-2, vol_shift=1.0e-2, method='CENTRAL_DIFFERENCE_METHOD', granularity='TERM_STRIKE_BUCKET_RISK', price_scaling_factor=1.0e-2, vol_scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE')
        # Create Theta Risk Setting
        self.theta_risk_settings = create_theta_risk_settings(theta=True, shift=1, scaling_factor=1./365.)
        # Create IR Curve Risk Settings
        self.ir_curve_risk_settings = create_ir_curve_risk_settings(delta=True, gamma=True, curvature=False, shift=1.0e-4, curvature_shift=5.0e-1, method='CENTRAL_DIFFERENCE_METHOD', granularity='TERM_BUCKET_RISK', scaling_factor=1.0e-4, threading_mode='SINGLE_THREADING_MODE')
        # Create Dividend Curve Risk Settings
        self.dividend_curve_risk_settings = create_dividend_curve_risk_settings(delta=True, gamma=True, shift=1.0e-4, method="CENTRAL_DIFFERENCE_METHOD", granularity="TOTAL_RISK", scaling_factor=1.0e-4, threading_mode="SINGLE_THREADING_MODE")

        # Create Risk Settings
        self.risk_settings = create_cm_risk_settings(self.ir_curve_risk_settings, self.price_risk_settings,self.vol_risk_settings, self.price_vol_risk_settings, self.dividend_curve_risk_settings, self.theta_risk_settings)

        # Create Market Data
        self.as_of_date = datetime(2020, 2, 21)

        # Create IR Yield Curve
        self.ir_yield_curve = create_ir_yield_curve(self.as_of_date,
                                                   'CNY',
                                                   [datetime(2020, 2, 26), datetime(2020, 3, 2), datetime(2020, 3, 9), datetime(2020, 3, 24), datetime(2020, 5, 24), datetime(2020, 8, 24), datetime(2020, 11, 24), datetime(2021, 2, 24), datetime(2022, 2, 24), datetime(2023, 2, 24), datetime(2024, 2, 24), datetime(2025, 2, 24), datetime(2027, 2, 24), datetime(2030, 2, 24)],
                                                   [0.013549, 0.019776, 0.019769, 0.022484, 0.024174, 0.025682, 0.02651, 0.027133, 0.027431, 0.028483, 0.029728, 0.030841, 0.032693, 0.03441])
        
        # Create CM Option Quote Matrix
        self.cm_option_quote_matrix = create_cm_option_quote_matrix(exercise_type='AMERICAN', 
                                                                    underlying_type='FUTURE_UNDERLYING_TYPE', 
                                                                    term_dates=[datetime(2020, 3, 12), datetime(2020, 4, 13), datetime(2020, 5, 12), datetime(2020, 6, 12), datetime(2020, 7, 10), datetime(2020, 8, 12), datetime(2020, 9, 11)], 
                                                                    payoff_types=['PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'PUT_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE', 'CALL_OPTION_TYPE'], 
                                                                    strikes=[54000, 55000, 56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000, 82000], 
                                                                    prices=[[14.00, 16.00, 20.00, 26.00, 38.00, 64.00, 86.00, 130.00, 198.00, 282.00, 400.00, 600.00, 878.00, 1070.00,660.00, 394.00, 236.00, 142.00, 90.00, 52.00, 32.00, 22.00, 18.00, 14.00, 10.00, 6.00, 6.00, 6.00],
                                                                            [126.00, 126.00, 160.00, 200.00, 250.00, 312.00, 396.00, 478.00, 600.00, 776.00, 974.00, 1230.00, 1602.00, 1736.00, 1276.00, 910.00, 642.00, 460.00, 312.00, 212.00, 150.00, 110.00, 80.00, 58.00, 40.00, 28.00, 38.00, 26.00],
                                                                            [172.00, 192.00, 236.00, 292.00, 426.00, 478.00, 574.00, 702.00, 892.00, 1206.00, 1368.00, 1632.00, 2140.00, 2218.00,1762.00, 1350.00, 1026.00, 762.00, 562.00, 404.00, 294.00, 210.00, 128.00, 102.00, 58.00, 56.00, 106.00, 20.00],
                                                                            [414.00, 486.00, 584.00, 700.00, 958.00, 1186.00, 1308.00, 1634.00, 2008.00, 2436.00, 2914.00, 2814.00, 2396.00, 2026.00, 1698.00, 1412.00, 758.00, 964.00, 446.00, 346.00, 256.00, 188.00, 138.00, 102.00, 82.00, 44.00],
                                                                            [676.00, 798.00, 936.00, 1064.00, 1354.00, 1780.00, 2138.00, 2538.00, 2978.00, 3474.00, 3324.00, 2902.00, 2516.00, 1544.00, 1256.00, 984.00, 806.00, 622.00, 488.00, 382.00, 282.00],
                                                                            [678.00, 802.00, 906.00, 1058.00, 1246.00, 1456.00, 2066.00, 2446.00, 2862.00, 3314.00, 3814.00, 3590.00, 3168.00, 2784.00, 2446.00, 2136.00, 1852.00, 1612.00, 1390.00, 630.00, 1026.00, 448.00, 338.00, 278.00, 196.00],
                                                                            [1006.00, 1146.00, 1312.00, 1558.00, 1790.00, 2118.00, 2688.00, 3118.00, 3578.00, 4078.00, 3828.00, 3408.00, 3024.00, 2680.00, 2358.00, 2078.00, 1822.00, 1586.00, 1388.00, 666.00]],
                                                                    underlying='CU.SHFE')

        # Build Volatility Surface
        self.vol_surf = cm_vol_surface_builder(self.as_of_date, 
            smile_method='LINEAR_SMILE_METHOD', 
            wing_strike_type='DELTA',
            lower=-0.01,
            upper=0.01, 
            cm_option_quote_matrix=self.cm_option_quote_matrix, 
            underlying_prices=[66810.0, 66750.0, 66620.0, 66620.0, 66490.0, 66460.0, 66380.0],
            discount_curve=self.ir_yield_curve, 
            fwd_curve=self.ir_yield_curve,
            building_settings = [0.02, 0.04], 
            underlying='CU.SHFE')

    # Test cm_vol_surface_builder
    
    def test_cm_vol_surface_builder(self):
        expected = b'\x08\x01\n\x01\x12\x1e\x08\x01\x10\x01\x12\x08\x08\x01\x10\x01\x12\x08\x12\x1e\x08\x01\x10\x01\x12\x08\x16\x1e\x08\x01\x10\x01\x12\x08\x1a\x1e\x08\x01\x10\x01\x12\x08\x1e\x1e\x08\x01\x10\x01\x12\x08 \x1e\x08\x01\x10\x01\x12\x08"\x1e\x08\x01\x10\x01\x12\x08$\x1e\x08\x01\x10\x01\x12\x08&\x1e\x08\x01\x10\x01\x12\x08(\x1e\x08\x01\x10\x01\x12\x08*\x1e\x08\x01\x10\x01\x12\x08,\x1e\x08\x01\x10\x01\x12\x08.\x1e\x08\x01\x10\x01\x12\x08/\x1e\x08\x01\x10\x01\x12\x080\x1e\x08\x01\x10\x01\x12\x082\x1e\x08\x01\x10\x01\x12\x084\x1e\x08\x01\x10\x01\x12\x086\x1e\x08\x01\x10\x01\x12\x088\x1e\x08\x01\x10\x01\x12\x08:\x1e\x08\x01\x10\x01\x12\x08<\x1e\x08\x01\x10\x01\x12\x08>\x1e\x08\x01\x10\x01\x12\x08@\x1e\x08\x01\x10\x01\x12\x08B\x1e\x08\x01\x10\x01\x12\x08D\x1e\x08\x01\x10\x01\x12\x08F\x1e\x08\x01\x10\x01\x12\x08H\x1e\x08\x01\x10\x01\x12\x08J\x1e\x08\x01\x10\x01\x12\x08L\x1e\x08\x01\x10\x01\x12\x08N\x1e\x08\x01\x10\x01\x12\x08P\x1e\x08\x01\x10\x01\x12\x08R\x1e\x08\x01\x10\x01\x12\x08T\x1e\x08\x01\x10\x01\x12\x08V\x1e\x08\x01\x10\x01\x12\x08X\x1e\x08\x01\x10\x01\x12\x08Z\x1e\x08\x01\x10\x01\x12\x08\x5c\x1e\x08\x01\x10\x01\x12\x08\x5e\x1e\x08\x01\x10\x01\x12\x08\x60\x1e\x08\x01\x10\x01\x12\x08\x62\x1e\x08\x01\x10\x01\x12\x08\x64\x1e\x08\x01\x10\x01\x12\x08\x66\x1e\x08\x01\x10\x01\x12\x08\x68\x1e\x08\x01\x10\x01\x12\x08\x6a\x1e\x08\x01\x10\x01\x12\x08\x6c\x1e\x08\x01\x10\x01\x12\x08\x6e\x1e\x08\x01\x10\x01\x12\x08\x70\x1e\x08\x01\x10\x01\x12\x08\x72\x1e\x08\x01\x10\x01\x12\x08\x74\x1e\x08\x01\x10\x01\x12\x08\x76\x1e\x08\x01\x10\x01\x12\x08\x78\x1e\x08\x01\x10\x01\x12\x08\x7a'
        self.assertEqual(self.vol_surf.SerializeToString(), expected)

    def test_cm_american_option_pricer(self):
        instrument = dqCreateProtoCmInstrument('call', 'EURUSD', 'Put', 1.0, 1.0, 'EUR', 'USD', datetime(2020,1,1), datetime(2021,1,1))
        pricing_date = datetime(2020,1,1)
        mkt_data_set = create_cm_mkt_data_set(datetime(2020,1,1), 'EUR', 'USD', 1.0, 0.1, 0.01)
        pricing_settings = create_cm_pricing_settings(0.1, 0.1)
        risk_settings = create_cm_risk_settings('IR', 'Price', 'Vol', 'PriceVol', 'Theta', 'Dividend')
        scn_settings = create_cm_scenario_settings('RISK_NEUTRAL', 'RISK_NEUTRAL', 'RISK_NEUTRAL', 'RISK_NEUTRAL')
        res = cm_american_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)
        self.assertGreater(res.value, 0.0)
    
    def test_create_fx_risk_settings(self):
        expected = b'\n!\x08\x01\x18\x01!-C\x1c\xeb\xe26\x1a?){\x14\xaeG\xe1zt?8\x01A-C\x1c\xeb\xe26\x1a?\x12\x1d\x08\x01!-C\x1c\xeb\xe26\x1a?){\x14\xaeG\xe1zt?A-C\x1c\xeb\xe26\x1a?\x1a\x12!-C\x1c\xeb\xe26\x1a?A-C\x1c\xeb\xe26\x1a?"$\x11-C\x1c\xeb\xe26\x1a?\x19-C\x1c\xeb\xe26\x1a?!-C\x1c\xeb\xe26\x1a?A-C\x1c\xeb\xe26\x1a?*\r\x08\x01\x10\x01\x19\x1ag\x016\x9fqf?'
        ir_curve_settings = create_ir_curve_risk_settings(delta=True, curvature=True, granularity='TERM_BUCKET_RISK')
        price_settings = create_price_risk_settings(delta=True)
        vol_settings = create_vol_risk_settings()
        price_vol_settings = create_price_vol_risk_settings()
        theta_settings = create_theta_risk_settings(theta=True)
        test = create_fx_risk_settings(ir_curve_settings,
                                       price_settings,
                                       vol_settings,
                                       price_vol_settings,
                                       theta_settings)
        self.assertEqual(test.SerializeToString(), expected)

    def test_create_fx_mkt_data_set(self):
        expected = b'\n\x07\x08\xe6\x0f\x10\x03\x18\t\x12X\x12;\n7\n\x07\x08\xe6\x0f\x10\x03\x18\t\x10\x02\x1a\x07\x08\xe6\x0f\x10\x03\x18\n\x1a\x07\x08\xe9\x0f\x10\x03\x18\n"\x00*\x12\n\x10{\x14\xaeG\xe1z\x94?\x9a\x99\x99\x99\x99\x99\x99?0\x018\x01\x10\x01\x1a\x03CNY \x01:\x12\x12\x10\x08\x01\x10\x01\x1a\x08\x00\x00\x00\x00\x00\x00\x00\x00 \x01\x1aX\x12;\n7\n\x07\x08\xe6\x0f\x10\x03\x18\t\x10\x02\x1a\x07\x08\xe6\x0f\x10\x03\x18\n\x1a\x07\x08\xe9\x0f\x10\x03\x18\n"\x00*\x12\n\x10{\x14\xaeG\xe1z\x94?\x9a\x99\x99\x99\x99\x99\x99?0\x018\x01\x10\x01\x1a\x03USD \x01:\x12\x12\x10\x08\x01\x10\x01\x1a\x08\x00\x00\x00\x00\x00\x00\x00\x00 \x01"\'\n\x13\t\xcd\xcc\xcc\xcc\xcc\xcc\x1a@\x12\x03CNY\x1a\x03USD\x12\x07\x08\xe6\x0f\x10\x03\x18\t\x1a\x07\x08\xe6\x0f\x10\x03\x18\t*\xed\x01\n \x08\x01\x10\x01\x18\x01 \x01(\x010\x028\x01I\x9a\x99\x99\x99\x99\x99\xa9?Q\x9a\x99\x99\x99\x99\x99\xd9?\x12\x07\x08\xe6\x0f\x10\x03\x18\t\x1aV\x08\x01\x12\x07\x08\xe6\x0f\x10\x03\x18\t\x19\x9a\x99\x99\x99\x99\x99\xa9?!\x9a\x99\x99\x99\x99\x99\xd9?*\x12\n\x10\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@0\x019{\x14\xaeG\xe1z\x94?B\x12\n\x10\x9a\x99\x99\x99\x99\x99\xb9?\x9a\x99\x99\x99\x99\x99\xb9?J\x00R\x00X\x01\x1aV\x08\x01\x12\x07\x08\xe6\x0f\x10\x03\x18\t\x19\x9a\x99\x99\x99\x99\x99\xa9?!\x9a\x99\x99\x99\x99\x99\xd9?*\x12\n\x10\x00\x00\x00\x00\x00\x00\xf0?\x00\x00\x00\x00\x00\x00\x00@0\x019{\x14\xaeG\xe1z\xa4?B\x12\n\x10\x9a\x99\x99\x99\x99\x99\xb9?\x9a\x99\x99\x99\x99\x99\xb9?J\x00R\x00X\x01"\x07\x08\xe6\x0f\x10\x03\x18\n"\x07\x08\xe9\x0f\x10\x03\x18\n'
        
        test = create_fx_mkt_data_set(self.as_of_date,
                                      self.domestic_discount_curve_cny,
                                      self.foreign_discount_curve_usd,
                                      self.fx_spot_rate2,
                                      self.vol_surf)
        #print('test_create_fx_mkt_data_set', test.SerializeToString())
        self.assertEqual(test.SerializeToString(), expected)

    def test_fx_ndf_pricer(self):
        expected = b'\x1a\x00"\x00*\x03CNH2\x00'
        fx_ndf_template = create_fx_ndf_template(inst_name="TestFxNdf",
                                                 fixing_offset="180d",
                                                 currency_pair="USDCNH",
                                                 delivery_day_convention="MODIFIED_PRECEDING",
                                                 fixing_day_convention="MODIFIED_PRECEDING",
                                                 calendars=["CAL_CFETS"],
                                                 settlement_currency="USD")

        fx_ndf = create_fx_non_deliverable_forwad(buy_currency="USD",
                                                  buy_amount=10000,
                                                  sell_currency="CNH",
                                                  sell_amount=66916,
                                                  delivery_date=datetime(2022, 12, 21),
                                                  expiry_date=datetime(2022, 12, 21),
                                                  settlement_currency="USD",
                                                  fx_ndf_template=fx_ndf_template)

        test = fx_ndf_pricer(pricing_date=datetime(2022, 3, 9),
                             instrument=fx_ndf,
                             mkt_data=self.fx_mkt_data_set1,
                             pricing_settings=self.pricing_settings1,
                             risk_settings=self.risk_settings)
        self.assertEqual(test.SerializeToString(), expected)

    def test_fx_swap_pricer(self):
        expected = b'\t\x00\x00\x00\x00\x00\x00\xb0=\x1a\x00"\x00*\x03CNY2\x00'
        fx_swap_template = create_fx_swap_template(inst_name="TestFxSwap",
                                                   start_convention="INVALID_INSTRUMENT_START_CONVENTION",
                                                   currency_pair="USDCNY",
                                                   calendars=["CAL_CFETS"],
                                                   start_day_convention="MODIFIED_PRECEDING",
                                                   end_day_convention="MODIFIED_PRECEDING",
                                                   fixing_offset="180d",
                                                   fixing_day_convention="MODIFIED_PRECEDING")

        fx_swap = create_fx_swap(near_buy_currency="USD",
                                 near_buy_amount=10000,
                                 near_sell_currency="CNY",
                                 near_sell_amount=67000,
                                 near_delivery_date=datetime(2022, 12, 21),
                                 near_expiry_date=None,
                                 far_buy_currency="USD",
                                 far_buy_amount=10000,
                                 far_sell_currency="CNY",
                                 far_sell_amount=67000,
                                 far_delivery_date=datetime(2023, 12, 21),
                                 far_expiry_date=None,
                                 fx_swap_template=fx_swap_template)

        test = fx_swap_pricer(pricing_date=datetime(2022, 3, 9),
                              instrument=fx_swap,
                              mkt_data=self.fx_mkt_data_set2,
                              pricing_settings=self.pricing_settings2,
                              risk_settings=self.risk_settings)
        self.assertEqual(test.SerializeToString(), expected)

    def test_fx_forward_pricer(self):
        expected = b'\x1a\x00"\x00*\x03CNY2\x00'
        fx_fwd_template = create_fx_forward_template(inst_name="TestFxForward",
                                                     fixing_offset="180d",
                                                     currency_pair="USDCNY",
                                                     delivery_day_convention="MODIFIED_PRECEDING",
                                                     fixing_day_convention="MODIFIED_PRECEDING",
                                                     calendars=["CAL_CFETS"])

        fx_forward = create_fx_forward(buy_currency="USD",
                                       buy_amount=10000,
                                       sell_currency="CNY",
                                       sell_amount=67000,
                                       delivery=datetime(2022, 12, 21),
                                       fx_fwd_template=fx_fwd_template,
                                       expiry=None)

        test = fx_forward_pricer(pricing_date=datetime(2022, 3, 9),
                                 instrument=fx_forward,
                                 mkt_data=self.fx_mkt_data_set2,
                                 pricing_settings=self.pricing_settings2,
                                 risk_settings=self.risk_settings)
        self.assertEqual(test.SerializeToString(), expected)


if __name__ == "__main__":
    unittest.main()
