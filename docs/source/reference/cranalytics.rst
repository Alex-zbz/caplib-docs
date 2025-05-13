Credit Analytics
===============

The cranalytics module provides functions for building credit curves, creating market data sets, and pricing credit derivatives.

.. contents:: Table of Contents
   :local:
   :depth: 2

Risk Settings
-----------

These functions create risk settings for credit derivatives.

Create CR Risk Settings
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cr_risk_settings(ir_curve_settings, cs_curve_settings, theta_settings)

Create credit risk settings.

Parameters:
  - ``ir_curve_settings`` (object): Interest rate curve settings.
  - ``cs_curve_settings`` (object): Credit spread curve settings.
  - ``theta_settings`` (object): Theta (time decay) settings.

Returns:
  - Risk settings object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    
    risk_settings = cranalytics.create_cr_risk_settings(
        ir_curve_settings=ir_settings,  
        cs_curve_settings=cs_settings,  
        theta_settings=theta_settings   
    )

Credit Curve Functions
--------------------

These functions help create and manage credit curves from market data.

Create Credit Par Curve
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_credit_par_curve(as_of_date, currency, name, pillars, tag, mode, save, location)

Create a credit par curve from market quotes.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the curve.
  - ``currency`` (str): Currency of the credit instruments.
  - ``name`` (str): Identifier for the curve.
  - ``pillars`` (list): List of tuples containing credit instrument data points.
  - ``tag`` (str): Optional tag for the curve.
  - ``mode`` (str): Mode for curve creation.
  - ``save`` (bool): Whether to save the curve.
  - ``location`` (str): Location to save the curve.

Returns:
  - Credit par curve object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    
    # Define pillar points for the curve
    pillars = [
        ["CDS_6M", "credit_default_swap", "6M", 0.0050, "spot_start"],
        ["CDS_1Y", "credit_default_swap", "1Y", 0.0075, "spot_start"],
        ["CDS_2Y", "credit_default_swap", "2Y", 0.0100, "spot_start"],
        ["CDS_3Y", "credit_default_swap", "3Y", 0.0120, "spot_start"],
        ["CDS_5Y", "credit_default_swap", "5Y", 0.0150, "spot_start"],
        ["CDS_7Y", "credit_default_swap", "7Y", 0.0170, "spot_start"],
        ["CDS_10Y", "credit_default_swap", "10Y", 0.0200, "spot_start"]
    ]
    
    credit_par_curve = cranalytics.create_credit_par_curve(
        as_of_date="2025-03-20",
        currency="USD",
        name="COMPANY_XYZ_PAR_CURVE",
        pillars=pillars,
        tag="",
        mode="",
        save=False,
        location=""
    )

Credit Curve Builder
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    credit_curve_builder(as_of_date, curve_name, build_settings, par_curve, discount_curve, building_method, calc_jacobian)

Build a credit curve from a par curve.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the curve.
  - ``curve_name`` (str): Name identifier for the curve.
  - ``build_settings`` (object): Settings for curve building.
  - ``par_curve`` (object): Credit par curve from market quotes.
  - ``discount_curve`` (object): Discount curve for present value calculations.
  - ``building_method`` (str): Method for constructing the curve (e.g., "BOOTSTRAP").
  - ``calc_jacobian`` (bool): Whether to calculate the Jacobian matrix for sensitivity analysis.

Returns:
  - Credit curve object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    
    credit_curve = cranalytics.credit_curve_builder(
        as_of_date="2025-03-20",
        curve_name="COMPANY_XYZ_CREDIT_CURVE",
        build_settings=build_settings,
        par_curve=credit_par_curve,
        discount_curve=usd_discount_curve,
        building_method="BOOTSTRAP",
        calc_jacobian=True
    )

Pricing Settings
--------------

These functions create pricing settings for credit derivatives.

Create CDS Pricing Settings
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cds_pricing_settings(pricing_currency, include_current_flow, cash_flows, include_settlement_flow, numerical_fix, accrual_bias, fwds_in_cpn_period, name, tag)

