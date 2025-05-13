Credit Market
============

This module provides functionality for creating and managing credit market instruments, including credit default swaps (CDS) and other credit derivatives.

.. contents:: Table of Contents
   :local:
   :depth: 2

CDS Template
---------

Functions for creating templates for credit default swap (CDS) instruments.

.. code-block:: python

    create_cds_template(inst_name, currency, index, currency_calendar, index_calendars, index_tenor, day_count, payment_frequency, protection_payment_timing, business_day_convention, cash_settlement_day_offset, cash_settlement_day_convention, trade_day_offset, use_cashflow_cashsettlement)

Create a template for credit default swap (CDS) instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``currency`` (str): Currency of the CDS.
  - ``index`` (str): Reference index for the CDS.
  - ``currency_calendar`` (str): Calendar for the CDS currency.
  - ``index_calendars`` (list): List of calendars for the index.
  - ``index_tenor`` (str): Tenor of the index (e.g., "3M").
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``payment_frequency`` (str): Frequency of premium payments (e.g., "QUARTERLY").
  - ``protection_payment_timing`` (str): Timing for protection payments.
  - ``business_day_convention`` (str): Business day convention for date adjustments.
  - ``cash_settlement_day_offset`` (int): Day offset for cash settlement.
  - ``cash_settlement_day_convention`` (str): Business day convention for cash settlement.
  - ``trade_day_offset`` (int): Day offset for trade date.
  - ``use_cashflow_cashsettlement`` (bool): Whether to use cashflow for cash settlement.

Returns:
  - CDS template object.

Example:

.. code-block:: python

    from caplib.crmarket import create_cds_template
    
    # Create a USD CDS template
    cds_template = create_cds_template(
        inst_name="USD_CDS",
        currency="USD",
        index="USD_LIBOR_3M",
        currency_calendar="US",
        index_calendars=["US", "UK"],
        index_tenor="3M",
        day_count="ACT_360",
        payment_frequency="QUARTERLY",
        protection_payment_timing="END",
        business_day_convention="FOLLOWING",
        cash_settlement_day_offset=3,
        cash_settlement_day_convention="FOLLOWING",
        trade_day_offset=1,
        use_cashflow_cashsettlement=True
    )

Credit Protection Types
~~~~~~~~~~~~~~~~~~~~~

Credit protection types define when protection payments are made in credit default swaps:

.. code-block:: python

    from caplib.crmarket import to_credit_protection_type
    
    # Convert string to CreditProtectionType
    protection_type = to_credit_protection_type("PAY_PROTECTION_AT_DEFAULT")
    
    # Default value if None is provided
    default_protection = to_credit_protection_type(None)  # Returns PAY_PROTECTION_AT_DEFAULT

Credit Premium Types
~~~~~~~~~~~~~~~~~

Credit premium types define how premium payments are handled in credit default swaps:

.. code-block:: python

    from caplib.crmarket import to_credit_premium_type
    
    # Convert string to CreditPremiumType
    premium_type = to_credit_premium_type("PAY_PREMIUM_AT_DEFAULT")
    
    # Default value if None is provided
    default_premium = to_credit_premium_type(None)  # Returns PAY_PREMIUM_AT_DEFAULT

Building Credit Default Swaps
---------------------------

You can build a Credit Default Swap instrument using the template:

.. code-block:: python

    from caplib.crmarket import build_credit_default_swap
    
    # Build a Credit Default Swap instrument
    cds = build_credit_default_swap(
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

**Parameters:**

- ``nominal``: Notional amount of the CDS contract
- ``currency``: Currency of the CDS
- ``issue_date``: Effective date of the CDS
- ``maturity``: Maturity date of the CDS
- ``protection_leg_pay_receive``: Whether the user pays or receives protection
- ``protection_leg_settlement_type``: Cash or physical settlement
- ``protection_leg_reference_price``: Reference price for the underlying
- ``protection_leg_leverage``: Leverage factor applied to the protection amount
- ``credit_protection_type``: Type of protection payment
- ``protection_leg_recovery_rate``: Expected recovery rate in case of default
- ``coupon_rate``: Annual premium rate (CDS spread)
- ``credit_premium_type``: Type of premium payment
- ``day_count_convention``: Day count convention for calculating premium amounts
- ``frequency``: Frequency of premium payments
- ``business_day_convention``: Business day adjustment convention
- ``calendars``: List of holiday calendars to consider
- ``upfront_rate``: Upfront payment rate as a percentage of nominal
- ``rebate_accrual``: Whether to rebate accrued premium in case of default
- ``name``: Name identifier for the CDS
- ``tag``: Optional tag for the CDS
- ``mode``: Mode for building the CDS
- ``save``: Whether to save the instrument
- ``location``: Location to save the instrument

Integration with Credit Analytics
------------------------------

The Credit Market module integrates with the Credit Analytics module to enable pricing and risk analysis:

.. code-block:: python

    from caplib.crmarket import create_cds_template, build_credit_default_swap
    from caplib.cranalytics import create_cr_mkt_data_set, credit_default_swap_pricer
    
    # Create a CDS template
    cds_template = create_cds_template(...)
    
    # Build a CDS instrument
    cds = build_credit_default_swap(...)
    
    # Create market data for pricing
    market_data = create_cr_mkt_data_set(
        as_of_date="2025-03-20",
        discount_curve=discount_curve,
        credit_curve=credit_curve,
        name="CR_MKT_DATA",
        tag=""
    )
    
    # Price the CDS
    pricing_result = credit_default_swap_pricer(
        instrument=cds,
        pricing_date="2025-03-20",
        mkt_data_set=market_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        result_tag="",
        rtn_type="",
        mode=""
    )
