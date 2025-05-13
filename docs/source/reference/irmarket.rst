Interest Rate Market
=================

This module provides functionality for creating and managing interest rate market instruments, including indexes, deposit templates, swap templates, and other interest rate products.

.. contents:: Table of Contents
   :local:
   :depth: 2

Conversion Functions
----------------

Functions to convert string representations to their corresponding enumeration values for various interest rate market concepts.

.. code-block:: python

    to_brokend_rate_calculation_method(str_value)
    to_interest_rate_leg_type(str_value)
    to_interest_calculation_method(str_value)
    to_payment_discount_method(str_value)
    to_interest_rate_calculation_method(str_value)
    to_interest_schedule_type(str_value)
    to_interest_rate_index_type(str_value)
    to_ibor_index_type(str_value)

Convert string values to their corresponding enumeration types.

Parameters:
  - ``str_value`` (str): String representation of the enumeration value.

Returns:
  - Enumeration value corresponding to the input string.

Example:

.. code-block:: python

    from caplib.irmarket import (
        to_interest_rate_leg_type,
        to_payment_discount_method,
        to_interest_rate_calculation_method,
        to_ibor_index_type
    )
    
    # Convert string to enumeration value
    leg_type = to_interest_rate_leg_type("FIXED_LEG")
    payment_method = to_payment_discount_method("NO_DISCOUNT")
    calc_method = to_interest_rate_calculation_method("STANDARD")
    ibor_type = to_ibor_index_type("STANDARD_IBOR_INDEX")

Index Definitions
--------------

Functions for creating and managing interest rate indexes.

IBOR Index
~~~~~~~

.. code-block:: python

    create_ibor_index(index_name, index_tenor, index_ccy, calendar_list, start_delay, day_count, interest_day_convention, date_roll_convention=None, ibor_type=None)

Create an IBOR (Interbank Offered Rate) index.

Parameters:
  - ``index_name`` (str): Name of the IBOR index (e.g., "USD_LIBOR_3M").
  - ``index_tenor`` (str): Tenor of the index (e.g., "3M", "6M").
  - ``index_ccy`` (str): Currency of the index (e.g., "USD", "EUR").
  - ``calendar_list`` (list): List of calendar names to use for business day adjustments.
  - ``start_delay`` (int): Number of business days between fixing and the start of the interest period.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``date_roll_convention`` (str, optional): Date roll convention.
  - ``ibor_type`` (str, optional): Type of IBOR index (defaults to "STANDARD_IBOR_INDEX").

Returns:
  - IBOR index object that can be used in floating rate instruments.

Example:

.. code-block:: python

    from caplib.irmarket import create_ibor_index
    
    # Create a 3-month USD LIBOR index
    libor_3m = create_ibor_index(
        index_name="USD_LIBOR_3M",
        index_tenor="3M",
        index_ccy="USD",
        calendar_list=["US", "UK"],
        start_delay=2,
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING",
        ibor_type="STANDARD_IBOR_INDEX"
    )
    
    # Create a 6-month EURIBOR index
    euribor_6m = create_ibor_index(
        index_name="EUR_EURIBOR_6M",
        index_tenor="6M",
        index_ccy="EUR",
        calendar_list=["TARGET"],
        start_delay=2,
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING"
    )

Overnight Index
~~~~~~~~~~~

.. code-block:: python

    create_overnight_index(index_name, index_ccy, calendar_list, day_count, interest_day_convention, date_roll_convention=None)

Create an overnight interest rate index.

Parameters:
  - ``index_name`` (str): Name of the overnight index (e.g., "USD_SOFR", "EUR_ESTR").
  - ``index_ccy`` (str): Currency of the index (e.g., "USD", "EUR").
  - ``calendar_list`` (list): List of calendar names to use for business day adjustments.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``date_roll_convention`` (str, optional): Date roll convention.

Returns:
  - Overnight index object that can be used in overnight rate instruments.

Example:

.. code-block:: python

    from caplib.irmarket import create_overnight_index
    
    # Create a SOFR index
    sofr_index = create_overnight_index(
        index_name="USD_SOFR",
        index_ccy="USD",
        calendar_list=["US"],
        day_count="ACT_360",
        interest_day_convention="FOLLOWING"
    )
    
    # Create an ESTR index
    estr_index = create_overnight_index(
        index_name="EUR_ESTR",
        index_ccy="EUR",
        calendar_list=["TARGET"],
        day_count="ACT_360",
        interest_day_convention="FOLLOWING"
    )

