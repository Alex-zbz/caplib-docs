Equity Analytics
===============

The eqanalytics module provides functions for creating equity risk settings, market data sets, dividend curves, volatility surfaces, and pricing various equity derivatives.

.. contents:: Table of Contents
   :local:
   :depth: 2

Risk Settings
-----------

These functions create risk settings for equity derivatives.

Create EQ Risk Settings
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_eq_risk_settings(ir_curve_settings, price_settings, vol_settings, price_vol_settings, dividend_curve_settings, theta_settings)

Create equity risk settings.

Parameters:
  - ``ir_curve_settings`` (object): Settings for interest rate curve risk.
  - ``price_settings`` (object): Settings for price risk.
  - ``vol_settings`` (object): Settings for volatility risk.
  - ``price_vol_settings`` (object): Settings for price-volatility risk.
  - ``dividend_curve_settings`` (object): Settings for dividend curve risk.
  - ``theta_settings`` (object): Settings for theta risk.

Returns:
  - Equity risk settings object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    risk_settings = eqanalytics.create_eq_risk_settings(
        ir_curve_settings=ir_curve_settings,
        price_settings=price_settings,
        vol_settings=vol_settings,
        price_vol_settings=price_vol_settings,
        dividend_curve_settings=dividend_curve_settings,
        theta_settings=theta_settings
    )

Market Data
--------

These functions create market data sets for equity derivatives.

Create EQ Market Data Set
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_eq_mkt_data_set(as_of_date, discount_curve, underlying_price, vol_surf, dividend_curve, quanto_discount_curve, quanto_fx_vol_curve, quanto_correlation, underlying)

Create an equity market data set.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the market data.
  - ``discount_curve`` (object): Discount curve for the equity.
  - ``underlying_price`` (float): Price of the underlying equity.
  - ``vol_surf`` (object): Volatility surface for the equity.
  - ``dividend_curve`` (object): Dividend curve for the equity.
  - ``quanto_discount_curve`` (object, optional): Quanto discount curve, if applicable.
  - ``quanto_fx_vol_curve`` (object, optional): Quanto FX volatility curve, if applicable.
  - ``quanto_correlation`` (float, optional): Quanto correlation, if applicable.
  - ``underlying`` (str, optional): Identifier for the underlying equity.

Returns:
  - Equity market data set object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    mkt_data = eqanalytics.create_eq_mkt_data_set(
        as_of_date="2025-03-20",
        discount_curve=usd_curve,
        underlying_price=100.0,
        vol_surf=spy_vol_surface,
        dividend_curve=spy_dividend_curve,
        quanto_discount_curve=None,
        quanto_fx_vol_curve=None,
        quanto_correlation=0.0,
        underlying="SPY"
    )
    
Build EQ Index Dividend Curve
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    build_eq_index_dividend_curve(as_of_date, term_dates, future_prices, call_price_matrix, put_price_matrix, strike_matrix, spot, discount_curve, name)

Build an equity index dividend curve.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the dividend curve.
  - ``term_dates`` (list): List of term dates for the dividend curve.
  - ``future_prices`` (list): List of future prices corresponding to term dates.
  - ``call_price_matrix`` (list of lists): Matrix of call option prices.
  - ``put_price_matrix`` (list of lists): Matrix of put option prices.
  - ``strike_matrix`` (list of lists): Matrix of strike prices corresponding to option prices.
  - ``spot`` (float): Spot price of the underlying equity index.
  - ``discount_curve`` (object): Discount curve used for calculations.
  - ``name`` (str): Name of the dividend curve.

Returns:
  - Dividend curve object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    # Define inputs for dividend curve construction
    as_of_date = "2025-03-20"
    term_dates = ["2025-06-20", "2025-09-20", "2025-12-20", "2026-03-20"]
    future_prices = [102.0, 103.5, 105.0, 106.5]
    
    # Option matrices
    strike_matrix = [
        [95.0, 97.5, 100.0, 102.5, 105.0],
        [92.5, 95.0, 100.0, 105.0, 107.5],
        [90.0, 95.0, 100.0, 105.0, 110.0],
        [90.0, 95.0, 100.0, 105.0, 110.0]
    ]
    
    call_price_matrix = [
        [6.89, 4.82, 2.95, 1.58, 0.75],
        [10.21, 7.69, 3.92, 1.62, 0.71],
        [13.42, 9.86, 5.83, 2.85, 1.14],
        [15.83, 11.98, 7.51, 3.98, 1.83]
    ]
    
    put_price_matrix = [
        [0.59, 0.94, 1.56, 2.68, 4.34],
        [0.51, 0.87, 2.11, 4.68, 6.26],
        [0.67, 1.12, 2.08, 4.10, 7.39],
        [0.83, 1.99, 3.53, 6.00, 9.26]
    ]
    
    dividend_curve = eqanalytics.build_eq_index_dividend_curve(
        as_of_date=as_of_date,
        term_dates=term_dates,
        future_prices=future_prices,
        call_price_matrix=call_price_matrix,
        put_price_matrix=put_price_matrix,
        strike_matrix=strike_matrix,
        spot=100.0,
        discount_curve=usd_curve,
        name="SPY_DIV"
    )

