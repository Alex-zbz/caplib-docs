Interest Rate Derivatives
========================

Examples of Interest Rate Derivatives analytics using caplib.

Interest Rate Derivatives Pricing
---------------------------------

.. code-block:: python

    from datetime import datetime
    from caplib.analytics import *
    from caplib.fxmarket import create_fx_swap_template
    from caplib.iranalytics import *
    from caplib.irmarket import *
    
    
    
    # Create fixed leg
    fixed_leg = create_fixed_leg_definition('cny', 
                                            'cal_cfets', 
                                            'QUARTERLY',
                                            day_count='ACT_360',
                                            interest_day_convention='MODIFIED_FOLLOWING',
                                            stub_policy='INITIAL',
                                            broken_period_type='LONG',
                                            pay_day_offset=0, pay_day_convention='MODIFIED_FOLLOWING',
                                            fixing_day_convention='MODIFIED_PRECEDING', fixing_mode='IN_ADVANCE',
                                            fixing_day_offset=-1,
                                            notional_exchange='INVALID_NOTIONAL_EXCHANGE')
    
    # Create floating leg
    floating_leg = create_floating_leg_definition('cny', 
                                                'shibor_3m', 
                                                'cal_cfets', 
                                                ['cal_cfets'], 
                                                'QUARTERLY',
                                                'QUARTERLY',
                                                day_count='ACT_360',
                                                payment_discount_method='NO_DISCOUNT',
                                                rate_calc_method='STANDARD',
                                                spread=False,
                                                interest_day_convention='MODIFIED_FOLLOWING',
                                                stub_policy='INITIAL',
                                                broken_period_type='LONG',
                                                pay_day_offset=0, pay_day_convention='MODIFIED_FOLLOWING',
                                                fixing_day_convention='MODIFIED_PRECEDING', fixing_mode='IN_ADVANCE',
                                                fixing_day_offset=-1,
                                                notional_exchange='INVALID_NOTIONAL_EXCHANGE')
    
    # Create swap template
    cny_shibor_3m_swap_template = create_ir_vanilla_swap_template('cny_shibor_3m',
                                                                  1,
                                                                  fixed_leg,
                                                                  floating_leg,
                                                                  'SPOTSTART')
    
    # Create leg fixings
    leg_fixings = create_leg_fixings(
        [
            ['shibor_3m', 
            create_time_series(
                [datetime(2022, 3, 3), datetime(2022, 3, 4)],
                [0.1, 0.3],
                'TS_FORWARD_MODE',
                'shibor_3m'
                )
            ]
        ]
    )
    
    # Build interest rate vanilla swap
    cny_shibor_3m_swap = build_ir_vanilla_instrument('PAY', 
                                      0.05, 
                                      0.0,
                                      datetime(2022, 3, 7), 
                                      datetime(2023, 3, 7),
                                      cny_shibor_3m_swap_template, 
                                      1000000,
                                      leg_fixings)
    # Market data
    as_of_date = datetime(2022, 12, 5)
    # CNY SHIBOR 3M Curve
    cny_shibor_3m_curve = create_ir_yield_curve(as_of_date, 
                                                currency='CNY',
                                                term_dates=[
                                                    datetime(2022, 12, 7),
                                                    datetime(2022, 12, 13),
                                                    datetime(2022, 12, 20),
                                                    datetime(2023, 1, 6),
                                                    datetime(2023, 3, 6),
                                                    datetime(2023, 6, 6),
                                                    datetime(2023, 9, 6),
                                                    datetime(2023, 12, 6),
                                                    datetime(2024, 12, 6),
                                                    datetime(2025, 12, 8),
                                                    datetime(2026, 12, 7),
                                                    datetime(2027, 12, 6),
                                                    datetime(2029, 12, 6),
                                                    datetime(2032, 12, 6)
                                                ],
                                                zero_rates=[
                                                    0.026889,
                                                    0.026936,
                                                    0.027940,
                                                    0.026348,
                                                    0.026478,
                                                    0.027785,
                                                    0.028543,
                                                    0.028961,
                                                    0.029905,
                                                    0.030712,
                                                    0.031695,
                                                    0.032667,
                                                    0.034370,
                                                    0.036047
                                                ],
                                                day_count='ACT_365_FIXED',
                                                interp_method='LINEAR_INTERP',
                                                extrap_method='FLAT_EXTRAP',
                                                compounding_type='CONTINUOUS_COMPOUNDING',
                                                frequency='ANNUAL',
                                                jacobian=[0.0],
                                                curve_name='CNY_SHIBOR_3M',
                                                pillar_names=[
                                                    '1D',
                                                    '1W',
                                                    '2W',
                                                    '1M',
                                                    '3M',
                                                    '6M',
                                                    '9M',
                                                    '1Y',
                                                    '2Y',
                                                    '3Y',
                                                    '4Y',
                                                    '5Y',
                                                    '7Y',
                                                    '10Y'
                                                ])

    
    mkt_data = create_ir_mkt_data_set(as_of_date, 
                                      cny_shibor_3m_curve,
                                      ['shibor_3m'],
                                      [cny_shibor_3m_curve])
    # Pricing settings
    pricing_settings = create_model_free_pricing_settings('CNY', 
                                                         True, 
                                                         cash_flows=True)
    # Risk settings
    risk_settings = create_ir_risk_settings(create_ir_curve_risk_settings(True, 
                                                         True, 
                                                         1e-4, 
                                                         50e-4, 
                                                         'CENTRAL_DIFFERENCE_METHOD',
                                                         'TERM_BUCKET_RISK'),
                                            create_theta_risk_settings(True))
    # Pricing
    result = ir_vanilla_instrument_pricer(cny_shibor_3m_swap, 
                                         as_of_date, 
                                         mkt_data, 
                                         pricing_settings, 
                                         risk_settings)
    
    
