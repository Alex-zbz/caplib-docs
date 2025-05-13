FX Market
===========

This module provides functionality for creating and managing FX market instruments, including FX forwards, swaps, non-deliverable forwards (NDFs), and options.

.. contents:: Table of Contents
   :local:
   :depth: 2

FX Forward Templates
-----------------

Functions for creating templates for FX forward instruments.

.. code-block:: python

    create_fx_forward_template(inst_name, fixing_offset, currency_pair, delivery_day_convention, fixing_day_convention, calendars)

Create a template for FX forward instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``fixing_offset`` (str): Offset for fixing relative to delivery (e.g., "2D").
  - ``currency_pair`` (str): Currency pair in format "CCY1/CCY2" (e.g., "EUR/USD").
  - ``delivery_day_convention`` (str): Business day convention for delivery dates.
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.
  - ``calendars`` (list): List of calendar names to use for business day adjustments.

Returns:
  - FX forward template object.

Example:

.. code-block:: python

    from caplib.fxmarket import create_fx_forward_template
    
    # Create an FX forward template
    fx_forward_template = create_fx_forward_template(
        inst_name="EUR_USD_1M_FWD",
        fixing_offset="2D",
        currency_pair="EUR/USD",
        delivery_day_convention="MODIFIED_FOLLOWING",
        fixing_day_convention="MODIFIED_FOLLOWING",
        calendars=["TARGET", "US"]
    )

FX Forward Instruments
------------------

Functions for creating FX forward instruments.

.. code-block:: python

    create_fx_forward(buy_currency, buy_amount, sell_currency, sell_amount, delivery, fx_fwd_template, expiry)

Create an FX forward instrument.

Parameters:
  - ``buy_currency`` (str): Currency to buy (e.g., "EUR").
  - ``buy_amount`` (float): Amount of buy currency.
  - ``sell_currency`` (str): Currency to sell (e.g., "USD").
  - ``sell_amount`` (float): Amount of sell currency.
  - ``delivery`` (datetime): Delivery date of the forward.
  - ``fx_fwd_template`` (object): FX forward template created by ``create_fx_forward_template``.
  - ``expiry`` (datetime): Expiry date of the forward.

Returns:
  - FX forward instrument object.

Example:

.. code-block:: python

    from datetime import datetime
    from caplib.fxmarket import create_fx_forward
    from caplib.datetime import create_date
    
    # Create calculation dates
    as_of_date = datetime(2025, 3, 20)
    delivery_date = create_date(as_of_date, "1M", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    expiry_date = create_date(as_of_date, "1M-2D", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    
    # Create an FX forward instrument
    fx_forward = create_fx_forward(
        buy_currency="EUR",
        buy_amount=1000000.0,
        sell_currency="USD",
        sell_amount=1080000.0,
        delivery=delivery_date,
        fx_fwd_template=fx_forward_template,  # From previous example
        expiry=expiry_date
    )

FX Swap Templates
-------------

Functions for creating templates for FX swap instruments.

.. code-block:: python

    create_fx_swap_template(inst_name, start_convention, currency_pair, calendars, start_day_convention, end_day_convention, fixing_offset, fixing_day_convention)

Create a template for FX swap instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``start_convention`` (str): Convention for the start date (e.g., "SPOT").
  - ``currency_pair`` (str): Currency pair in format "CCY1/CCY2" (e.g., "EUR/USD").
  - ``calendars`` (list): List of calendar names to use for business day adjustments.
  - ``start_day_convention`` (str): Business day convention for start dates.
  - ``end_day_convention`` (str): Business day convention for end dates.
  - ``fixing_offset`` (str): Offset for fixing relative to delivery (e.g., "2D").
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.

Returns:
  - FX swap template object.

Example:

.. code-block:: python

    from caplib.fxmarket import create_fx_swap_template
    
    # Create an FX swap template
    fx_swap_template = create_fx_swap_template(
        inst_name="EUR_USD_SWAP",
        start_convention="SPOT",
        currency_pair="EUR/USD",
        calendars=["TARGET", "US"],
        start_day_convention="MODIFIED_FOLLOWING",
        end_day_convention="MODIFIED_FOLLOWING",
        fixing_offset="2D",
        fixing_day_convention="MODIFIED_FOLLOWING"
    )

FX Swap Instruments
--------------

Functions for creating FX swap instruments.

.. code-block:: python

    create_fx_swap(near_buy_currency, near_buy_amount, near_sell_currency, near_sell_amount, near_delivery_date, near_expiry_date, far_buy_currency, far_buy_amount, far_sell_currency, far_sell_amount, far_delivery_date, far_expiry_date, fx_swap_template)

Create an FX swap instrument.

Parameters:
  - ``near_buy_currency`` (str): Currency to buy in the near leg.
  - ``near_buy_amount`` (float): Amount of currency to buy in the near leg.
  - ``near_sell_currency`` (str): Currency to sell in the near leg.
  - ``near_sell_amount`` (float): Amount of currency to sell in the near leg.
  - ``near_delivery_date`` (datetime): Delivery date of the near leg.
  - ``near_expiry_date`` (datetime): Expiry date of the near leg.
  - ``far_buy_currency`` (str): Currency to buy in the far leg.
  - ``far_buy_amount`` (float): Amount of currency to buy in the far leg.
  - ``far_sell_currency`` (str): Currency to sell in the far leg.
  - ``far_sell_amount`` (float): Amount of currency to sell in the far leg.
  - ``far_delivery_date`` (datetime): Delivery date of the far leg.
  - ``far_expiry_date`` (datetime): Expiry date of the far leg.
  - ``fx_swap_template`` (object): FX swap template created by ``create_fx_swap_template``.

Returns:
  - FX swap instrument object.

Example:

.. code-block:: python

    from caplib.fxmarket import create_fx_swap
    from datetime import datetime
    from caplib.datetime import create_date
    
    # Create an as_of_date for reference
    as_of_date = datetime(2025, 3, 20)
    
    # Create an FX swap instrument
    fx_swap = create_fx_swap(
        near_buy_currency="EUR",
        near_buy_amount=1000000.0,
        near_sell_currency="USD",
        near_sell_amount=1080000.0,
        near_delivery_date=create_date(as_of_date, "1M", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        near_expiry_date=create_date(as_of_date, "1M-2D", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        far_buy_currency="USD",
        far_buy_amount=1082000.0,
        far_sell_currency="EUR",
        far_sell_amount=1000000.0,
        far_delivery_date=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        far_expiry_date=create_date(as_of_date, "3M-2D", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        fx_swap_template=fx_swap_template  # From previous example
    )

FX NDF Templates
-----------

Functions for creating templates for FX non-deliverable forward (NDF) instruments.

.. code-block:: python

    create_fx_ndf_template(inst_name, fixing_offset, currency_pair, delivery_day_convention, fixing_day_convention, calendars, settlement_currency)

Create a template for FX non-deliverable forward (NDF) instruments.

Parameters:
  - ``inst_name`` (str): Name identifier for the template.
  - ``fixing_offset`` (str): Offset for fixing relative to delivery (e.g., "2D").
  - ``currency_pair`` (str): Currency pair in format "CCY1/CCY2" (e.g., "USD/CNY").
  - ``delivery_day_convention`` (str): Business day convention for delivery dates.
  - ``fixing_day_convention`` (str): Business day convention for fixing dates.
  - ``calendars`` (list): List of calendar names to use for business day adjustments.
  - ``settlement_currency`` (str): Currency used for settlement (typically a freely convertible currency).

Returns:
  - FX NDF template object.

Example:

.. code-block:: python

    from caplib.fxmarket import create_fx_ndf_template
    
    # Create an FX NDF template
    fx_ndf_template = create_fx_ndf_template(
        inst_name="USD_CNY_NDF",
        fixing_offset="2D",
        currency_pair="USD/CNY",
        delivery_day_convention="MODIFIED_FOLLOWING",
        fixing_day_convention="MODIFIED_FOLLOWING",
        calendars=["US", "CHINA"],
        settlement_currency="USD"
    )

FX NDF Instruments
-------------

Functions for creating FX non-deliverable forward (NDF) instruments.

.. code-block:: python

    create_fx_non_deliverable_forwad(buy_currency, buy_amount, sell_currency, sell_amount, delivery_date, expiry_date, settlement_currency, fx_ndf_template)

Create an FX non-deliverable forward (NDF) instrument.

Parameters:
  - ``buy_currency`` (str): Currency to buy (e.g., "USD").
  - ``buy_amount`` (float): Amount of buy currency.
  - ``sell_currency`` (str): Currency to sell (e.g., "CNY").
  - ``sell_amount`` (float): Amount of sell currency.
  - ``delivery_date`` (datetime): Delivery date of the NDF.
  - ``expiry_date`` (datetime): Expiry date of the NDF.
  - ``settlement_currency`` (str): Currency used for settlement.
  - ``fx_ndf_template`` (object): FX NDF template created by ``create_fx_ndf_template``.

Returns:
  - FX NDF instrument object.

Example:

.. code-block:: python

    from caplib.fxmarket import create_fx_non_deliverable_forwad
    from datetime import datetime
    from caplib.datetime import create_date
    
    # Create an as_of_date for reference
    as_of_date = datetime(2025, 3, 20)
    
    # Create an FX NDF instrument
    fx_ndf = create_fx_non_deliverable_forwad(
        buy_currency="USD",
        buy_amount=1000000.0,
        sell_currency="CNY",
        sell_amount=6450000.0,
        delivery_date=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US", "CHINA"]),
        expiry_date=create_date(as_of_date, "3M-2D", "MODIFIED_FOLLOWING", ["US", "CHINA"]),
        settlement_currency="USD",
        fx_ndf_template=fx_ndf_template  # From previous example
    )

Date Calculation
-------------

Functions for calculating important FX dates.

FX Spot Date Calculator
~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_spot_date_calculator(calculation_date, currency_pair)

Calculate the spot date for an FX transaction based on the calculation date and currency pair.

Parameters:
  - ``calculation_date`` (datetime): Date from which to calculate the spot date.
  - ``currency_pair`` (str): Currency pair in format "CCY1/CCY2" (e.g., "EUR/USD").

Returns:
  - datetime: Spot date for the FX transaction.

Example:

.. code-block:: python

    from datetime import datetime
    from caplib.fxmarket import fx_spot_date_calculator
    
    # Calculate FX spot date for EUR/USD
    as_of_date = datetime(2025, 3, 20)
    spot_date = fx_spot_date_calculator(
        calculation_date=as_of_date,
        currency_pair="EUR/USD"
    )
    print(f"EUR/USD spot date: {spot_date}")  # Typically T+2 business days

FX Option Date Calculator
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_option_date_calculator(calculation_date, currency_pair, term, business_day_convention)

Calculate the option date for an FX option based on the calculation date, currency pair, and term.

Parameters:
  - ``calculation_date`` (datetime): Date from which to calculate the option date.
  - ``currency_pair`` (str): Currency pair in format "CCY1/CCY2" (e.g., "EUR/USD").
  - ``term`` (str): Term of the option (e.g., "1M", "3M", "1Y").
  - ``business_day_convention`` (str): Business day convention to apply.

Returns:
  - datetime: Option date for the FX option.

Example:

.. code-block:: python

    from caplib.fxmarket import fx_option_date_calculator
    
    # Calculate FX option date for a 3-month EUR/USD option
    option_date = fx_option_date_calculator(
        calculation_date=as_of_date,
        currency_pair="EUR/USD",
        term="3M",
        business_day_convention="MODIFIED_FOLLOWING"
    )
    print(f"3M EUR/USD option date: {option_date}")

Complete Workflow Example
--------------------

Here's a complete workflow that demonstrates creating and using FX market instruments:

.. code-block:: python

    from datetime import datetime
    from caplib.datetime import create_date
    from caplib.fxmarket import (
        create_fx_forward_template,
        create_fx_forward,
        create_fx_swap_template,
        create_fx_swap,
        fx_spot_date_calculator
    )
    
    # Step 1: Set up date
    as_of_date = datetime(2025, 3, 20)
    
    # Step 2: Create FX forward template
    fx_forward_template = create_fx_forward_template(
        inst_name="EUR_USD_FWD",
        fixing_offset="2D",
        currency_pair="EUR/USD",
        delivery_day_convention="MODIFIED_FOLLOWING",
        fixing_day_convention="MODIFIED_FOLLOWING",
        calendars=["TARGET", "US"]
    )
    
    # Step 3: Calculate spot date
    spot_date = fx_spot_date_calculator(as_of_date, "EUR/USD")
    
    # Step 4: Calculate delivery and expiry dates
    delivery_date = create_date(spot_date, "1M", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    expiry_date = create_date(delivery_date, "-2D", "PRECEDING", ["TARGET", "US"])
    
    # Step 5: Create FX forward
    fx_forward = create_fx_forward(
        buy_currency="EUR",
        buy_amount=1000000.0,
        sell_currency="USD",
        sell_amount=1080000.0,
        delivery=delivery_date,
        fx_fwd_template=fx_forward_template,
        expiry=expiry_date
    )
    
    # Step 6: Create FX swap template
    fx_swap_template = create_fx_swap_template(
        inst_name="EUR_USD_SWAP",
        start_convention="SPOT",
        currency_pair="EUR/USD",
        calendars=["TARGET", "US"],
        start_day_convention="MODIFIED_FOLLOWING",
        end_day_convention="MODIFIED_FOLLOWING",
        fixing_offset="2D",
        fixing_day_convention="MODIFIED_FOLLOWING"
    )
    
    # Step 7: Create far leg dates
    far_delivery_date = create_date(spot_date, "3M", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    far_expiry_date = create_date(far_delivery_date, "-2D", "PRECEDING", ["TARGET", "US"])
    
    # Step 8: Create FX swap
    fx_swap = create_fx_swap(
        near_buy_currency="EUR",
        near_buy_amount=1000000.0,
        near_sell_currency="USD",
        near_sell_amount=1080000.0,
        near_delivery_date=delivery_date,
        near_expiry_date=expiry_date,
        far_buy_currency="USD",
        far_buy_amount=1082000.0,
        far_sell_currency="EUR",
        far_sell_amount=1000000.0,
        far_delivery_date=far_delivery_date,
        far_expiry_date=far_expiry_date,
        fx_swap_template=fx_swap_template
    )
    
    # Step 9: Output results
    print(f"Spot Date: {spot_date}")
    print(f"Forward Delivery Date: {delivery_date}")
    print(f"Forward Expiry Date: {expiry_date}")
    print(f"Far Delivery Date: {far_delivery_date}")
    print(f"Far Expiry Date: {far_expiry_date}")