Leg Definitions
------------

Functions for creating various types of interest rate leg definitions.

General Leg Definition
~~~~~~~~~~~~~~~~

.. code-block:: python

    create_leg_definition(leg_type, currency, day_count, ref_index, payment_discount_method, rate_calc_method, notional_exchange, spread, fx_convert, fx_reset, calendar, freq, interest_day_convention, stub_policy, broken_period_type, pay_day_offset, pay_day_convention, fixing_calendars, fixing_freq, fixing_day_convention, fixing_mode, fixing_day_offset)

Create a general leg definition for interest rate products.

Parameters:
  - ``leg_type`` (str): Type of leg (e.g., "FIXED_LEG", "FLOATING_LEG").
  - ``currency`` (str): Currency of the leg.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``ref_index`` (str): Reference index name for floating legs (empty for fixed legs).
  - ``payment_discount_method`` (str): Method for discounting payments.
  - ``rate_calc_method`` (str): Method for calculating interest rates.
  - ``notional_exchange`` (str): Type of notional exchange (e.g., "NO_EXCHANGE", "INITIAL_FINAL_EXCHANGE").
  - ``spread`` (bool): Whether a spread is applied over the reference rate.
  - ``fx_convert`` (bool): Whether FX conversion is applied.
  - ``fx_reset`` (bool): Whether FX reset is applied.
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``freq`` (str): Payment frequency (e.g., "QUARTERLY", "SEMI_ANNUAL").
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``stub_policy`` (str): Stub period policy (e.g., "INITIAL", "FINAL").
  - ``broken_period_type`` (str): Type of broken period (e.g., "LONG", "SHORT").
  - ``pay_day_offset`` (int): Offset days for payment dates.
  - ``pay_day_convention`` (str): Business day convention for payment dates.
  - ``fixing_calendars`` (list): List of calendars for rate fixing.
  - ``fixing_freq`` (str): Frequency of fixing.
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.
  - ``fixing_mode`` (str): Mode for fixing (e.g., "IN_ADVANCE", "IN_ARREARS").
  - ``fixing_day_offset`` (int): Offset days for fixing dates.

Returns:
  - Leg definition object.

Example:

.. code-block:: python

    from caplib.irmarket import create_leg_definition
    
    # Create a general leg definition
    leg_def = create_leg_definition(
        leg_type="FIXED_LEG",
        currency="USD",
        day_count="ACT_365_FIXED",
        ref_index="",  # Empty for fixed legs
        payment_discount_method="NO_DISCOUNT",
        rate_calc_method="STANDARD",
        notional_exchange="INITIAL_FINAL_EXCHANGE",
        spread=False,
        fx_convert=False,
        fx_reset=False,
        calendar="US",
        freq="SEMI_ANNUAL",
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        fixing_calendars=[],
        fixing_freq="INVALID_FREQUENCY",
        fixing_day_convention="INVALID_BUSINESS_DAY_CONVENTION",
        fixing_mode="INVALID_DATE_GENERATION_MODE",
        fixing_day_offset=0
    )

Fixed Leg Definition
~~~~~~~~~~~~~~~

.. code-block:: python

    create_fixed_leg_definition(currency, calendar, freq, day_count, interest_day_convention, stub_policy, broken_period_type, pay_day_offset, pay_day_convention, notional_exchange)

Create a fixed rate leg definition with simplified parameters.

Parameters:
  - ``currency`` (str): Currency of the leg (e.g., "USD", "EUR").
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``freq`` (str): Payment frequency (e.g., "QUARTERLY", "SEMI_ANNUAL").
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``stub_policy`` (str): Stub period policy (e.g., "INITIAL", "FINAL").
  - ``broken_period_type`` (str): Type of broken period (e.g., "LONG", "SHORT").
  - ``pay_day_offset`` (int): Offset days for payment dates.
  - ``pay_day_convention`` (str): Business day convention for payment dates.
  - ``notional_exchange`` (str): Type of notional exchange.

Returns:
  - Fixed leg definition object.

Example:

.. code-block:: python

    from caplib.irmarket import create_fixed_leg_definition
    
    # Create a fixed leg definition
    fixed_leg_def = create_fixed_leg_definition(
        currency="USD",
        calendar="US",
        freq="SEMI_ANNUAL",
        day_count="ACT_365_FIXED",
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        notional_exchange="INITIAL_FINAL_EXCHANGE"
    )