IR Yield Curve Construction
----------------

.. code-block:: python

    from datetime import datetime
    from caplib.analytics import *
    from caplib.fxmarket import create_fx_swap_template
    from caplib.iranalytics import *
    from caplib.irmarket import *

    as_of_date = datetime(2023, 3, 3)

    currency = 'CNY'
    curve_name = 'CNY_FR_007'

    discount_curves = {'CNY': 'CNY_FR_007'}
    forward_curves = {'FR_007': 'CNY_FR_007'}
    build_settings = create_ir_curve_build_settings(
        curve_name, 
        discount_curves, 
        forward_curves, 
        False)

    inst_names = [
        'CNY_FR_001',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007',
        'CNY_FR_007'
    ]
    inst_types = [
        'DEPOSIT',
        'DEPOSIT',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP',
        'IR_VANILLA_SWAP'
    ]
    inst_terms = [
        '1D',
        '7D',
        '3M',
        '6M',
        '9M',
        '1Y',
        '2Y',
        '3Y',
        '4Y',
        '5Y',
        '7Y',
        '10Y'
    ]
    factors = [
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100,
        100
    ]
    quotes = [
        1.3500,
        2.0000,
        2.3575,
        2.3663,
        2.3925,
        2.4321,
        2.5790,
        2.7113,
        2.8842,
        2.9072,
        3.1090,
        3.1525
    ]
    
    par_curve = create_ir_par_rate_curve(
        as_of_date, 
        currency, 
        curve_name,
        inst_names, 
        inst_types, 
        inst_terms, 
        factors, 
        quotes)
    par_curves = [par_curve]
           
    yield_curve = ir_single_ccy_curve_builder(
        as_of_date, 
        target_curve_names=  [curve_name], 
        build_settings = [build_settings], 
        par_curves= [par_curve],
        day_count = 'ACT_365_FIXED',
        compounding_type = 'CONTINUOUS_COMPOUNDING',
        frequency = 'ANNUAL',
        other_curves = [],
        building_method = 'BOOTSTRAPPING_METHOD')
        