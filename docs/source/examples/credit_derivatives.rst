Credit
======

Examples of credit derivatives modeling and pricing with caplib.

Credit Default Swaps
------------------

.. code-block:: python

    from datetime import datetime
    from caplib.analytics import create_ir_yield_curve, create_credit_curve
    from caplib.crmarket import build_credit_default_swap
    from caplib.cranalytics import create_cr_mkt_data_set, credit_default_swap_pricer, create_cds_pricing_settings, create_cr_risk_settings
    
    inst = build_credit_default_swap(nominal = 1000000.00,
                                    currency = 'CNY',
                                    issue_date = datetime(2019, 6, 20),
                                    maturity = datetime(2024, 6, 20),
                                    protection_leg_pay_receive = 'PAY',
                                    protection_leg_settlement_type = 'CASH_SETTLEMENT',
                                    protection_leg_reference_price = 0.0,
                                    protection_leg_leverage = 1.0,
                                    credit_protection_type = 'PAY_PROTECTION_AT_MATURITY',
                                    protection_leg_recovery_rate = 0.4,
                                    coupon_rate = 0.01,
                                    credit_premium_type = 'PAY_PREMIUM_UPTO_CURRENT_PERIOD',
                                    day_count_convention = 'ACTUAL_360',
                                    frequency = 'QUARTERLY',
                                    business_day_convention = 'MODIFIED_FOLLOWING',
                                    calendars = ['CAL_CFETS'],
                                    upfront_rate = 0.01,
                                    rebate_accrual = False)

    as_of_date = datetime(2020, 2, 21)

    # China treasury yield curve
    cn_treas_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency='CNY',
        term_dates = [
            datetime(2020, 3, 24),
            datetime(2020, 4, 24),
            datetime(2020, 5, 22),
            datetime(2020, 8, 22),
            datetime(2020, 11, 22),
            datetime(2021, 2, 21),
            datetime(2022, 2, 22),
            datetime(2023, 2, 24),
            datetime(2025, 2, 21),
            datetime(2027, 2, 22),
            datetime(2030, 2, 22),
            datetime(2035, 2, 23),
            datetime(2040, 2, 24),
            datetime(2050, 2, 22),
            datetime(2060, 2, 22),
            datetime(2070, 2, 22)
        ],
        zero_rates = [
            0.016587, 
            0.019987, 
            0.020290, 
            0.021068, 
            0.021139, 
            0.021222, 
            0.023163, 
            0.024260, 
            0.026628, 
            0.028458, 
            0.028658, 
            0.030162, 
            0.031016,
            0.033171, 
            0.033777, 
            0.034289
        ],
        curve_name='CN_TREAS'
    )

    bond_credit_curve = create_credit_curve(
            as_of_date=datetime(2020, 2, 21),
            term_dates=[
                datetime(2020, 2, 29),
                datetime(2020, 3, 7),
                datetime(2020, 3, 24),
                datetime(2020, 4, 24),
                datetime(2020, 5, 22),
                datetime(2020, 8, 22),
                datetime(2020, 11, 22),
                datetime(2021, 2, 21),
                datetime(2022, 2, 22),
                datetime(2023, 2, 24),
                datetime(2024, 2, 23),
                datetime(2025, 2, 21),
                datetime(2026, 2, 22),
                datetime(2027, 2, 22),
                datetime(2028, 2, 22),
                datetime(2029, 2, 23),
                datetime(2030, 2, 22),
                datetime(2035, 2, 23)
            ],
            hazard_rates = [
                0.001249,
                0.002330,
                0.005956,
                0.005516,
                0.005307,
                0.006861,
                0.008471,
                0.008545,
                0.010818,
                0.011579,
                0.011327,
                0.010564,
                0.008867,
                0.008566,
                0.008979,
                0.008981,
                0.011045,
                0.013547
            ]
        )
        
    
    mkt_data_set = create_cr_mkt_data_set(as_of_date,
                                        cn_treas_curve,
                                        bond_credit_curve)

    pricing_settings = create_cds_pricing_settings(
                                pricing_currency = 'CNY',
                                include_current_flow = False,
                                cash_flows = True,
                                numerical_fix = 'TAYLOR',
                                accrual_bias = 'HALFDAYBIAS',
                                fwds_in_cpn_period = 'PIECEWISE'
                                )

    risk_settings = create_cr_risk_settings(
        create_ir_curve_risk_settings(
            delta=True, gamma=False, curvature=False, 
            shift=1.0e-4, curvature_shift=5.0e-1, 
            method='CENTRAL_DIFFERENCE_METHOD', granularity='TERM_BUCKET_RISK', 
            scaling_factor=1.0e-4, threading_mode='SINGLE_THREADING_MODE'),
        create_credit_curve_risk_settings(
            delta=True, gamma=False, 
            shift=1.0e-4, 
            method='CENTRAL_DIFFERENCE_METHOD', granularity='TERM_BUCKET_RISK', 
            scaling_factor=1.0e-4, threading_mode='SINGLE_THREADING_MODE'),
        create_theta_risk_settings(
            theta=True, shift=1, scaling_factor=1./365.)
        )

    result = credit_default_swap_pricer(inst,
                                        as_of_date,
                                        mkt_data_set, 
                                        pricing_settings, 
                                        risk_settings)    
    
    
CDS Credit Curve Construction
------------

.. code-block:: python

    from datetime import datetime
    from caplib.analytics import create_ir_yield_curve
    from caplib.cranalytics import create_credit_par_curve, credit_curve_builder
    
    as_of_date = datetime(2020, 2, 21)

    # China treasury yield curve
    cn_treas_curve = create_ir_yield_curve(
        as_of_date = as_of_date,
        currency='CNY',
        term_dates = [
            datetime(2020, 3, 24),
            datetime(2020, 4, 24),
            datetime(2020, 5, 22),
            datetime(2020, 8, 22),
            datetime(2020, 11, 22),
            datetime(2021, 2, 21),
            datetime(2022, 2, 22),
            datetime(2023, 2, 24),
            datetime(2025, 2, 21),
            datetime(2027, 2, 22),
            datetime(2030, 2, 22),
            datetime(2035, 2, 23),
            datetime(2040, 2, 24),
            datetime(2050, 2, 22),
            datetime(2060, 2, 22),
            datetime(2070, 2, 22)
        ],
        zero_rates = [
            0.016587, 
            0.019987, 
            0.020290, 
            0.021068, 
            0.021139, 
            0.021222, 
            0.023163, 
            0.024260, 
            0.026628, 
            0.028458, 
            0.028658, 
            0.030162, 
            0.031016,
            0.033171, 
            0.033777, 
            0.034289
        ],
        curve_name='CN_TREAS'
    )

    credit_par_curve = create_credit_par_curve(
            as_of_date = as_of_date,
            currency = 'CNY',
            name = 'CFETS-SHCH-GTJA',
            pillars = [
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '3M', 0.002694),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '6M', 0.002960),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '1Y', 0.003184),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '2Y', 0.003422),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '3Y', 0.003673),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '4Y', 0.004223),  
                ('CFETS-SHCH-GTJA', 'CREDIT_DEFAULT_SWAP', '5Y', 0.004868)   
            ]
        )
        
    # credit curve
    credit_curve = credit_curve_builder(
            as_of_date = as_of_date,
            curve_name = 'CFETS-SHCH-GTJA',
            par_curve = credit_par_curve,
            discount_curve = cn_treas_curve,
            building_method = 'BOOTSTRAPPING_METHOD',
            calc_jacobian = False
    )