Floating Leg Definition
~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_floating_leg_definition(currency, ref_index, calendar, fixing_calendars, freq, fixing_freq, day_count, payment_discount_method, rate_calc_method, spread, interest_day_convention, stub_policy, broken_period_type, pay_day_offset, pay_day_convention, fixing_day_convention, fixing_mode, fixing_day_offset, notional_exchange)

Create a floating rate leg definition.

Parameters:
  - ``currency`` (str): Currency of the leg.
  - ``ref_index`` (str): Reference index name (e.g., "USD_LIBOR_3M").
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``fixing_calendars`` (list): List of calendars for rate fixing.
  - ``freq`` (str): Payment frequency.
  - ``fixing_freq`` (str): Frequency of fixing.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``payment_discount_method`` (str): Method for discounting payments.
  - ``rate_calc_method`` (str): Method for calculating interest rates.
  - ``spread`` (bool): Whether a spread is applied over the reference rate.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``stub_policy`` (str): Stub period policy.
  - ``broken_period_type`` (str): Type of broken period.
  - ``pay_day_offset`` (int): Offset days for payment dates.
  - ``pay_day_convention`` (str): Business day convention for payment dates.
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.
  - ``fixing_mode`` (str): Mode for fixing.
  - ``fixing_day_offset`` (int): Offset days for fixing dates.
  - ``notional_exchange`` (str): Type of notional exchange.

Returns:
  - Floating leg definition object.

Example:

.. code-block:: python

    from caplib.irmarket import create_floating_leg_definition
    
    # Create a floating leg definition
    floating_leg_def = create_floating_leg_definition(
        currency="USD",
        ref_index="USD_LIBOR_3M",  # Reference to the IBOR index
        calendar="US",
        fixing_calendars=["US", "UK"],
        freq="QUARTERLY",
        fixing_freq="QUARTERLY",
        day_count="ACT_360",
        payment_discount_method="NO_DISCOUNT",
        rate_calc_method="STANDARD",
        spread=True,  # Can have a spread over the floating rate
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        fixing_day_convention="MODIFIED_PRECEDING",
        fixing_mode="IN_ADVANCE",
        fixing_day_offset=-2,  # Typically 2 days before the start of period
        notional_exchange="INITIAL_FINAL_EXCHANGE"
    )

Instrument Templates
----------------

Functions for creating templates for various interest rate instruments.

Deposit Template
~~~~~~~~~~~

.. code-block:: python

    create_depo_template(inst_name, currency, calendar, start_delay, day_count, interest_day_convention, pay_day_offset, pay_day_convention, start_convention)

Create a template for deposit instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the deposit template.
  - ``currency`` (str): Currency of the deposit.
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``start_delay`` (int): Number of business days between trade date and effective date.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``pay_day_offset`` (int): Offset days for payment dates.
  - ``pay_day_convention`` (str): Business day convention for payment dates.
  - ``start_convention`` (str): Convention for the start date (e.g., "SPOTSTART").

Returns:
  - Deposit template object.

Example:

.. code-block:: python

    from caplib.irmarket import create_depo_template
    
    # Create a USD deposit template
    depo_template = create_depo_template(
        inst_name="USD_DEPO",
        currency="USD",
        calendar="US",
        start_delay=2,  # T+2 settlement
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        start_convention="SPOTSTART"
    )
    
    # Create a EUR deposit template
    eur_depo_template = create_depo_template(
        inst_name="EUR_DEPO",
        currency="EUR",
        calendar="TARGET",
        start_delay=2,
        day_count="ACT_360"
    )

Forward Rate Agreement (FRA) Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fra_template(inst_name, currency, ref_index, calendar, fixing_calendars, fixing_day_convention, fixing_mode, fixing_day_offset, day_count, interest_day_convention, pay_day_offset, pay_day_convention, payment_discount_method)

Create a template for Forward Rate Agreement (FRA) instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the FRA template.
  - ``currency`` (str): Currency of the FRA.
  - ``ref_index`` (str): Reference index name (e.g., "USD_LIBOR_3M").
  - ``calendar`` (str): Calendar for business day adjustments.
  - ``fixing_calendars`` (list): List of calendars for rate fixing.
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.
  - ``fixing_mode`` (str): Mode for fixing (e.g., "IN_ADVANCE").
  - ``fixing_day_offset`` (int): Offset days for fixing dates.
  - ``day_count`` (str): Day count convention for interest calculation.
  - ``interest_day_convention`` (str): Business day convention for interest dates.
  - ``pay_day_offset`` (int): Offset days for payment dates.
  - ``pay_day_convention`` (str): Business day convention for payment dates.
  - ``payment_discount_method`` (str): Method for discounting payments.

