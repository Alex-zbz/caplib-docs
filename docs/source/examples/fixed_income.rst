Fixed Income
============

Examples of fixed income analytics using caplib.

Bond Pricing
-----------

.. code-block:: python

    from datetime import datetime
    from caplib.analytics import *
    from caplib.fianalytics import *
    from caplib.fimarket import *
    
    bond = build_fixed_cpn_bond(1000000.0, 
        create_fixed_cpn_bond_template('cny_treas_cpn_bond_200014',
                                        datetime(2020, 10, 9), 
                                        1,
                                        datetime(2020, 10, 10),
                                        '5Y',
                                        2.15e-2, 
                                        'CNY', 
                                        'CAL_CFETS',
                                        frequency='ANNUAL',
                                        day_count='ACT_365_FIXED',
                                        issue_price=100.0,
                                        interest_day_convention='MODIFIED_FOLLOWING',
                                        stub_policy='INITIAL',
                                        broken_period_type='LONG',
                                        pay_day_offset=0,
                                        pay_day_convention='MODIFIED_FOLLOWING',
                                        ex_cpn_period='0d',
                                        ex_cpn_calendar='',
                                        ex_cpn_day_convention='INVALID_BUSINESS_DAY_CONVENTION',
                                        ex_cpn_eom=False)
    )
        
    as_of_date = datetime(2021, 7, 22)
    
    # Market data
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

    # Bond credit spread curve
    bond_credit_spread_curve = create_credit_curve(
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
    
    mkt_data = create_fi_mkt_data_set(as_of_date, 
                                    cn_treas_curve, 
                                    bond_credit_spread_curve,
                                    cn_treas_curve, 
                                    cn_treas_curve, 
                                    cn_treas_curve)

    # Risk settings
    risk_settings = create_fi_risk_settings(
        create_ir_curve_risk_settings(
            True, False, True, granularity='TERM_BUCKET_RISK'), 
        create_credit_curve_risk_settings(
            True, granularity='TERM_BUCKET_RISK'), 
        create_theta_risk_settings(True))
    
    # Pricing settings
    pricing_settings = create_model_free_pricing_settings(
        currency='CNY', 
        include_current_flow=False, 
        cash_flows=True)
    
    # Pricing
    result = vanilla_bond_pricer(bond, 
                                as_of_date, 
                                mkt_data, 
                                pricing_settings, 
                                risk_settings)
        
    
Bond Yield Curve Construction
----------------

.. code-block:: python

    from datetime import datetime
    from caplib.fianalytics import create_bond_par_curve,create_bond_curve_build_settings,build_bond_yield_curve

    as_of_date = datetime(2021, 7, 22)

    par_curve = create_bond_par_curve(
        as_of_date = as_of_date,
        currency = 'CNY',
        bond_names = ['CNY_TREAS_ZERO_1M',
                      'CNY_TREAS_CPN_A_3M',
                      'CNY_TREAS_CPN_A_6M',
                      'CNY_TREAS_CPN_A_9M',
                      'CNY_TREAS_CPN_A_1Y',
                      'CNY_TREAS_CPN_A_2Y',
                      'CNY_TREAS_CPN_A_3Y',
                      'CNY_TREAS_CPN_A_5Y',
                      'CNY_TREAS_CPN_SA_7Y',
                      'CNY_TREAS_CPN_SA_10Y',
                      'CNY_TREAS_CPN_SA_15Y',
                      'CNY_TREAS_CPN_SA_20Y',
                      'CNY_TREAS_CPN_SA_30Y'], 
        bond_quotes = [1.7112E-02,
                       1.8317E-02,
                       1.9413E-02,
                       1.9500E-02,
                       2.1563E-02,
                       2.4985E-02,
                       2.5538E-02,
                       2.7550E-02,
                       2.9175E-02,
                       2.9263E-02,
                       3.2984E-02,
                       3.3462E-02,
                       3.5023E-02],
        quote_type = 'YIELD_TO_MATURITY', 
        curve_name = 'CN_TREAS_STD')
        
    build_settings = create_bond_curve_build_settings('CN_TREAS_STD', 
                'ZERO_RATE', 
                'LINEAR_INTERP',
                'FLAT_EXTRAP')

    yield_curve = build_bond_yield_curve(build_settings, 
            curve_name = 'CN_TREAS_STD',
            as_of_date = as_of_date,
            par_curve = par_curve,
            day_count = 'ACT_365_FIXED',
            compounding_type = 'CONTINUOUS_COMPOUNDING',
            freq = 'ANNUAL',
            build_method = 'BOOTSTRAPPING_METHOD',
            calc_jacobian = False,
            fwd_curve = None)