Create pricing settings for credit default swaps.

Parameters:
  - ``pricing_currency`` (str): Currency for pricing and results.
  - ``include_current_flow`` (bool): Whether to include the current coupon flow.
  - ``cash_flows`` (bool): Whether to compute detailed cash flows.
  - ``include_settlement_flow`` (bool): Whether to include settlement flows.
  - ``numerical_fix`` (str): Numerical fix to apply during calculation.
  - ``accrual_bias`` (str): Method for calculating day fractions.
  - ``fwds_in_cpn_period`` (str): How forward rates are treated within coupon periods.
  - ``name`` (str): Name for the settings.
  - ``tag`` (str): Optional tag.

Returns:
  - CDS pricing settings object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    
    pricing_settings = cranalytics.create_cds_pricing_settings(
        pricing_currency="USD",
        include_current_flow=True,
        cash_flows=True,
        include_settlement_flow=True,
        numerical_fix="NONE_FIX",
        accrual_bias="HALFDAYBIAS",
        fwds_in_cpn_period="FLAT",
        name="STANDARD_CDS_PRICING",
        tag=""
    )

Market Data
----------

These functions create market data sets for credit derivatives pricing.

Create CR Market Data Set
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cr_mkt_data_set(as_of_date, discount_curve, credit_curve, name, tag)

Create a credit market data set for pricing.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the market data.
  - ``discount_curve`` (object): Interest rate discount curve.
  - ``credit_curve`` (object): Credit spread curve.
  - ``name`` (str): Name identifier for the market data set.
  - ``tag`` (str): Optional tag.

Returns:
  - Credit market data set object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    
    market_data = cranalytics.create_cr_mkt_data_set(
        as_of_date="2025-03-20",
        discount_curve=usd_discount_curve,
        credit_curve=company_xyz_credit_curve,
        name="COMPANY_XYZ_MKT_DATA",
        tag=""
    )

Pricing Functions
--------------

These functions price various credit derivative instruments.

Credit Default Swap Pricer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    credit_default_swap_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, result_tag, rtn_type, mode)

Price a credit default swap instrument.

Parameters:
  - ``instrument`` (object): The CDS instrument to price.
  - ``pricing_date`` (datetime): The date for pricing.
  - ``mkt_data_set`` (object): Market data set containing curves.
  - ``pricing_settings`` (object): Pricing settings for the CDS.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``result_tag`` (str): Tag for the pricing result.
  - ``rtn_type`` (str): Return type for the calculation.
  - ``mode`` (str): Mode for the calculation.

Returns:
  - CDS pricing result object

Example:

.. code-block:: python

    import caplib.cranalytics as cranalytics
    import caplib.crmarket as crmarket
    
    # Build a CDS instrument
    cds = crmarket.build_credit_default_swap(
        nominal=10000000,
        currency="USD",
        issue_date="2025-03-20",
        maturity="2030-03-20",
        protection_leg_pay_receive="PAY",
        protection_leg_settlement_type="CASH",
        protection_leg_reference_price=100.0,
        protection_leg_leverage=1.0,
        credit_protection_type="PAY_PROTECTION_AT_DEFAULT",
        protection_leg_recovery_rate=0.4,
        coupon_rate=0.01,  # 100 bps spread
        credit_premium_type="PAY_PREMIUM_AT_DEFAULT",
        day_count_convention="ACT_360",
        frequency="3M",
        business_day_convention="FOLLOWING",
        calendars=["USA", "UK"],
        upfront_rate=0.0,
        rebate_accrual=True,
        name="COMPANY_XYZ_CDS",
        tag="",
        mode="",
        save=False,
        location=""
    )
    
    # Price the CDS
    cds_result = cranalytics.credit_default_swap_pricer(
        instrument=cds,
        pricing_date="2025-03-20",
        mkt_data_set=market_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        result_tag="PRICING_RESULT",
        rtn_type="",
        mode=""
    )