Returns:
  - FRA template object.

Example:

.. code-block:: python

    from caplib.irmarket import create_fra_template
    
    # Create a USD FRA template using LIBOR 3M
    fra_template = create_fra_template(
        inst_name="USD_FRA_3M",
        currency="USD",
        ref_index="USD_LIBOR_3M",
        calendar="US",
        fixing_calendars=["US", "UK"],
        fixing_day_convention="MODIFIED_PRECEDING",
        fixing_mode="IN_ADVANCE",
        fixing_day_offset=-2,
        day_count="ACT_360",
        interest_day_convention="MODIFIED_FOLLOWING",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        payment_discount_method="NO_DISCOUNT"
    )

Interest Rate Swap Template
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_swap_template(inst_name, fixed_leg_definition, floating_leg_definition)

Create a template for interest rate swap instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the swap template.
  - ``fixed_leg_definition`` (object): Fixed leg definition created by ``create_fixed_leg_definition``.
  - ``floating_leg_definition`` (object): Floating leg definition created by ``create_floating_leg_definition``.

Returns:
  - Interest rate swap template object.

Example:

.. code-block:: python

    from caplib.irmarket import create_swap_template, create_fixed_leg_definition, create_floating_leg_definition
    
    # Create the fixed leg definition
    fixed_leg = create_fixed_leg_definition(
        currency="USD",
        calendar="US",
        freq="SEMI_ANNUAL",
        day_count="ACT_365_FIXED",
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        notional_exchange="NO_EXCHANGE"
    )
    
    # Create the floating leg definition
    floating_leg = create_floating_leg_definition(
        currency="USD",
        ref_index="USD_LIBOR_3M",
        calendar="US",
        fixing_calendars=["US", "UK"],
        freq="QUARTERLY",
        fixing_freq="QUARTERLY",
        day_count="ACT_360",
        payment_discount_method="NO_DISCOUNT",
        rate_calc_method="STANDARD",
        spread=True,
        interest_day_convention="MODIFIED_FOLLOWING",
        stub_policy="INITIAL",
        broken_period_type="LONG",
        pay_day_offset=0,
        pay_day_convention="MODIFIED_FOLLOWING",
        fixing_day_convention="MODIFIED_PRECEDING",
        fixing_mode="IN_ADVANCE",
        fixing_day_offset=-2,
        notional_exchange="NO_EXCHANGE"
    )
    
    # Create a USD IRS template
    swap_template = create_swap_template(
        inst_name="USD_IRS",
        fixed_leg_definition=fixed_leg,
        floating_leg_definition=floating_leg
    )

Leg Fixings
--------

The ``create_leg_fixings`` function creates fixings for floating rate legs.

.. code-block:: python

    from caplib.irmarket import create_leg_fixings
    from datetime import datetime
    
    # Create fixings for a floating rate leg
    # Key is the fixing date as string, value is the rate
    fixings_dict = {
        "2025-01-20": 0.03500,
        "2025-02-20": 0.03550,
        "2025-03-20": 0.03600
    }
    
    leg_fixings = create_leg_fixings(fixings_dict)

Building Instruments
----------------

Deposit
~~~~~

The ``build_depo`` function creates a deposit instrument from a template.

.. code-block:: python

    from caplib.irmarket import build_depo
    from datetime import datetime
    
    # Valuation date
    val_date = datetime(2025, 3, 20)
    
    # Build a 3-month USD deposit
    depo = build_depo(
        pay_rec="RECEIVE",  # Receive fixed
        rate=0.0350,  # 3.50%
        start_date=val_date,
        maturity="3M",  # 3-month maturity
        inst_template=depo_template,  # Template from earlier example
        nominal=1000000.0  # $1 million notional
    )

Forward Rate Agreement (FRA)
~~~~~~~~~~~~~~~~~~~~~~~

The ``build_fra`` function creates a FRA instrument from a template.

