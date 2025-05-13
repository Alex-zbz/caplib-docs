Commodity Derivatives
==================

Examples of commodity derivatives pricing and analysis using caplib.

Commodity Derivatives Pricing
-------------------------

.. code-block:: python

    from datetime import datetime
    from caplib.market import *
    from caplib.analytics import *
    from caplib.cmanalytics import *
    
    # currency
    currency = 'CNY'
    # underlying
    underlying = 'CU.SHFE'

    ''' Mkt Data'''        
    as_of_date = datetime(2020, 2, 21)

    ir_curve = create_ir_yield_curve(
            as_of_date = as_of_date,
            currency='CNY',
            term_dates=[
                datetime(2020, 2, 26), 
                datetime(2020, 3, 2), 
                datetime(2020, 3, 9), 
                datetime(2020, 3, 24), 
                datetime(2020, 5, 24), 
                datetime(2020, 8, 24), 
                datetime(2020, 11, 24), 
                datetime(2021, 2, 24), 
                datetime(2022, 2, 24), 
                datetime(2023, 2, 24), 
                datetime(2024, 2, 24), 
                datetime(2025, 2, 24), 
                datetime(2027, 2, 24), 
                datetime(2030, 2, 24)
            ],
            zero_rates=[
                0.0135486283791684, 0.0197762034605164, 0.0197686053073393, 0.0224838821372655, 0.0241740300538751, 0.0256822601972516, 0.0265096948143765, 0.0271330931714993, 0.0274314991366822, 0.0284834397783798, 0.0297276346662025, 0.0308410887945891, 0.032692683803743, 0.034410206396147
            ],
            curve_name='CNY_SHIBOR_3M'
        )

        
        # Create Option Quote Matrix
    cm_option_quote_matrix = create_cm_option_quote_matrix(
            exercise_type='AMERICAN', 
            underlying_type="FUTURE_UNDERLYING_TYPE", 
            as_of_date = as_of_date,
            term_dates = [
                datetime(2020, 3, 12),
                datetime(2020, 4, 13),
                datetime(2020, 5, 12),
                datetime(2020, 6, 12),
                datetime(2020, 7, 10),
                datetime(2020, 8, 12),
                datetime(2020, 9, 11)
            ], 
            payoff_types = [
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT','PUT',  'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT','PUT',  'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'],
                ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL']
            ],
            strikes = [
                [54000, 55000, 56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000, 82000],
                [54000, 55000, 56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000, 82000],
                [54000, 55000, 56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000, 82000],
                [56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000, 82000],
                [57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000],
                [56000, 57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000, 77000, 78000, 79000, 80000],
                [57000, 58000, 59000, 60000, 61000, 62000, 63000, 64000, 65000, 66000, 67000, 68000, 69000, 70000, 71000, 72000, 73000, 74000, 75000, 76000]
            ],
            prices = [
                [14.00, 16.00, 20.00, 26.00, 38.00, 64.00, 86.00, 130.00, 198.00, 282.00, 400.00, 600.00, 878.00, 1070.00, 660.00, 394.00, 236.00, 142.00, 90.00, 52.00, 32.00, 22.00, 18.00, 14.00, 10.00, 6.00, 6.00],
                [126.00, 126.00, 160.00, 200.00, 250.00, 312.00, 396.00, 478.00, 600.00, 776.00, 974.00, 1230.00, 1602.00, 1736.00, 1276.00, 910.00, 642.00, 460.00, 312.00, 212.00, 150.00, 110.00, 80.00, 58.00, 40.00, 28.00, 38.00],
                [172.00, 192.00, 236.00, 292.00, 426.00, 478.00, 574.00, 702.00, 892.00, 1206.00, 1368.00, 1632.00, 2140.00, 2218.00, 1762.00, 1350.00, 1026.00, 762.00, 562.00, 404.00, 294.00, 210.00, 128.00, 102.00, 58.00, 56.00, 106.00],
                [414.00, 486.00, 584.00, 700.00, 958.00, 1186.00, 1308.00, 1634.00, 2008.00, 2436.00, 2914.00, 2814.00, 2396.00, 2026.00, 1698.00, 1412.00, 758.00, 964.00, 446.00, 346.00, 256.00, 188.00, 138.00, 102.00, 82.00, 44.00],
                [676.00, 798.00, 936.00, 1064.00, 1354.00, 1780.00, 2138.00, 2538.00, 2978.00, 3474.00, 3324.00, 2902.00, 2516.00, 1544.00, 1256.00, 984.00, 806.00, 622.00, 488.00, 382.00, 282.00],
                [678.00, 802.00, 906.00, 1058.00, 1246.00, 1456.00, 2066.00, 2446.00, 2862.00, 3314.00, 3814.00, 3590.00, 3168.00, 2784.00, 2446.00, 2136.00, 1852.00, 1612.00, 1390.00, 630.00, 1026.00, 448.00, 338.00, 278.00, 196.00],
                [1006.00, 1146.00, 1312.00, 1558.00, 1790.00, 2118.00, 2688.00, 3118.00, 3578.00, 4078.00, 3828.00, 3408.00, 3024.00, 2680.00, 2358.00, 2078.00, 1822.00, 1586.00, 1388.00, 666.00]
            ],
            underlying = self.underlying
        )
        
    # Build Volatility Surface
    vol_surf = cm_vol_surface_builder(
            as_of_date=as_of_date, 
            smile_method='SVI_SMILE_METHOD', 
            wing_strike_type='DELTA',
            lower=-1e-5,
            upper=1e-5, 
            option_quote_matrix=cm_option_quote_matrix, 
            underlying_prices=[66810.00, 66750.00, 66620.00, 66620.00, 66490.00, 66460.00, 66380.00],
            discount_curve=ir_curve, 
            fwd_curve=None,
            building_settings = [1, 0.5], 
            underlying=underlying
         )
        
        
    mkt_data_set = create_cm_mkt_data_set(
            as_of_date=as_of_date, 
            discount_curve=ir_curve,
            underlying_price=66380.00, 
            vol_surf=vol_surf,
            underlying=underlying)

    # Create Pricing Settings with BLACK_SCHOLES_MERTON model and ANALYTICAL method 
    bsm_analytical_pricing_settings = create_pricing_settings(
            'CNY', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'ANALYTICAL', 
            create_pde_settings(), 
            create_monte_carlo_settings()
            )

    # Create Pricing Settings with BLACK_SCHOLES_MERTON model and PDE method
    bsm_pde_pricing_settings = create_pricing_settings(
            'CNY', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'PDE', 
            create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP'), 
            create_monte_carlo_settings()
            )

    # Create Pricing Settings with BLACK_SCHOLES_MERTON model and MONTE_CARLO method
    bsm_mc_pricing_settings = create_pricing_settings(
            'CNY', False, 
            create_model_settings('BLACK_SCHOLES_MERTON'), 
            'MONTE_CARLO', 
            create_pde_settings(), 
            create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD',False, 1)
            )

    # Create Pricing Settings with Duprie Local Vol model and PDE method 
    duprie_pde_pricing_settings = create_pricing_settings(
            'CNY', False, 
            create_model_settings('DUPIRE_LOCAL_VOL_MODEL',[201,401,4, 0.001]), 
            'PDE', 
            create_pde_settings(201, 401, -5, 5, 'MMT_NUM_STDEVS', 0.001, 'ADAPTIVE_GRID', 'CUBIC_SPLINE_INTERP'), 
            create_monte_carlo_settings()
            )

    # Create Pricing Settings with Duprie Local Vol model and MONTE_CARLO method
    duprie_mc_pricing_settings = create_pricing_settings(
            'CNY', False, 
            create_model_settings('DUPIRE_LOCAL_VOL_MODEL',[201,401,4, 0.001]), 
            'MONTE_CARLO', 
            create_pde_settings(), 
            create_monte_carlo_settings(8096, 'SOBOL_NUMBER', 1023, 'BROWNIAN_BRIDGE_METHOD', 'INVERSE_CUMULATIVE_METHOD', False, 201)
            )
        
    # Create Risk Settings
    risk_settings = create_cm_risk_settings(
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
            create_dividend_curve_risk_settings(
                delta=True, gamma=False, 
                shift=1.0e-4, 
                method="CENTRAL_DIFFERENCE_METHOD", granularity="TOTAL_RISK", 
                scaling_factor=1.0e-4, threading_mode="SINGLE_THREADING_MODE"), 
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

    # Create European Option
    european_option = create_european_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike=66380.00,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )
    # Price European Option
    european_option_result = cm_european_option_pricer(
            instrument=european_option,
            pricing_date=as_of_date,
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create American Option
    american_option = create_american_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            strike=66380.00,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price American Option
    american_option_result = cm_american_option_pricer(
            instrument=american_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Asian Option
    asian_option = create_asian_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike_type='FIXED_STRIKE',
            strike=66380.00,
            avg_method='ARITHMETIC_AVERAGE_METHOD',
            obs_type='DISCRETE_OBSERVATION_TYPE',
            fixing_schedule= [
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],                
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Asian Option
    asian_option_result = cm_asian_option_pricer(
            instrument=asian_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Digital Option Pricing
    # Create Digital Option Instrument
    digital_option = create_digital_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike=66380.00,
            cash = 1.0,
            asset= 0.0,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )
        
    # Price Digital Option
    digital_option_result = cm_digital_option_pricer(
            instrument=digital_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Single Barrier Option Instrument
    single_barrier_option = create_single_barrier_option(
            payoff_type='CALL',
            strike=66380.00,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP_IN',
            barrier_value=66380.00*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash_rebate=0.0,
            asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Single Barrier Option
    single_barrier_option_result = cm_single_barrier_option_pricer(
            instrument=single_barrier_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Double Barrier Option Instrument
    double_barrier_option = create_double_barrier_option(
            payoff_type='CALL',
            strike=66380.00,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=66380.00*0.95,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=66380.00*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            lower_cash_rebate=0.0,
            lower_asset_rebate=0.0,
            upper_cash_rebate=0.0,
            upper_asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Double Barrier Option
    double_barrier_option_result = cm_double_barrier_option_pricer(
            instrument=double_barrier_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create One Touch Option Instrument
    one_touch_option = create_one_touch_option(            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP_IN',
            barrier_value=66380.00*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price One Touch Option
    one_touch_option_result = cm_one_touch_option_pricer(
            instrument=one_touch_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Double Touch Option Instrument
    double_touch_option = create_double_touch_option(            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=66380.00*0.95,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=66380.00*1.05,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Double Touch Option
    double_touch_option_result = cm_double_touch_option_pricer(
            instrument=double_touch_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Single Shark Fin Option Instrument
    single_shark_fin_option = create_single_shark_fin_option(
            payoff_type='CALL',
            strike=66380.00,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            gearing = 1.0,
            performance_type='RELATIVE_PERFORM_TYPE',
            barrier_type='UP_OUT',
            barrier_value=66380.00*1.05,    
            barrier_obs_type='DISCRETE_OBSERVATION_TYPE',
            obs_schedule=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],
            payment_type='PAY_AT_MATURITY',
            cash_rebate=0.0,
            asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Single Shark Fin Option
    single_shark_fin_option_result = cm_single_shark_fin_option_pricer(
            instrument=single_shark_fin_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Double Shark Fin Option Instrument
    double_shark_fin_option = create_double_shark_fin_option(
            lower_strike=66380.00,
            upper_strike=66380.00,            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_participation = 1.0,
            upper_participation = 1.0,
            performance_type='ABSOLUTE_PERFORM_TYPE',
            lower_barrier=66380.00*0.95,    
            upper_barrier=66380.00*1.05,                
            barrier_obs_type='DISCRETE_OBSERVATION_TYPE',
            obs_schedule=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],
            payment_type='PAY_AT_MATURITY',
            lower_cash_rebate=0.0,
            lower_asset_rebate=0.0,
            upper_cash_rebate=0.0,
            upper_asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

        # Price Double Shark Fin Option
        double_shark_fin_option_result = cm_double_shark_fin_option_pricer(
            instrument=double_shark_fin_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Range Accrual Option Instrument
    range_accrual_option = create_range_accrual_option(
            expiry_date=datetime(2020, 8, 19),
            delivery_date=datetime(2020, 8, 20),
            cash=0.01,
            asset=0.0,
            lower_barrier=66380.00*0.95,    
            upper_barrier=66380.00*1.05, 
            obs_schedule=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],   
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Range Accrual Option
    range_accrual_option_result = cm_range_accrual_option_pricer(
            instrument=range_accrual_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Airbag Option Instrument
    airbag_option = create_airbag_option(
            payoff_type='CALL',                    
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_strike=66380.00,
            upper_strike=66380.00*1.05,    
            lower_participation = 1.0,
            upper_participation = 1.0,
            knock_in_strike = 66380.00,
            barrier_type='DOWN_IN',
            barrier_value=66380.00*0.8,                
            barrier_obs_type='DISCRETE_OBSERVATION_TYPE',
            obs_schedule=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],            
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Airbag Option
    airbag_option_result = cm_airbag_option_pricer(
            instrument=airbag_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Ping Pong Option Instrument
    ping_pong_option = create_ping_pong_option(
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=66380.00*0.95,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=66380.00*1.05,    
            barrier_obs_type='DISCRETE_OBSERVATION_TYPE',
            obs_schedule=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],  
            payment_type='PAY_AT_MATURITY',
            cash=0.015,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Ping Pong Option
    ping_pong_option_result = cm_ping_pong_option_pricer(
            instrument=ping_pong_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Phoenix Auto Callable Note Instrument
    phoenix_auto_callable_note = create_phoenix_auto_callable_note(
            coupon_payoff_type = 'CALL',
            coupon_strike=66380.00,
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 22),
            coupon_dates=[datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
            day_count='ACT_365_FIXED',
            knock_out_barrier_type ='UP_OUT',
            knock_out_barrier_value=66380.00*1.1,
            knock_out_sched=[
                [datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
                [0.0] * 6,
                [1.0] * 6
            ],
            knock_in_barrier_type ='DOWN_IN',
            knock_in_barrier_value=66380.00*0.9,
            knock_in_sched=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],  
            long_short='SELL',
            knock_in_payoff_type='PUT',
            knock_in_payoff_strike=66380.00*0.85,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )
        
    # Price Phoenix Auto Callable Note
    phoenix_auto_callable_note_result = cm_phoenix_auto_callable_note_pricer(
            instrument=phoenix_auto_callable_note,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Create Snowball Auto Callable Note Instrument
    snowball_auto_callable_note = create_snowball_auto_callable_note(
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 21),
            coupon_dates=[datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
            day_count='ACT_365_FIXED',
            knock_out_barrier_type ='UP_OUT',
            knock_out_barrier_value=66380.00*1.05,
            knock_out_sched=[
                [datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
                [0.0] * 6,
                [1.0] * 6
            ],
            knock_in_barrier_type ='DOWN_IN',
            knock_in_barrier_value=66380.00*0.80,
            knock_in_sched=[
                    [
                        datetime(2020,2,22), datetime(2020,2,23), datetime(2020,2,24),
                        datetime(2020,2,25), datetime(2020,2,26), datetime(2020,2,27),
                        datetime(2020,2,28), datetime(2020,2,29), datetime(2020,3,1),
                        datetime(2020,3,2), datetime(2020,3,3), datetime(2020,3,4),
                        datetime(2020,3,5), datetime(2020,3,6), datetime(2020,3,7),
                        datetime(2020,3,8), datetime(2020,3,9), datetime(2020,3,10),
                        datetime(2020,3,11), datetime(2020,3,12), datetime(2020,3,13),
                        datetime(2020,3,14), datetime(2020,3,15), datetime(2020,3,16),
                        datetime(2020,3,17), datetime(2020,3,18), datetime(2020,3,19),
                        datetime(2020,3,20), datetime(2020,3,21), datetime(2020,3,22),
                        datetime(2020,3,23), datetime(2020,3,24), datetime(2020,3,25),
                        datetime(2020,3,26), datetime(2020,3,27), datetime(2020,3,28),
                        datetime(2020,3,29), datetime(2020,3,30), datetime(2020,3,31),
                        datetime(2020,4,1), datetime(2020,4,2), datetime(2020,4,3),
                        datetime(2020,4,4), datetime(2020,4,5), datetime(2020,4,6),
                        datetime(2020,4,7), datetime(2020,4,8), datetime(2020,4,9),
                        datetime(2020,4,10), datetime(2020,4,11), datetime(2020,4,12),
                        datetime(2020,4,13), datetime(2020,4,14), datetime(2020,4,15),
                        datetime(2020,4,16), datetime(2020,4,17), datetime(2020,4,18),
                        datetime(2020,4,19), datetime(2020,4,20), datetime(2020,4,21),
                        datetime(2020,4,22), datetime(2020,4,23), datetime(2020,4,24),
                        datetime(2020,4,25), datetime(2020,4,26), datetime(2020,4,27),
                        datetime(2020,4,28), datetime(2020,4,29), datetime(2020,4,30),
                        datetime(2020,5,1), datetime(2020,5,2), datetime(2020,5,3),
                        datetime(2020,5,4), datetime(2020,5,5), datetime(2020,5,6),
                        datetime(2020,5,7), datetime(2020,5,8), datetime(2020,5,9),
                        datetime(2020,5,10), datetime(2020,5,11), datetime(2020,5,12),
                        datetime(2020,5,13), datetime(2020,5,14), datetime(2020,5,15),
                        datetime(2020,5,16), datetime(2020,5,17), datetime(2020,5,18),
                        datetime(2020,5,19), datetime(2020,5,20), datetime(2020,5,21),
                        datetime(2020,5,22), datetime(2020,5,23), datetime(2020,5,24),
                        datetime(2020,5,25), datetime(2020,5,26), datetime(2020,5,27),
                        datetime(2020,5,28), datetime(2020,5,29), datetime(2020,5,30),
                        datetime(2020,5,31), datetime(2020,6,1), datetime(2020,6,2),
                        datetime(2020,6,3), datetime(2020,6,4), datetime(2020,6,5),
                        datetime(2020,6,6), datetime(2020,6,7), datetime(2020,6,8),
                        datetime(2020,6,9), datetime(2020,6,10), datetime(2020,6,11),
                        datetime(2020,6,12), datetime(2020,6,13), datetime(2020,6,14),
                        datetime(2020,6,15), datetime(2020,6,16), datetime(2020,6,17),
                        datetime(2020,6,18), datetime(2020,6,19), datetime(2020,6,20),
                        datetime(2020,6,21), datetime(2020,6,22), datetime(2020,6,23),
                        datetime(2020,6,24), datetime(2020,6,25), datetime(2020,6,26),
                        datetime(2020,6,27), datetime(2020,6,28), datetime(2020,6,29),
                        datetime(2020,6,30), datetime(2020,7,1), datetime(2020,7,2),
                        datetime(2020,7,3), datetime(2020,7,4), datetime(2020,7,5),
                        datetime(2020,7,6), datetime(2020,7,7), datetime(2020,7,8),
                        datetime(2020,7,9), datetime(2020,7,10), datetime(2020,7,11),
                        datetime(2020,7,12), datetime(2020,7,13), datetime(2020,7,14),
                        datetime(2020,7,15), datetime(2020,7,16), datetime(2020,7,17),
                        datetime(2020,7,18), datetime(2020,7,19), datetime(2020,7,20),
                        datetime(2020,7,21), datetime(2020,7,22), datetime(2020,7,23),
                        datetime(2020,7,24), datetime(2020,7,25), datetime(2020,7,26),
                        datetime(2020,7,27), datetime(2020,7,28), datetime(2020,7,29),
                        datetime(2020,7,30), datetime(2020,7,31), datetime(2020,8,1),
                        datetime(2020,8,2), datetime(2020,8,3), datetime(2020,8,4),
                        datetime(2020,8,5), datetime(2020,8,6), datetime(2020,8,7),
                        datetime(2020,8,8), datetime(2020,8,9), datetime(2020,8,10),
                        datetime(2020,8,11), datetime(2020,8,12), datetime(2020,8,13),
                        datetime(2020,8,14), datetime(2020,8,15), datetime(2020,8,16),
                        datetime(2020,8,17), datetime(2020,8,18), datetime(2020,8,19)
                ],
                [0] * 180,  # All values are 0
                [1] * 180  # All weights are 1
            ],  
            long_short='SELL',
            knock_in_payoff_type='PUT',
            knock_in_payoff_strike=66380.00*1.0,
            knock_in_payoff_gearing = 1.0,
            reference_price = 66380.00,
            expiry=datetime(2020, 8, 22),
            delivery=datetime(2020, 8, 22),
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='FUTURE_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Snowball Auto Callable Note
    snowball_auto_callable_note_result = cm_snowball_auto_callable_note_pricer(
            instrument=snowball_auto_callable_note,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )