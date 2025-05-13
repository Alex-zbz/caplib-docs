Equity Derivatives
==================

Examples of equity derivatives pricing and analysis using caplib.

Equity Derivatives Pricing
-------------------------

.. code-block:: python

    from datetime import datetime
    from caplib.market import *
    from caplib.analytics import *
    from caplib.eqanalytics import *
    
    # Create Risk Settings
    risk_settings = create_eq_risk_settings(
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

    # currency
    currency = 'CNY'
    # underlying
    underlying = '50ETF.SSE'

    # Create Market Data
    as_of_date = datetime(2020, 2, 21)
        
    # Discount curve
    ir_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency=currency,
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
            0.0135486283791684, 
            0.0197762034605164, 
            0.0197686053073393, 
            0.0224838821372655, 
            0.0241740300538751, 
            0.0256822601972516, 
            0.0265096948143765, 
            0.0271330931714993, 
            0.0274314991366822, 
            0.0284834397783798, 
            0.0297276346662025, 
            0.0308410887945891, 
            0.032692683803743, 
            0.034410206396147
        ],
        curve_name='CNY_SHIBOR_3M'
    )

    # equity spot price
    underlying_price = 2.958

    # dividend curve
    dividend_curve = create_dividend_curve(
        as_of_date = as_of_date,
        pillar_dates=[
            datetime(2020, 2, 26), 
            datetime(2020, 3, 25), 
            datetime(2020, 6, 24), 
            datetime(2020, 9, 23)
        ],
        pillar_values=[
            0.05361055758784821,
            0.01338941242891319, 
            -0.001765240983827533, 
            -0.002594662370949712
        ],
        dividend_type='CONTINUOUS_DIVIDEND',
        interp_method='LINEAR_INTERP',
        extrap_method='FLAT_EXTRAP',
        day_count='ACTUAL_365_FIXED',
        yield_start_date=as_of_date,
        pillar_names=None,
        curve_name='DIVIDEND_CURVE_50ETF'
    )

    # Create Option Quote Matrix
    eq_option_quote_matrix = create_eq_option_quote_matrix(
        exercise_type='EUROPEAN', 
        underlying_type="SPOT_UNDERLYING_TYPE", 
        as_of_date = as_of_date,
        term_dates = [
            datetime(2020, 2, 26), 
            datetime(2020, 3, 25), 
            datetime(2020, 6, 24), 
            datetime(2020, 9, 23)
        ], 
        payoff_types = [
            ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'], 
            ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'], 
            ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL'], 
            ['PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'PUT', 'CALL', 'CALL', 'CALL', 'CALL', 'CALL']
        ],
        option_prices = [
            [0.0002, 0.0002, 0.0002, 0.0002, 0.0004, 0.0008, 0.0015, 0.0023, 0.0065, 0.0184, 0.0053, 0.0012, 0.0005, 0.0001, 0.0001], 
            [0.0027, 0.0033, 0.004, 0.0054, 0.0081, 0.0113, 0.0172, 0.027, 0.04, 0.0608, 0.0498, 0.0216, 0.011, 0.0066, 0.0046], 
            [0.0201, 0.023, 0.0281, 0.0345, 0.0433, 0.0541, 0.0668, 0.0818, 0.1004, 0.1229, 0.1325, 0.0935, 0.0659, 0.047, 0.033], 
            [0.0365, 0.0434, 0.0516, 0.0612, 0.0724, 0.0862, 0.1015, 0.1184, 0.1381, 0.1595, 0.193, 0.1483, 0.1298, 0.0897, 0.0702]
        ],
        option_strikes = [
            [2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.1, 3.2, 3.3, 3.4], 
            [2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.1, 3.2, 3.3, 3.4], 
            [2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.1, 3.2, 3.3, 3.4], 
            [2.5, 2.55, 2.6, 2.65, 2.7, 2.75, 2.8, 2.85, 2.9, 2.95, 3.0, 3.1, 3.2, 3.3, 3.4]
        ],
        underlying = underlying
    )

    # Build Volatility Surface
    vol_surf = eq_vol_surface_builder(
        as_of_date=as_of_date, 
        smile_method='SVI_SMILE_METHOD', 
        wing_strike_type='DELTA',
        lower=-1e-5,
        upper=1e-5, 
        option_quote_matrix=eq_option_quote_matrix, 
        underlying_prices=[underlying_price],
        discount_curve=ir_curve, 
        dividend_curve=dividend_curve,
        pricing_settings=bsm_analytical_pricing_settings,
        building_settings = [1, 0.5], 
        underlying=underlying
    )

    # Quanto market data
    quanto_discount_curve = create_flat_ir_yield_curve(as_of_date, 'USD', 0.0)
    quanto_fx_vol_curve = create_flat_vol_curve(as_of_date, 0.0)
    quanto_correlation = 0.0
    
    # Create market data set
    mkt_data_set = create_eq_mkt_data_set(
        as_of_date=as_of_date, 
        discount_curve=ir_curve,
        underlying_price=underlying_price, 
        vol_surf=vol_surf,
        dividend_curve=dividend_curve, 
        quanto_discount_curve=quanto_discount_curve,
        quanto_fx_vol_curve=quanto_fx_vol_curve, 
        quanto_correlation=quanto_correlation,
        underlying=underlying)
    
    # Eurpean Option Pricing
    # Create European Option Instrument
    european_option = create_european_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike=2.958,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price European Option
    european_option_result = eq_european_option_pricer(
            instrument=european_option,
            pricing_date=as_of_date,
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )
    
    # American Option Pricing
    # Create American Option Instrument
    american_option = create_american_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            strike=2.958,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price American Option
    american_option_result = eq_american_option_pricer(
            instrument=american_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )
    
    # Asian Option Pricing
    # Create Asian Option Instrument
    asian_option = create_asian_option(
            payoff_type='CALL',
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            strike_type='FIXED_STRIKE',
            strike=2.958,
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    asian_option_result = eq_asian_option_pricer(
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
            strike=2.958,
            cash = 1.0,
            asset= 0.0,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )
        
    # Price Digital Option
    digital_option_result = eq_digital_option_pricer(
            instrument=digital_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Single Barrier Option Pricing
    # Create Single Barrier Option Instrument
    single_barrier_option = create_single_barrier_option(
            payoff_type='CALL',
            strike=2.958,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP_IN',
            barrier_value=3.2538,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash_rebate=0.0,
            asset_rebate=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )
    
    # Price Single Barrier Option
    single_barrier_option_result = eq_single_barrier_option_pricer(
            instrument=single_barrier_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Double Barrier Option Pricing
    # Create Double Barrier Option Instrument
    double_barrier_option = create_double_barrier_option(
            payoff_type='CALL',
            strike=2.958,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=2.810,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=3.106,    
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Double Barrier Option
    double_barrier_option_result = eq_double_barrier_option_pricer(
            instrument=double_barrier_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # One Touch Option Pricing
    # Create One Touch Option Instrument
    one_touch_option = create_one_touch_option(            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            barrier_type='UP_IN',
            barrier_value=3.106,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price One Touch Option
    one_touch_option_result = eq_one_touch_option_pricer(
            instrument=one_touch_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Double Touch Option Pricing
    # Create Double Touch Option Instrument
    double_touch_option = create_double_touch_option(            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=2.810,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=3.106,    
            barrier_obs_type='CONTINUOUS_OBSERVATION_TYPE',
            obs_schedule=[[],[],[]],
            payment_type='PAY_AT_MATURITY',
            cash=1.0,
            asset=0.0,
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Double Touch Option
    double_touch_option_result = eq_double_touch_option_pricer(
            instrument=double_touch_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )  

    # Single Shark Fin Option Pricing
    # Create Single Shark Fin Option Instrument
    single_shark_fin_option = create_single_shark_fin_option(
            payoff_type='CALL',
            strike=2.958,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            gearing = 1.0,
            performance_type='RELATIVE_PERFORM_TYPE',
            barrier_type='UP_OUT',
            barrier_value=3.10590,    
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Single Shark Fin Option
    single_shark_fin_option_result = eq_single_shark_fin_option_pricer(
            instrument=single_shark_fin_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )  

    # Double Shark Fin Option Pricing
    # Create Double Shark Fin Option Instrument
    double_shark_fin_option = create_double_shark_fin_option(
            lower_strike=2.958,
            upper_strike=2.958,            
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_participation = 1.0,
            upper_participation = 1.0,
            performance_type='ABSOLUTE_PERFORM_TYPE',
            lower_barrier=2.662200,    
            upper_barrier=3.253800,                
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Double Shark Fin Option
    double_shark_fin_option_result = eq_double_shark_fin_option_pricer(
            instrument=double_shark_fin_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Range Accrual Option Pricing
    # Create Range Accrual Option Instrument
    range_accrual_option = create_range_accrual_option(
            expiry_date=datetime(2020, 8, 19),
            delivery_date=datetime(2020, 8, 20),
            cash=0.01,
            asset=0.0,
            lower_barrier=2.662200,    
            upper_barrier=3.253800, 
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Range Accrual Option
    range_accrual_option_result = eq_range_accrual_option_pricer(
            instrument=range_accrual_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_analytical_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Airbag Option Pricing
    # Create Airbag Option Instrument
    airbag_option = create_airbag_option(
            payoff_type='CALL',                    
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_strike=2.958,
            upper_strike=3.54960,    
            lower_participation = 1.0,
            upper_participation = 1.0,
            knock_in_strike = 2.958,
            barrier_type='DOWN_IN',
            barrier_value=2.36640,                
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Airbag Option
    airbag_option_result = eq_airbag_option_pricer(
            instrument=airbag_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_pde_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Ping Pong Option Pricing
    # Create Ping Pong Option Instrument
    ping_pong_option = create_ping_pong_option(
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            lower_barrier_type='DOWN_IN',
            lower_barrier_value=2.810,    
            upper_barrier_type='UP_IN',
            upper_barrier_value=3.106,    
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
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Ping Pong Option
    ping_pong_option_result = eq_ping_pong_option_pricer(
            instrument=ping_pong_option,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

    # Phoenix Auto Callable Note Pricing
    # Create Phoenix Auto Callable Note Instrument
    phoenix_auto_callable_note = create_phoenix_auto_callable_note(
            coupon_payoff_type = 'CALL',
            coupon_strike=2.958,
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 22),
            coupon_dates=[datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
            day_count='ACT_365_FIXED',
            knock_out_barrier_type ='UP_OUT',
            knock_out_barrier_value=3.25380,
            knock_out_sched=[
                [datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
                [0.0] * 6,
                [1.0] * 6
            ],
            knock_in_barrier_type ='DOWN_IN',
            knock_in_barrier_value=2.66220,
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
            knock_in_payoff_strike=2.514300,
            expiry=datetime(2020, 8, 19),
            delivery=datetime(2020, 8, 20),
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Phoenix Auto Callable Note
    phoenix_auto_callable_note_result = eq_phoenix_auto_callable_note_pricer(
            instrument=phoenix_auto_callable_note,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )
    
    # Snowball Auto Callable Note Pricing
    # Create Snowball Auto Callable Note Instrument
    snowball_auto_callable_note = create_snowball_auto_callable_note(
            coupon_rate=0.12,
            start_date=datetime(2020, 2, 21),
            coupon_dates=[datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
            day_count='ACT_365_FIXED',
            knock_out_barrier_type ='UP_OUT',
            knock_out_barrier_value=3.25380,
            knock_out_sched=[
                [datetime(2020, 3, 23), datetime(2020, 4, 22), datetime(2020, 5, 22), datetime(2020, 6, 22), datetime(2020, 7, 23),datetime(2020, 8, 22)],
                [0.0] * 6,
                [1.0] * 6
            ],
            knock_in_barrier_type ='DOWN_IN',
            knock_in_barrier_value=2.66220,
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
            knock_in_payoff_strike=2.514300,
            knock_in_payoff_gearing = 1.0,
            reference_price = 2.958,
            expiry=datetime(2020, 8, 22),
            delivery=datetime(2020, 8, 22),
            settlement_days=1,
            nominal=1000000.0,
            payoff_ccy='CNY',
            underlying_type='SPOT_UNDERLYING_TYPE',
            underlying_ccy='CNY',
            underlying=underlying
        )

    # Price Snowball Auto Callable Note
    snowball_auto_callable_note_result = eq_snowball_auto_callable_note_pricer(
            instrument=snowball_auto_callable_note,
            pricing_date=datetime(2020, 2, 21),
            mkt_data_set=mkt_data_set,
            pricing_settings=bsm_mc_pricing_settings,
            risk_settings=risk_settings,
            scn_settings=scenario_analysis_settings
        )