Dividend Curve Construction
-------------------------

.. code-block:: python

    from caplib.eqanalytics import build_eq_index_dividend_curve
    import numpy as np
    
    # Define inputs for dividend curve construction
    as_of_date = "2025-03-20"
    term_dates = ["2025-06-20", "2025-09-20", "2025-12-20", "2026-03-20"]
    future_prices = [102.0, 103.5, 105.0, 106.5]
    
    # Option matrices
    strike_matrix = [
        [95.0, 97.5, 100.0, 102.5, 105.0],
        [92.5, 95.0, 100.0, 105.0, 107.5],
        [90.0, 95.0, 100.0, 105.0, 110.0],
        [90.0, 95.0, 100.0, 105.0, 110.0]
    ]
    
    call_price_matrix = [
        [6.89, 4.82, 2.95, 1.58, 0.75],
        [10.21, 7.69, 3.92, 1.62, 0.71],
        [13.42, 9.86, 5.83, 2.85, 1.14],
        [15.83, 11.98, 7.51, 3.98, 1.83]
    ]
    
    put_price_matrix = [
        [0.59, 0.94, 1.56, 2.68, 4.34],
        [0.51, 0.87, 2.11, 4.68, 6.26],
        [0.67, 1.12, 2.08, 4.10, 7.39],
        [0.83, 1.99, 3.53, 6.00, 9.26]
    ]
    
    # Build the dividend curve
    dividend_curve = build_eq_index_dividend_curve(
        as_of_date=as_of_date,
        term_dates=term_dates,
        future_prices=future_prices,
        call_price_matrix=call_price_matrix,
        put_price_matrix=put_price_matrix,
        strike_matrix=strike_matrix,
        spot=100.0,
        discount_curve=usd_curve,
        name="SPY_DIV"
    )

Volatility Surface Construction
------------------------------

Create EQ Option Quote Matrix
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_eq_option_quote_matrix(exercise_type, underlying_type, term_dates, payoff_types, option_prices, option_strikes, underlying)

Create an equity option quote matrix for volatility surface construction.

Parameters:
  - ``exercise_type`` (str): Type of option exercise (e.g., "EUROPEAN").
  - ``underlying_type`` (str): Type of option underlying (e.g., "EQUITY").
  - ``term_dates`` (list): List of term dates for the options.
  - ``payoff_types`` (list): List of payoff types (e.g., ["CALL", "PUT"]).
  - ``option_prices`` (list): List of option prices corresponding to strikes and terms.
  - ``option_strikes`` (list): List of strike prices.
  - ``underlying`` (str, optional): Identifier for the underlying equity.

Returns:
  - Option quote matrix object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    option_quote_matrix = eqanalytics.create_eq_option_quote_matrix(
        exercise_type="EUROPEAN",
        underlying_type="EQUITY",
        term_dates=["2025-06-20", "2025-09-20", "2025-12-20", "2026-03-20"],
        payoff_types=["CALL", "PUT"],
        option_prices=[call_prices, put_prices],
        option_strikes=[90.0, 95.0, 100.0, 105.0, 110.0],
        underlying="SPY"
    )

EQ Vol Surface Builder
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_vol_surface_builder(as_of_date, smile_method, wing_strike_type, lower, upper, option_quote_matrix, underlying_prices, discount_curve, dividend_curve, pricing_settings, building_settings, underlying)

Build an equity volatility surface.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the volatility surface.
  - ``smile_method`` (str): Method for modeling volatility smile (e.g., "CUBIC_SPLINE").
  - ``wing_strike_type`` (str): Type of wing strike (e.g., "ABSOLUTE").
  - ``lower`` (float): Lower bound for the volatility surface.
  - ``upper`` (float): Upper bound for the volatility surface.
  - ``option_quote_matrix`` (object): Option quote matrix.
  - ``underlying_prices`` (list): List of underlying prices.
  - ``discount_curve`` (object): Discount curve.
  - ``dividend_curve`` (object): Dividend curve.
  - ``pricing_settings`` (object): Pricing settings.
  - ``building_settings`` (list): Building settings.
  - ``underlying`` (str): Identifier for the underlying equity.

