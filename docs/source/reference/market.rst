Market
======

This section covers the market functionality available in the caplib.market module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Market Data Types and Conversions
------------------------------

The module provides numerous functions for converting string representations to market data types and enumerations.

**Function Signatures**

.. code-block:: python

    to_time_series_mode(mode_str)
    to_exercise_type(exercise_str)
    to_payoff_type(payoff_str)
    to_payment_type(payment_str)
    to_instrument_type(instrument_str)
    to_barrier_type(barrier_str)
    to_performance_type(performance_str)
    to_buy_sell_flag(buy_sell_str)
    to_settlement_type(settlement_str)
    to_ccy_pair(ccy_pair_str)
    to_notional_exchange(notional_exchange_str)
    to_instrument_start_convention(start_convention_str)
    to_pay_receive_flag(pay_receive_str)
    to_notional_type(notional_type_str)
    to_strike_type(strike_type_str)
    to_averaging_method(averaging_method_str)
    to_event_observation_type(observation_type_str)
    to_risk_reversal(risk_reversal_str)

**Parameters**

* **mode_str/exercise_str/etc.** (*str*) - String representation of the type to convert

**Returns**

* Enumeration value corresponding to the input string

**Example**

.. code-block:: python

    from caplib.market import (
        to_time_series_mode,
        to_exercise_type,
        to_payoff_type,
        to_payment_type,
        to_instrument_type,
        to_barrier_type,
        to_performance_type,
        to_buy_sell_flag,
        to_settlement_type,
        to_ccy_pair,
        to_notional_exchange,
        to_instrument_start_convention,
        to_pay_receive_flag,
        to_notional_type,
        to_strike_type,
        to_averaging_method,
        to_event_observation_type,
        to_risk_reversal
    )
    
    # Convert string to TimeSeries Mode
    mode = to_time_series_mode("TS_FORWARD_MODE")
    
    # Convert string to Exercise Type
    exercise = to_exercise_type("EUROPEAN")
    
    # Convert string to Currency Pair
    pair = to_ccy_pair("EUR/USD")
    
    # Convert string to Barrier Type
    barrier_type = to_barrier_type("UP_IN")

Time Series
--------

**Function Signature**

.. code-block:: python

    create_time_series(dates, values, mode, name=None)

**Parameters**

* **dates** (*list*) - List of datetime objects representing the series dates
* **values** (*list*) - List of values corresponding to each date
* **mode** (*str*) - Mode of the time series (e.g., "TS_FORWARD_MODE")
* **name** (*str, optional*) - Name of the time series

**Returns**

* Time series object

**Example**

.. code-block:: python

    from datetime import datetime
    from caplib.market import create_time_series
    from caplib.datetime import create_date
    
    # Create dates for time series
    as_of_date = datetime(2025, 3, 20)
    dates = [
        as_of_date,
        create_date(as_of_date, "1M", "MODIFIED_FOLLOWING", ["US"]),
        create_date(as_of_date, "2M", "MODIFIED_FOLLOWING", ["US"]),
        create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"])
    ]
    
    # Create values
    values = [100.0, 101.0, 102.0, 103.0]
    
    # Create time series
    ts = create_time_series(
        dates=dates,
        values=values,
        mode="TS_FORWARD_MODE",
        name="EQUITY_PRICE_TS"
    )

Fixing Schedules
--------------

**Function Signature**

.. code-block:: python

    create_fixing_schedule(fixing_dates, fixing_values, fixing_weights)

**Parameters**

* **fixing_dates** (*list*) - List of datetime objects representing fixing dates
* **fixing_values** (*list*) - List of values for each fixing date
* **fixing_weights** (*list*) - List of weights for each fixing date

**Returns**

* Fixing schedule object

**Example**

.. code-block:: python

    from caplib.market import create_fixing_schedule
    
    # Create fixing dates
    fixing_dates = [
        create_date(as_of_date, "1M", "MODIFIED_FOLLOWING", ["US"]),
        create_date(as_of_date, "2M", "MODIFIED_FOLLOWING", ["US"]),
        create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"])
    ]
    
    # Create equal-weighted fixing schedule
    fixing_schedule = create_fixing_schedule(
        fixing_dates=fixing_dates,
        fixing_values=[0.0, 0.0, 0.0],  # Initial values
        fixing_weights=[1/3, 1/3, 1/3]  # Equal weights
    )

Foreign Exchange Rates
-------------------

**Function Signatures**

.. code-block:: python

    create_foreign_exchange_rate(value, base_currency, target_currency)
    create_fx_spot_rate(fx_rate, ref_date, spot_date)
    create_fx_spot_template(inst_name, currency_pair, spot_day_convention, calendars, spot_delay)

**Parameters for create_foreign_exchange_rate**

* **value** (*float*) - Exchange rate value
* **base_currency** (*str*) - Base currency code
* **target_currency** (*str*) - Target currency code

**Parameters for create_fx_spot_rate**

* **fx_rate** (*object*) - Foreign exchange rate object
* **ref_date** (*datetime*) - Reference date
* **spot_date** (*datetime*) - Spot date for the FX rate

**Parameters for create_fx_spot_template**

* **inst_name** (*str*) - Name of the FX spot template
* **currency_pair** (*str*) - Currency pair (e.g., "EUR/USD")
* **spot_day_convention** (*str*) - Day convention for spot dates
* **calendars** (*list*) - List of calendar strings
* **spot_delay** (*str*) - Delay for spot date (e.g., "2D")

**Returns**

* Foreign exchange rate, FX spot rate, or FX spot template object

**Example**

.. code-block:: python

    from caplib.market import create_foreign_exchange_rate, create_fx_spot_rate, create_fx_spot_template
    
    # Create foreign exchange rate
    fx_rate = create_foreign_exchange_rate(
        value=1.08,
        base_currency="EUR",
        target_currency="USD"
    )
    
    # Create FX spot rate
    spot_date = create_date(as_of_date, "2D", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    fx_spot = create_fx_spot_rate(
        fx_rate=fx_rate,
        ref_date=as_of_date,
        spot_date=spot_date
    )
    
    # Create FX spot template
    fx_spot_template = create_fx_spot_template(
        inst_name="EUR/USD_SPOT",
        currency_pair="EUR/USD",
        spot_day_convention="MODIFIED_FOLLOWING",
        calendars=["TARGET", "US"],
        spot_delay="2D"
    )

Barrier Creation
-------------

**Function Signature**

.. code-block:: python

    create_barrier(barrier_type, barrier_value)

**Parameters**

* **barrier_type** (*str*) - Type of barrier (e.g., "UP_IN", "DOWN_OUT")
* **barrier_value** (*float*) - Barrier level value

**Returns**

* Barrier object

**Example**

.. code-block:: python

    from caplib.market import create_barrier
    
    # Create an up barrier at 110.0
    up_barrier = create_barrier(
        barrier_type="UP_IN",
        barrier_value=110.0
    )
    
    # Create a down barrier at 90.0
    down_barrier = create_barrier(
        barrier_type="DOWN_OUT",
        barrier_value=90.0
    )

Option Creation
-----------

The module provides comprehensive functions for creating various types of options.

European Options
~~~~~~~~~~~

**Function Signature**

.. code-block:: python

    create_european_option(payoff_type, expiry, delivery, strike, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **strike** (*float*) - Strike price of the option
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "EQUITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* European option object

**Example**

.. code-block:: python

    from caplib.market import create_european_option
    
    # Create a European call option
    european_call = create_european_option(
        payoff_type="CALL",
        expiry=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "3M+2D", "MODIFIED_FOLLOWING", ["US"]),
        strike=100.0,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="EQUITY",
        underlying_ccy="USD",
        underlying="AAPL"
    )

American Options
~~~~~~~~~~~

**Function Signature**

.. code-block:: python

    create_american_option(payoff_type, expiry, strike, settlement_days, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **expiry** (*datetime*) - Expiry date of the option
* **strike** (*float*) - Strike price of the option
* **settlement_days** (*int*) - Number of days for settlement
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "EQUITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* American option object

**Example**

.. code-block:: python

    from caplib.market import create_american_option
    
    # Create an American put option
    american_put = create_american_option(
        payoff_type="PUT",
        expiry=create_date(as_of_date, "6M", "MODIFIED_FOLLOWING", ["US"]),
        strike=50.0,
        settlement_days=2,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="EQUITY",
        underlying_ccy="USD",
        underlying="MSFT"
    )

Asian Options
~~~~~~~~

**Function Signature**

.. code-block:: python

    create_asian_option(payoff_type, expiry, delivery, strike_type, strike, avg_method, obs_type, fixing_schedule, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **strike_type** (*str*) - Type of strike (e.g., "FIXED_STRIKE")
* **strike** (*float*) - Strike price of the option
* **avg_method** (*str*) - Averaging method (e.g., "ARITHMETIC")
* **obs_type** (*str*) - Observation type (e.g., "FIXINGS")
* **fixing_schedule** (*object*) - Fixing schedule object
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "COMMODITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* Asian option object

**Example**

.. code-block:: python

    from caplib.market import create_asian_option
    
    # Create an Asian average price call option
    asian_call = create_asian_option(
        payoff_type="CALL",
        expiry=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "3M+2D", "MODIFIED_FOLLOWING", ["US"]),
        strike_type="FIXED_STRIKE",
        strike=45.0,
        avg_method="ARITHMETIC",
        obs_type="FIXINGS",
        fixing_schedule=fixing_schedule,  # From previous example
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="COMMODITY",
        underlying_ccy="USD",
        underlying="WTI"
    )

Digital Options
~~~~~~~~~~

**Function Signature**

.. code-block:: python

    create_digital_option(payoff_type, expiry, delivery, strike, cash, asset, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **strike** (*float*) - Strike price of the option
* **cash** (*float*) - Cash amount of the option
* **asset** (*float*) - Asset amount of the option
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "FX")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* Digital option object

**Example**

.. code-block:: python

    from caplib.market import create_digital_option
    
    # Create a digital option
    digital_option = create_digital_option(
        payoff_type="CALL",
        expiry=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "3M+2D", "MODIFIED_FOLLOWING", ["US"]),
        strike=1.10,
        cash=100000.0,
        asset=0.0,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="FX",
        underlying_ccy="USD",
        underlying="EUR/USD"
    )

Barrier Options
~~~~~~~~~~~

**Function Signature**

.. code-block:: python

    create_single_barrier_option(payoff_type, strike, expiry, delivery, barrier_type, barrier_value, barrier_obs_type, obs_schedule, payment_type, cash_rebate, asset_rebate, settlement_days, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **strike** (*float*) - Strike price of the option
* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **barrier_type** (*str*) - Type of barrier (e.g., "UP_OUT")
* **barrier_value** (*float*) - Barrier level value
* **barrier_obs_type** (*str*) - Observation type of the barrier (e.g., "CONTINUOUS")
* **obs_schedule** (*list*) - Observation schedule for the barrier
* **payment_type** (*str*) - Type of payment (e.g., "CASH")
* **cash_rebate** (*float*) - Cash rebate amount
* **asset_rebate** (*float*) - Asset rebate amount
* **settlement_days** (*int*) - Number of days for settlement
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "EQUITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* Single barrier option object

**Example**

.. code-block:: python

    from caplib.market import create_single_barrier_option
    
    # Create a single barrier option
    single_barrier = create_single_barrier_option(
        payoff_type="CALL",
        strike=100.0,
        expiry=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "3M+2D", "MODIFIED_FOLLOWING", ["US"]),
        barrier_type="UP_OUT",
        barrier_value=110.0,
        barrier_obs_type="CONTINUOUS",
        obs_schedule=[],  # Continuous observation
        payment_type="CASH",
        cash_rebate=5000.0,
        asset_rebate=0.0,
        settlement_days=2,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="EQUITY",
        underlying_ccy="USD",
        underlying="AAPL"
    )

Touch Options
~~~~~~~~~

**Function Signature**

.. code-block:: python

    create_one_touch_option(expiry, delivery, barrier_type, barrier_value, barrier_obs_type, obs_schedule, payment_type, cash, asset, settlement_days, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **barrier_type** (*str*) - Type of barrier (e.g., "UP")
* **barrier_value** (*float*) - Barrier level value
* **barrier_obs_type** (*str*) - Observation type of the barrier (e.g., "CONTINUOUS")
* **obs_schedule** (*list*) - Observation schedule for the barrier
* **payment_type** (*str*) - Type of payment (e.g., "CASH")
* **cash** (*float*) - Cash amount of the option
* **asset** (*float*) - Asset amount of the option
* **settlement_days** (*int*) - Number of days for settlement
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "EQUITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* One touch option object

**Example**

.. code-block:: python

    from caplib.market import create_one_touch_option
    
    # Create a one-touch option
    one_touch = create_one_touch_option(
        expiry=create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "3M+2D", "MODIFIED_FOLLOWING", ["US"]),
        barrier_type="UP",
        barrier_value=110.0,
        barrier_obs_type="CONTINUOUS",
        obs_schedule=[],  # Continuous observation
        payment_type="CASH",
        cash=50000.0,
        asset=0.0,
        settlement_days=2,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="EQUITY",
        underlying_ccy="USD",
        underlying="AAPL"
    )

Structured Products
----------------

The module includes functions for creating structured products like Shark Fin options.

**Function Signature**

.. code-block:: python

    create_single_shark_fin_option(payoff_type, strike, expiry, delivery, gearing, performance_type, barrier_type, barrier_value, barrier_obs_type, obs_schedule, payment_type, cash_rebate, asset_rebate, settlement_days, nominal, payoff_ccy, underlying_type, underlying_ccy, underlying)

**Parameters**

* **payoff_type** (*str*) - Type of option payoff (e.g., "CALL", "PUT")
* **strike** (*float*) - Strike price of the option
* **expiry** (*datetime*) - Expiry date of the option
* **delivery** (*datetime*) - Delivery date of the option
* **gearing** (*float*) - Gearing of the option
* **performance_type** (*str*) - Type of performance (e.g., "ABSOLUTE")
* **barrier_type** (*str*) - Type of barrier (e.g., "UP_OUT")
* **barrier_value** (*float*) - Barrier level value
* **barrier_obs_type** (*str*) - Observation type of the barrier (e.g., "CONTINUOUS")
* **obs_schedule** (*list*) - Observation schedule for the barrier
* **payment_type** (*str*) - Type of payment (e.g., "CASH")
* **cash_rebate** (*float*) - Cash rebate amount
* **asset_rebate** (*float*) - Asset rebate amount
* **settlement_days** (*int*) - Number of days for settlement
* **nominal** (*float*) - Nominal amount of the option
* **payoff_ccy** (*str*) - Currency of the payoff
* **underlying_type** (*str*) - Type of the underlying (e.g., "EQUITY")
* **underlying_ccy** (*str*) - Currency of the underlying
* **underlying** (*str*) - Identifier of the underlying

**Returns**

* Single Shark Fin option object

**Example**

.. code-block:: python

    from caplib.market import create_single_shark_fin_option
    
    # Create a single Shark Fin option
    shark_fin = create_single_shark_fin_option(
        payoff_type="CALL",
        strike=100.0,
        expiry=create_date(as_of_date, "6M", "MODIFIED_FOLLOWING", ["US"]),
        delivery=create_date(as_of_date, "6M+2D", "MODIFIED_FOLLOWING", ["US"]),
        gearing=1.5,
        performance_type="ABSOLUTE",
        barrier_type="UP_OUT",
        barrier_value=115.0,
        barrier_obs_type="CONTINUOUS",
        obs_schedule=[],  # Continuous observation
        payment_type="CASH",
        cash_rebate=10000.0,
        asset_rebate=0.0,
        settlement_days=2,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="EQUITY",
        underlying_ccy="USD",
        underlying="AAPL"
    )

Complete Workflow Example
--------------------

Here's a complete workflow demonstrating how to create and combine various market objects:

.. code-block:: python

    from datetime import datetime
    from caplib.datetime import create_date
    from caplib.market import (
        create_time_series,
        create_foreign_exchange_rate,
        create_fx_spot_rate,
        create_european_option,
        to_ccy_pair,
        to_payoff_type
    )
    
    # Step 1: Set up date
    as_of_date = datetime(2025, 3, 20)
    
    # Step 2: Create FX rate
    fx_rate = create_foreign_exchange_rate(
        value=1.08,
        base_currency="EUR",
        target_currency="USD"
    )
    
    # Step 3: Create spot date and rate
    spot_date = create_date(as_of_date, "2D", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    fx_spot = create_fx_spot_rate(
        fx_rate=fx_rate,
        ref_date=as_of_date,
        spot_date=spot_date
    )
    
    # Step 4: Create time series for volatility
    vol_dates = [
        as_of_date,
        create_date(as_of_date, "1M", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        create_date(as_of_date, "2M", "MODIFIED_FOLLOWING", ["TARGET", "US"]),
        create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    ]
    
    vol_values = [0.10, 0.11, 0.12, 0.13]  # Volatilities
    
    vol_ts = create_time_series(
        dates=vol_dates,
        values=vol_values,
        mode="TS_FORWARD_MODE",
        name="EUR_USD_VOL_TS"
    )
    
    # Step 5: Create FX option
    expiry_date = create_date(as_of_date, "3M", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    delivery_date = create_date(expiry_date, "2D", "MODIFIED_FOLLOWING", ["TARGET", "US"])
    
    fx_option = create_european_option(
        payoff_type="CALL",
        expiry=expiry_date,
        delivery=delivery_date,
        strike=1.10,
        nominal=1000000.0,
        payoff_ccy="USD",
        underlying_type="FX",
        underlying_ccy="USD",
        underlying="EUR/USD"
    )
    
    # Step 6: Output information
    print(f"As-of Date: {as_of_date}")
    print(f"FX Rate: {fx_rate.value} {fx_rate.base_currency}/{fx_rate.target_currency}")
    print(f"FX Spot Date: {spot_date}")
    print(f"Option Expiry: {expiry_date}")
    print(f"Option Delivery: {delivery_date}")
    print(f"Option Strike: {fx_option.strike}")
    print(f"Option Nominal: {fx_option.nominal} {fx_option.payoff_ccy}")
    print(f"3M Volatility: {vol_values[3] * 100}%")