.. code-block:: python

    from caplib.irmarket import build_fra
    
    # Build a 3x6 FRA (starts in 3 months, ends in 6 months)
    fra = build_fra(
        pay_rec="PAY",  # Pay fixed rate
        rate=0.0365,  # 3.65% fixed rate
        start_date=datetime(2025, 6, 20),  # Start in 3 months
        maturity="3M",  # 3-month period
        inst_template=fra_template,  # Template from earlier example
        leg_fixings=leg_fixings,  # Fixings from earlier example
        nominal=5000000.0  # $5 million notional
    )

Interest Rate Vanilla Instrument
~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``build_ir_vanilla_instrument`` function creates a vanilla interest rate instrument from a template.

.. code-block:: python

    from caplib.irmarket import build_ir_vanilla_instrument
    
    # Build a 5-year vanilla interest rate swap
    swap = build_ir_vanilla_instrument(
        pay_rec="PAY",  # Pay fixed, receive floating
        cpn_rate=0.0375,  # 3.75% fixed rate
        spread=0.0,  # No spread on floating leg
        start_date=val_date,  # Start today
        maturity="5Y",  # 5-year maturity
        inst_template=vanilla_swap_template,  # Template from earlier example
        nominal=10000000.0,  # $10 million notional
        leg_fixings=leg_fixings  # Fixings from earlier example
    )

Utilities
-------

Print Cash Flow Schedule
~~~~~~~~~~~~~~~~~~

The ``print_cash_flow_sched`` function formats a cash flow schedule as a pandas DataFrame.

.. code-block:: python

    from caplib.irmarket import print_cash_flow_sched
    
    # Print cash flow schedule of an instrument
    # Assuming we have a cash flow schedule from an instrument
    cash_flow_df = print_cash_flow_sched(swap.cash_flow_schedule)
    
    print(cash_flow_df)
    # Output will be a pandas DataFrame with columns for dates, rates, etc.

Complete Workflow Example
--------------------

Here's a complete workflow that demonstrates creating and building interest rate instruments:

.. code-block:: python

    from datetime import datetime
    from caplib.irmarket import (
        create_ibor_index,
        create_fixed_leg_definition,
        create_floating_leg_definition,
        create_ir_vanilla_swap_template,
        create_leg_fixings,
        build_ir_vanilla_instrument,
        print_cash_flow_sched
    )
    
    # Step 1: Set up valuation date
    val_date = datetime(2025, 3, 20)
    
    # Step 2: Create a LIBOR index
    libor_3m = create_ibor_index(
        index_name="USD_LIBOR_3M",
        index_tenor="3M",
        index_ccy="USD",
        calendar_list=["US", "UK"],
        start_delay=2,
        day_count="ACT_360"
    )
    
    # Step 3: Create leg definitions
    fixed_leg_def = create_fixed_leg_definition(
        currency="USD",
        calendar="US",
        freq="SEMI_ANNUAL",
        day_count="30/360",
        interest_day_convention="MODIFIED_FOLLOWING"
    )
    
    floating_leg_def = create_floating_leg_definition(
        currency="USD",
        ref_index="USD_LIBOR_3M",
        calendar="US",
        fixing_calendars=["US", "UK"],
        freq="QUARTERLY",
        fixing_freq="QUARTERLY",
        day_count="ACT_360"
    )
    
    # Step 4: Create a swap template
    swap_template = create_ir_vanilla_swap_template(
        inst_name="USD_SWAP",
        start_delay=2,
        leg1_definition=fixed_leg_def,
        leg2_definition=floating_leg_def,
        start_convention="SPOTSTART"
    )
    
    # Step 5: Create fixings
    fixings_dict = {
        "2025-01-20": 0.03500,
        "2025-02-20": 0.03550,
        "2025-03-20": 0.03600
    }
    
    leg_fixings = create_leg_fixings(fixings_dict)
    
    # Step 6: Build a 10-year swap
    swap = build_ir_vanilla_instrument(
        pay_rec="PAY",  # Pay fixed, receive floating
        cpn_rate=0.03875,  # 3.875% fixed rate
        spread=0.0,  # No spread on floating leg
        start_date=val_date,
        maturity="10Y",  # 10-year swap
        inst_template=swap_template,
        nominal=10000000.0,  # $10 million
        leg_fixings=leg_fixings
    )
    
    # Step 7: Print the swap's cash flow schedule
    cash_flow_df = print_cash_flow_sched(swap.cash_flow_schedule)
    
    print(f"10Y Swap Cash Flow Schedule:")
    print(cash_flow_df)