Returns:
  - Volatility surface object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    vol_surface = eqanalytics.eq_vol_surface_builder(
        as_of_date="2025-03-20",
        smile_method="CUBIC_SPLINE",
        wing_strike_type="ABSOLUTE",
        lower=80.0,
        upper=120.0,
        option_quote_matrix=option_quote_matrix,
        underlying_prices=[100.0],
        discount_curve=usd_curve,
        dividend_curve=dividend_curve,
        pricing_settings=pricing_settings,
        building_settings=vol_building_settings,
        underlying="SPY"
    )

Vanilla Equity Options
-------------------

These functions price standard equity options.

EQ European Option Pricer
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_european_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a European equity option.

Parameters:
  - ``instrument`` (object): The European option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - European option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    european_results = eqanalytics.eq_european_option_pricer(
        instrument=european_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ American Option Pricer
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_american_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price an American equity option.

Parameters:
  - ``instrument`` (object): The American option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - American option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    american_results = eqanalytics.eq_american_option_pricer(
        instrument=american_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Asian Option Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_asian_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price an Asian equity option.

Parameters:
  - ``instrument`` (object): The Asian option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Asian option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    asian_results = eqanalytics.eq_asian_option_pricer(
        instrument=asian_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Digital Option Pricer
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_digital_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a digital equity option.

Parameters:
  - ``instrument`` (object): The digital option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Digital option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    digital_results = eqanalytics.eq_digital_option_pricer(
        instrument=digital_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Exotic Equity Options
-------------------

These functions price exotic equity derivatives.

EQ Single Barrier Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_single_barrier_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a single barrier equity option.

Parameters:
  - ``instrument`` (object): The single barrier option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Single barrier option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    barrier_results = eqanalytics.eq_single_barrier_option_pricer(
        instrument=barrier_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Double Barrier Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_double_barrier_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a double barrier equity option.

Parameters:
  - ``instrument`` (object): The double barrier option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Double barrier option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    dbl_barrier_results = eqanalytics.eq_double_barrier_option_pricer(
        instrument=dbl_barrier_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ One Touch Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_one_touch_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a one touch equity option.

Parameters:
  - ``instrument`` (object): The one touch option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - One touch option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    one_touch_results = eqanalytics.eq_one_touch_option_pricer(
        instrument=one_touch_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Double Touch Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_double_touch_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a double touch equity option.

Parameters:
  - ``instrument`` (object): The double touch option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Double touch option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    double_touch_results = eqanalytics.eq_double_touch_option_pricer(
        instrument=double_touch_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Range Accrual Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_range_accrual_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a range accrual equity option.

Parameters:
  - ``instrument`` (object): The range accrual option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Range accrual option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    range_accrual_results = eqanalytics.eq_range_accrual_option_pricer(
        instrument=range_accrual_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Structured Equity Products
-----------------------

These functions price complex structured equity products.

EQ Single Shark Fin Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_single_shark_fin_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a single shark fin equity option.

Parameters:
  - ``instrument`` (object): The single shark fin option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Single shark fin option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    shark_fin_results = eqanalytics.eq_single_shark_fin_option_pricer(
        instrument=shark_fin_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Double Shark Fin Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_double_shark_fin_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a double shark fin equity option.

Parameters:
  - ``instrument`` (object): The double shark fin option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Double shark fin option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    dbl_shark_fin_results = eqanalytics.eq_double_shark_fin_option_pricer(
        instrument=dbl_shark_fin_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Ping Pong Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_ping_pong_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a ping pong equity option.

Parameters:
  - ``instrument`` (object): The ping pong option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Ping pong option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    ping_pong_results = eqanalytics.eq_ping_pong_option_pricer(
        instrument=ping_pong_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Airbag Option Pricer
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_airbag_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price an airbag equity option.

Parameters:
  - ``instrument`` (object): The airbag option instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Airbag option pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    airbag_results = eqanalytics.eq_airbag_option_pricer(
        instrument=airbag_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Snowball Auto Callable Note Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_snowball_auto_callable_note_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a snowball auto callable equity note.

Parameters:
  - ``instrument`` (object): The snowball auto callable note instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Snowball auto callable note pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    snowball_results = eqanalytics.eq_snowball_auto_callable_note_pricer(
        instrument=snowball_note,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

EQ Phoenix Auto Callable Note Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    eq_phoenix_auto_callable_note_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a phoenix auto callable equity note.

Parameters:
  - ``instrument`` (object): The phoenix auto callable note instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Phoenix auto callable note pricing result object

Example:

.. code-block:: python

    import caplib.eqanalytics as eqanalytics
    
    phoenix_results = eqanalytics.eq_phoenix_auto_callable_note_pricer(
        instrument=phoenix_note,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )
