FX Derivatives
==================

Examples of FX derivatives pricing and analysis using caplib.

FX Derivatives Pricing
-------------------------

.. code-block:: python

    from datetime import datetime
    from caplib.market import *
    from caplib.analytics import *
    from caplib.fxanalytics import *
    
    ''' Mkt Data'''        
    as_of_date = datetime(2021, 3, 30)

    # USD Depo Curve
    usd_depo_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency='USD',
        term_dates=[
            datetime(2021, 4, 6), datetime(2021, 4, 13), datetime(2021, 4, 20), datetime(2021, 4, 30), 
            datetime(2021, 6, 1), datetime(2021, 6, 30), datetime(2021, 7, 30), datetime(2021, 8, 30), 
            datetime(2021, 9, 30), datetime(2021, 12, 30), datetime(2022, 3, 30), datetime(2022, 9, 30), 
            datetime(2023, 3, 30), datetime(2024, 4, 1), datetime(2025, 3, 31), datetime(2026, 3, 30), 
            datetime(2027, 3, 30), datetime(2028, 3, 30), datetime(2031, 3, 31)
        ],
        zero_rates=[
            0.00016, 0.00016, 0.00016, 0.00017, 0.00016, 0.00019, 0.00023, 0.00026, 0.00028, 0.00034, 0.00042, 0.00063, 0.00108, 0.00292, 0.00546, 0.00798, 0.01025, 0.01217, 0.01624
        ],
        curve_name='USD_DEPO'
    )
    # EUR EURUSD FX
    eur_eurusd_fx_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency = 'EUR',
        term_dates=[
            datetime(2021, 4, 6), datetime(2021, 4, 13), datetime(2021, 4, 20), datetime(2021, 4, 30), 
            datetime(2021, 5, 31), datetime(2021, 6, 30), datetime(2021, 7, 30), datetime(2021, 8, 30), 
            datetime(2021, 9, 30), datetime(2021, 12, 30), datetime(2022, 3, 30), datetime(2022, 9, 30), 
            datetime(2023, 3, 30), datetime(2024, 4, 2), datetime(2025, 3, 31), datetime(2026, 3, 30), 
            datetime(2027, 3, 30), datetime(2028, 3, 30), datetime(2031, 3, 31)
        ],
        zero_rates=[
            -0.00814, -0.00766, -0.00761, -0.00764, -0.00753, -0.00765, -0.00758, -0.00754, -0.00759, -0.00828, -0.00814, -0.00801, -0.00801, -0.00777, -0.00735, -0.0068, -0.00612, -0.00547, -0.00355
        ],
        curve_name='EUR_EURUSD_FX'
    )
    # CNH_USDCNH_FX Curve
    cnh_usdcnh_fx_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency='CNH',
        term_dates=[
            datetime(2021, 4, 1),
            datetime(2021, 4, 7),
            datetime(2021, 4, 14),
            datetime(2021, 4, 30),
            datetime(2021, 6, 30),
            datetime(2021, 9, 30),
            datetime(2021, 12, 31),
            datetime(2022, 3, 31),
            datetime(2023, 3, 31),
            datetime(2024, 4, 1),
            datetime(2025, 3, 31),
            datetime(2026, 3, 31),
            datetime(2028, 3, 31),
            datetime(2031, 3, 31)
        ],
        zero_rates=[
            0.01825,
            0.02184,
            0.02375,
            0.02515,
            0.02622,
            0.02770,
            0.02851,
            0.02958,
            0.03150,
            0.03289,
            0.03400,
            0.03497,
            0.03659,
            0.03814
        ],
        curve_name='CNH_USDCNH_FX'
    )
    # FX Spot
    eurusd_spot_rate = create_fx_spot_rate(create_foreign_exchange_rate(1.1761, "EUR", "USD"), 
                                           as_of_date, datetime(2021,4,1))

    usdcny_spot_rate = create_fx_spot_rate(create_foreign_exchange_rate(6.7, "USD", "CNY"), 
                                           as_of_date, datetime(2021,4,1))
    usdcnh_spot_rate = create_fx_spot_rate(create_foreign_exchange_rate(6.7, "USD", "CNH"), 
                                           as_of_date, datetime(2021,4,1))
        
    # FX Option Quote Matrix
    eurusd_option_quote_matrix = create_fx_option_quote_matrix(
        currency_pair = 'EURUSD', 
        as_of_date = as_of_date,
        terms = [
            "ON", "1W", "2W", "3W", "1M", "2M", "3M", "4M", "6M", "9M", "1Y", "18M", "2Y", "3Y", "4Y", "5Y", "7Y", "10Y"
        ], 
        deltas = [
            "ATM", "D25_RR", "D25_BF", "D10_RR", "D10_BF"
        ],
        quotes = np.array([
            [0.06035, -0.0031, 0.00115, -0.00565, 0.0031],
            [0.05515, -0.0029, 0.00135, -0.00520, 0.00385],
            [0.05730, -0.00285, 0.00135, -0.00520, 0.00415],
            [0.0587, -0.0023, 0.00140, -0.00415, 0.00405],
            [0.06115, -0.00248, 0.00147, -0.00450, 0.00450],
            [0.06105, -0.00213, 0.00177, -0.00380, 0.00530],
            [0.06135, -0.00180, 0.00205, -0.00330, 0.00625],
            [0.0621, -0.0016, 0.00220, -0.00290, 0.00678],
            [0.0625, -0.00135, 0.00250, -0.00240, 0.00815],
            [0.06315, -0.00105, 0.00295, -0.00195, 0.00995],
            [0.0633, -0.00100, 0.00325, -0.00185, 0.01120],
            [0.06635, -0.00182, 0.00330, -0.00360, 0.01100],
            [0.0678, -0.00248, 0.00333, -0.00480, 0.01150],
            [0.07125, -0.00165, 0.00345, -0.00330, 0.01205],
            [0.07338, -0.00138, 0.00350, -0.00275, 0.01225],
            [0.07533, -0.00120, 0.00350, -0.00245, 0.01240],
            [0.07825, -0.00168, 0.00322, -0.00373, 0.01058],
            [0.0819, -0.00197, 0.00307, -0.00410, 0.01035]
            ])
        )
        eurusd_market_conventions = create_fx_mkt_conventions(
            atm_type = "ATM_DNS_PIPS",
            short_delta_type = "PIPS_SPOT_DELTA",
            long_delta_type = "PIPS_FORWARD_DELTA",
            short_delta_cutoff = "1Y",
            risk_reversal = "RR_CALL_PUT",
            smile_quote_type = "BUTTERFLY_QUOTE",
            currency_pair = "EURUSD"
        )
        #print(eurusd_market_conventions)
        vol_surf_definitions = create_volatility_surface_definition(
            vol_smile_type = "STRIKE_VOL_SMILE",
            smile_method = "SVI_SMILE_METHOD",
            smile_extrap_method = "FLAT_EXTRAP",
            time_interp_method = "LINEAR_IN_VARIANCE",
            time_extrap_method = "FLAT_IN_VOLATILITY",
            day_count_convention = "ACT_365_FIXED",
            vol_type = "LOG_NORMAL_VOL_TYPE",
            wing_strike_type = "DELTA",
            lower = -1e-4,
            upper = 1e-4
        )
        # Build Volatility Surface
        eurusd_vol_surf = fx_volatility_surface_builder(
            as_of_date=as_of_date, 
            currency_pair="EURUSD",
            fx_market_conventions  = eurusd_market_conventions, 
            quotes = eurusd_option_quote_matrix, 
            fx_spot_rate = eurusd_spot_rate,
            dom_discount_curve=usd_depo_curve, 
            for_discount_curve=eur_eurusd_fx_curve,
            vol_surf_definitions = vol_surf_definitions,
            vol_surf_building_settings = [1, 0.5]
            )
        #print(self.eurusd_vol_surf)
        # EURUSD
        eurusd_mkt_data_set = create_fx_mkt_data_set(as_of_date,
                                                        usd_depo_curve,
                                                        eur_eurusd_fx_curve,
                                                        eurusd_spot_rate,
                                                        eurusd_vol_surf)
        # USDCNH
        usdcnh_mkt_data_set = create_fx_mkt_data_set(as_of_date,
                                                        cnh_usdcnh_fx_curve,
                                                        usd_depo_curve,
                                                        usdcnh_spot_rate,
                                                        None)
        #print(self.eurusd_mkt_data_set)
        '''Settings'''
        # BLACK_SCHOLES_MERTON model and ANALYTICAL method 
        bsm_analytical_pricing_settings = create_pricing_settings(
            'USD', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'ANALYTICAL', 
            create_pde_settings(), 
            create_monte_carlo_settings()
            )

        # BLACK_SCHOLES_MERTON model and PDE method
        bsm_pde_pricing_settings = create_pricing_settings(
            'USD', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'PDE', 
            create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP'), 
            create_monte_carlo_settings()
            )

        # BLACK_SCHOLES_MERTON model and MONTE_CARLO method
        bsm_mc_pricing_settings = create_pricing_settings(
            'USD', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'MONTE_CARLO', 
            create_pde_settings(), 
            create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD',False, 1)
            )

        # Duprie Local Vol model and PDE method 
        duprie_pde_pricing_settings = create_pricing_settings(
            'USD', False, 
            create_model_settings('DUPIRE_LOCAL_VOL_MODEL',[201,401,4, 0.001]), 
            'PDE', 
            create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP'), 
            create_monte_carlo_settings()
            )

        # Duprie Local Vol model and MONTE_CARLO method
        duprie_mc_pricing_settings = create_pricing_settings(
            'USD', False, 
            create_model_settings('DUPIRE_LOCAL_VOL_MODEL',[201,401,4, 0.001]), 
            'MONTE_CARLO', 
            create_pde_settings(), 
            create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD', False, 201)
            )
        
        # Create Risk Settings
        risk_settings = create_fx_risk_settings(
            create_ir_curve_risk_settings(
                delta=True, gamma=False, curvature=False, 
                shift=1.0e-4, curvature_shift=5.0e-1, 
                method='CENTRAL_DIFFERENCE_METHOD', granularity='TOTAL_RISK', 
                scaling_factor=1.0e-4, threading_mode='SINGLE_THREADING_MODE'),
            create_price_risk_settings(
                delta=True, gamma=True, curvature=False, 
                shift=1.0e-2, curvature_shift=5.0e-1, 
                method='CENTRAL_DIFFERENCE_METHOD', 
                scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE'), 
            create_vol_risk_settings(
                vega=True, volga=True, 
                shift=1.0e-2, 
                method='CENTRAL_DIFFERENCE_METHOD', granularity='TOTAL_RISK', 
                scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE'),
            create_price_vol_risk_settings(
                vanna=True, 
                price_shift=1.0e-2, vol_shift=1.0e-2, 
                method='CENTRAL_DIFFERENCE_METHOD', granularity='TOTAL_RISK', 
                price_scaling_factor=1.0e-2, vol_scaling_factor=1.0e-2, threading_mode='SINGLE_THREADING_MODE'),             
            create_theta_risk_settings(
                theta=True, shift=1, scaling_factor=1./365.)
            )

        # Create Scenario Analysis Settings
        scenario_analysis_settings = create_scn_analysis_settings(
            scn_analysis_type = 'PRICE_VOL_SCN_ANALYSIS', 
            min_underlying_price=-20e-2, 
            max_underlying_price=20e-2, 
            num_price_scns = 11,
            price_scn_gen_type = 1,
            min_vol = -5.e-2, 
            max_vol = 5.e-2,
            num_vol_scns = 12, 
            vol_scn_gen_type=0,
            threading_mode='SINGLE_THREADING_MODE'
            )

    # Create FX Forward
    fx_forward = create_fx_forward(buy_currency = "EUR",
                                   buy_amount = 1e6,
                                   sell_currency = "USD",
                                   sell_amount = 1.1761e6,
                                   delivery = datetime(2021, 4+3, 1),
                                   expiry = datetime(2021, 3+3, 30))
        
    # Price FX Forward
    fx_forward_result = fx_forward_pricer(pricing_date=as_of_date,
                                 instrument=fx_forward,
                                 mkt_data=eurusd_mkt_data_set,
                                 pricing_settings=create_pricing_settings(
                                    'USD', False, 
                                    create_model_settings(None), 
                                    'ANALYTICAL', 
                                    create_pde_settings(), 
                                    create_monte_carlo_settings()
                                    ),
                                 risk_settings=risk_settings)

    # Create FX Non-Deliverable Forward
    fx_ndf = create_fx_non_deliverable_forwad(buy_currency="USD",
                                                  buy_amount=10000,
                                                  sell_currency="CNH",
                                                  sell_amount=66916,
                                                  delivery_date=datetime(2021, 4+3, 1),
                                                  expiry_date=datetime(2021, 3+3, 30),
                                                  settlement_currency="USD"
                                                  )
        
    # Price FX Non-Deliverable Forward
    fx_ndf_result = fx_ndf_pricer(pricing_date=as_of_date,
                             instrument=fx_ndf,
                             mkt_data=usdcnh_mkt_data_set,
                             pricing_settings=create_pricing_settings(
                                    'USD', False, 
                                    create_model_settings(None), 
                                    'ANALYTICAL', 
                                    create_pde_settings(), 
                                    create_monte_carlo_settings()
                                    ),
                             risk_settings=risk_settings)

    # Create FX Swap
    fx_swap = create_fx_swap(near_buy_currency="EUR",
                                 near_buy_amount=1000000,
                                 near_sell_currency="USD",
                                 near_sell_amount=1176100,
                                 near_delivery_date=datetime(2021, 4+0, 1),
                                 near_expiry_date=None,
                                 far_buy_currency="USD",
                                 far_buy_amount=1000000,
                                 far_sell_currency="EUR",
                                 far_sell_amount=1176100,
                                 far_delivery_date=datetime(2021, 4+3, 1),
                                 far_expiry_date=None)

    # Price FX Swap
    fx_swap_result = fx_swap_pricer(pricing_date=as_of_date,
                                 instrument=fx_swap,
                                 mkt_data=eurusd_mkt_data_set,
                                 pricing_settings=create_pricing_settings(
                                    'USD', False, 
                                    create_model_settings(None), 
                                    'ANALYTICAL', 
                                    create_pde_settings(), 
                                    create_monte_carlo_settings()
                                    ),
                                 risk_settings=risk_settings)

    # Create FX European Option
    european_option = create_european_option(
            payoff_type='CALL',
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            strike=1.176100,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )
        
    # Price FX European Option
    european_option_result = fx_european_option_pricer(
            instrument=european_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX American Option
    american_option = create_american_option(
            payoff_type='CALL',
            expiry=datetime(2021, 9, 26),
            strike=1.176100,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX American Option
    american_option_result = fx_american_option_pricer(
            instrument=american_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX Digital Option
    digital_option = create_digital_option(
            payoff_type='CALL',
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            strike=1.176100,
            cash = 1.0,
            asset= 0.0,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )
        
    # Price FX Digital Option
    digital_option_result = fx_digital_option_pricer(
            instrument=digital_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX Single Barrier Option
    single_barrier_option = create_single_barrier_option(
            payoff_type='CALL',
            strike=1.176100,
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            barrier_type='UP_IN',
            barrier_value=1.176100*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash_rebate=0.0,
            asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX Single Barrier Option
    single_barrier_option_result = fx_single_barrier_option_pricer(
            instrument=single_barrier_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX Double Barrier Option
    double_barrier_option = create_double_barrier_option(
            payoff_type='CALL',
            strike=1.176100,
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=1.176100*0.95,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=1.176100*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            lower_cash_rebate=0.0,
            lower_asset_rebate=0.0,
            upper_cash_rebate=0.0,
            upper_asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX Double Barrier Option
    double_barrier_option_result = fx_double_barrier_option_pricer(
            instrument=double_barrier_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX One Touch Option
    one_touch_option = create_one_touch_option(
            payoff_type='CALL',
            strike=1.176100,
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            touch_type='DOWN_TOUCH',
            lower_barrier_value=1.176100*0.95,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=1.176100*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            lower_cash_rebate=0.0,
            lower_asset_rebate=0.0,
            upper_cash_rebate=0.0,
            upper_asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX One Touch Option
    one_touch_option_result = fx_one_touch_option_pricer(
            instrument=one_touch_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX One Touch Option
    one_touch_option = create_one_touch_option(
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            barrier_type='UP_IN',
            barrier_value=1.176100*1.05,     
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX One Touch Option
    one_touch_option_result = fx_one_touch_option_pricer(
            instrument=one_touch_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=self.scenario_analysis_settings
        )

    # Create FX Double Touch Option
    double_touch_option = create_double_touch_option( 
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=1.176100*0.95,      
            upper_barrier_type='UP_IN',
            upper_barrier_value=1.176100*1.05,       
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX Double Touch Option
    double_touch_option_result = fx_double_touch_option_pricer(
            instrument=double_touch_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create FX Ping Pong Option
    ping_pong_option = create_ping_pong_option(
            expiry=datetime(2021, 9, 26),
            delivery=datetime(2021, 9, 27),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=1.176100*0.95,   
            upper_barrier_type='UP_IN',
            upper_barrier_value=1.176100*1.05, 
            barrier_obs_type='DISCRETE_OBSERVATION_TYPE',
            obs_schedule=[
                    [
                        datetime(2021, 3, 31), datetime(2021, 4, 1), datetime(2021, 4, 2), 
                        datetime(2021, 4, 3), datetime(2021, 4, 4), datetime(2021, 4, 5), 
                        datetime(2021, 4, 6), datetime(2021, 4, 7), datetime(2021, 4, 8), 
                        datetime(2021, 4, 9), datetime(2021, 4, 10), datetime(2021, 4, 11), 
                        datetime(2021, 4, 12), datetime(2021, 4, 13), datetime(2021, 4, 14), 
                        datetime(2021, 4, 15), datetime(2021, 4, 16), datetime(2021, 4, 17), 
                        datetime(2021, 4, 18), datetime(2021, 4, 19), datetime(2021, 4, 20), 
                        datetime(2021, 4, 21), datetime(2021, 4, 22), datetime(2021, 4, 23), 
                        datetime(2021, 4, 24), datetime(2021, 4, 25), datetime(2021, 4, 26), 
                        datetime(2021, 4, 27), datetime(2021, 4, 28), datetime(2021, 4, 29), 
                        datetime(2021, 4, 30), datetime(2021, 5, 1), datetime(2021, 5, 2), 
                        datetime(2021, 5, 3), datetime(2021, 5, 4), datetime(2021, 5, 5), 
                        datetime(2021, 5, 6), datetime(2021, 5, 7), datetime(2021, 5, 8), 
                        datetime(2021, 5, 9), datetime(2021, 5, 10), datetime(2021, 5, 11), 
                        datetime(2021, 5, 12), datetime(2021, 5, 13), datetime(2021, 5, 14), 
                        datetime(2021, 5, 15), datetime(2021, 5, 16), datetime(2021, 5, 17), 
                        datetime(2021, 5, 18), datetime(2021, 5, 19), datetime(2021, 5, 20), 
                        datetime(2021, 5, 21), datetime(2021, 5, 22), datetime(2021, 5, 23), 
                        datetime(2021, 5, 24), datetime(2021, 5, 25), datetime(2021, 5, 26), 
                        datetime(2021, 5, 27), datetime(2021, 5, 28), datetime(2021, 5, 29), 
                        datetime(2021, 5, 30), datetime(2021, 5, 31), datetime(2021, 6, 1), 
                        datetime(2021, 6, 2), datetime(2021, 6, 3), datetime(2021, 6, 4), 
                        datetime(2021, 6, 5), datetime(2021, 6, 6), datetime(2021, 6, 7), 
                        datetime(2021, 6, 8), datetime(2021, 6, 9), datetime(2021, 6, 10), 
                        datetime(2021, 6, 11), datetime(2021, 6, 12), datetime(2021, 6, 13), 
                        datetime(2021, 6, 14), datetime(2021, 6, 15), datetime(2021, 6, 16), 
                        datetime(2021, 6, 17), datetime(2021, 6, 18), datetime(2021, 6, 19), 
                        datetime(2021, 6, 20), datetime(2021, 6, 21), datetime(2021, 6, 22), 
                        datetime(2021, 6, 23), datetime(2021, 6, 24), datetime(2021, 6, 25), 
                        datetime(2021, 6, 26), datetime(2021, 6, 27), datetime(2021, 6, 28), 
                        datetime(2021, 6, 29), datetime(2021, 6, 30), datetime(2021, 7, 1), 
                        datetime(2021, 7, 2), datetime(2021, 7, 3), datetime(2021, 7, 4), 
                        datetime(2021, 7, 5), datetime(2021, 7, 6), datetime(2021, 7, 7), 
                        datetime(2021, 7, 8), datetime(2021, 7, 9), datetime(2021, 7, 10), 
                        datetime(2021, 7, 11), datetime(2021, 7, 12), datetime(2021, 7, 13), 
                        datetime(2021, 7, 14), datetime(2021, 7, 15), datetime(2021, 7, 16), 
                        datetime(2021, 7, 17), datetime(2021, 7, 18), datetime(2021, 7, 19), 
                        datetime(2021, 7, 20), datetime(2021, 7, 21), datetime(2021, 7, 22), 
                        datetime(2021, 7, 23), datetime(2021, 7, 24), datetime(2021, 7, 25), 
                        datetime(2021, 7, 26), datetime(2021, 7, 27), datetime(2021, 7, 28), 
                        datetime(2021, 7, 29), datetime(2021, 7, 30), datetime(2021, 7, 31), 
                        datetime(2021, 8, 1), datetime(2021, 8, 2), datetime(2021, 8, 3), 
                        datetime(2021, 8, 4), datetime(2021, 8, 5), datetime(2021, 8, 6), 
                        datetime(2021, 8, 7), datetime(2021, 8, 8), datetime(2021, 8, 9), 
                        datetime(2021, 8, 10), datetime(2021, 8, 11), datetime(2021, 8, 12), 
                        datetime(2021, 8, 13), datetime(2021, 8, 14), datetime(2021, 8, 15), 
                        datetime(2021, 8, 16), datetime(2021, 8, 17), datetime(2021, 8, 18), 
                        datetime(2021, 8, 19), datetime(2021, 8, 20), datetime(2021, 8, 21), 
                        datetime(2021, 8, 22), datetime(2021, 8, 23), datetime(2021, 8, 24), 
                        datetime(2021, 8, 25), datetime(2021, 8, 26), datetime(2021, 8, 27), 
                        datetime(2021, 8, 28), datetime(2021, 8, 29), datetime(2021, 8, 30), 
                        datetime(2021, 8, 31), datetime(2021, 9, 1), datetime(2021, 9, 2), 
                        datetime(2021, 9, 3), datetime(2021, 9, 4), datetime(2021, 9, 5), 
                        datetime(2021, 9, 6), datetime(2021, 9, 7), datetime(2021, 9, 8), 
                        datetime(2021, 9, 9), datetime(2021, 9, 10), datetime(2021, 9, 11), 
                        datetime(2021, 9, 12), datetime(2021, 9, 13), datetime(2021, 9, 14), 
                        datetime(2021, 9, 15), datetime(2021, 9, 16), datetime(2021, 9, 17), 
                        datetime(2021, 9, 18), datetime(2021, 9, 19), datetime(2021, 9, 20), 
                        datetime(2021, 9, 21), datetime(2021, 9, 22), datetime(2021, 9, 23), 
                        datetime(2021, 9, 24), datetime(2021, 9, 25), datetime(2021, 9, 26)
                    ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],  
            payment_type='PAY_AT_MATURITY',
            cash=0.015,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='USD',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='USD',
            underlying='EURUSD'
        )

    # Price FX Ping Pong Option
    ping_pong_option_result = fx_ping_pong_option_pricer(
            instrument=ping_pong_option,
            pricing_date=as_of_date,
            mkt_data_set=eurusd_mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=self.scenario_analysis_settings
        )