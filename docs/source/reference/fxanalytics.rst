FX Analytics
===========

The foreign exchange analytics module provides functions for FX market data setup, volatility surface construction, pricing FX forwards and various FX options including vanilla and exotic derivatives.

Market Data Setup
--------------

These functions help create market data sets and risk settings for FX instruments.

FX Risk Settings
~~~~~~~~~~~~

.. code-block:: python

    create_fx_risk_settings(ir_curve_settings, price_settings, vol_settings, price_vol_settings, theta_settings)

Create risk settings for FX derivatives.

Parameters:
  - ``ir_curve_settings`` (object): Settings for interest rate curve risk.
  - ``price_settings`` (object): Settings for FX price risk.
  - ``vol_settings`` (object): Settings for volatility risks.
  - ``price_vol_settings`` (object): Settings for joint price-volatility risks.
  - ``theta_settings`` (object): Settings for theta risk.

Returns:
  - FX risk settings object

Example:

.. code-block:: python

    import caplib.analytics as analytics
    import caplib.fxanalytics as fxanalytics
    
    # Create interest rate curve risk settings
    ir_curve_settings = analytics.create_ir_curve_risk_settings(
        bump_size=0.0001,  # 1 basis point
        bump_type="ABSOLUTE_BUMP"
    )
    
    # Create price risk settings
    price_settings = analytics.create_price_risk_settings(
        bump_size=0.01,  # 1%
        bump_type="RELATIVE_BUMP"
    )
    
    # Create volatility risk settings
    vol_settings = analytics.create_vol_risk_settings(
        bump_size=0.01,  # 1 vol point
        bump_type="ABSOLUTE_BUMP"
    )
    
    # Create price-vol risk settings
    price_vol_settings = analytics.create_price_vol_risk_settings(
        price_bump_size=0.01,
        price_bump_type="RELATIVE_BUMP",
        vol_bump_size=0.01,
        vol_bump_type="ABSOLUTE_BUMP"
    )
    
    # Create theta risk settings
    theta_settings = analytics.create_theta_risk_settings(
        bump_days=1
    )
    
    # Create FX risk settings
    risk_settings = fxanalytics.create_fx_risk_settings(
        ir_curve_settings=ir_curve_settings,
        price_settings=price_settings,
        vol_settings=vol_settings,
        price_vol_settings=price_vol_settings,
        theta_settings=theta_settings
    )

FX Market Data Set
~~~~~~~~~~~~~~

.. code-block:: python

    create_fx_mkt_data_set(as_of_date, domestic_discount_curve, foreign_discount_curve, spot, vol_surf)

Create a market data set for FX instruments.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the market data.
  - ``domestic_discount_curve`` (object): Discount curve for the domestic currency.
  - ``foreign_discount_curve`` (object): Discount curve for the foreign currency.
  - ``spot`` (float): FX spot rate.
  - ``vol_surf`` (object, optional): FX volatility surface.

Returns:
  - FX market data set object

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    as_of_date = datetime(2025, 3, 20)
    
    # Create FX market data set
    mkt_data = fxanalytics.create_fx_mkt_data_set(
        as_of_date=as_of_date,
        domestic_discount_curve=usd_curve,
        foreign_discount_curve=eur_curve,
        spot=1.08,  # EUR/USD spot rate
        vol_surf=eurusd_vol_surface
    )

FX Market Conventions
~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fx_mkt_conventions(atm_type, short_delta_type, long_delta_type, short_delta_cutoff, risk_reversal, smile_quote_type, currency_pair)

Create FX market conventions for option quoting and volatility surface construction.

Parameters:
  - ``atm_type`` (str): At-the-money type, e.g., 'DELTA_NEUTRAL'.
  - ``short_delta_type`` (str): Delta type for short-dated options, e.g., 'SPOT_DELTA'.
  - ``long_delta_type`` (str): Delta type for long-dated options, e.g., 'FORWARD_DELTA'.
  - ``short_delta_cutoff`` (str): Tenor cutoff for short/long delta distinction, e.g., '1M'.
  - ``risk_reversal`` (str): Risk reversal quote type, e.g., 'TRUE_RR'.
  - ``smile_quote_type`` (str): Smile quote type, e.g., 'BUTTERFLY'.
  - ``currency_pair`` (str): Currency pair, e.g., 'EURUSD'.

Returns:
  - FX market conventions object

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create FX market conventions
    fx_conventions = fxanalytics.create_fx_mkt_conventions(
        atm_type="DELTA_NEUTRAL",
        short_delta_type="SPOT_DELTA",
        long_delta_type="FORWARD_DELTA",
        short_delta_cutoff="1M",
        risk_reversal="TRUE_RR",
        smile_quote_type="BUTTERFLY",
        currency_pair="EURUSD"
    )

FX Forward Pricing
-----------------

Functions for pricing FX forward contracts and related instruments.

FX Forward Pricer
~~~~~~~~~~~~~~

.. code-block:: python

    fx_forward_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price an FX forward contract.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): FX forward instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value and risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    # Create an FX forward instrument
    fx_forward = create_fx_forward(
        trade_date=datetime(2025, 1, 15),
        settlement_date=datetime(2025, 4, 15),
        buy_currency="EUR",
        buy_amount=1000000,
        sell_currency="USD",
        sell_amount=1090000
    )
    
    # Price the FX forward
    forward_results = fxanalytics.fx_forward_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=fx_forward,
        mkt_data=mkt_data_set,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )
    
    # Access results
    pv = forward_results.present_value
    delta = forward_results.delta

FX Swap Pricer
~~~~~~~~~~

.. code-block:: python

    fx_swap_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price an FX swap contract.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): FX swap instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value and risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create an FX swap instrument
    fx_swap = create_fx_swap(
        trade_date=datetime(2025, 1, 15),
        near_leg_settlement_date=datetime(2025, 1, 17),
        far_leg_settlement_date=datetime(2025, 7, 17),
        buy_currency="EUR",
        near_leg_buy_amount=1000000,
        far_leg_buy_amount=1000000,
        sell_currency="USD",
        near_leg_sell_amount=1090000,
        far_leg_sell_amount=1100000
    )
    
    # Price the FX swap
    swap_results = fxanalytics.fx_swap_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=fx_swap,
        mkt_data=mkt_data_set,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

FX NDF Pricer
~~~~~~~~~

.. code-block:: python

    fx_ndf_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a non-deliverable forward (NDF) contract.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): FX NDF instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value and risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create an FX NDF instrument
    fx_ndf = create_fx_ndf(
        trade_date=datetime(2025, 1, 15),
        settlement_date=datetime(2025, 4, 15),
        fixing_date=datetime(2025, 4, 13),
        currency_pair="USDCNY",
        notional_currency="USD",
        notional_amount=1000000,
        forward_rate=6.45,
        settlement_currency="USD"
    )
    
    # Price the FX NDF
    ndf_results = fxanalytics.fx_ndf_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=fx_ndf,
        mkt_data=mkt_data_set,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Volatility Surface Construction
------------------------------

Functions for creating and manipulating FX volatility surfaces.

FX Option Quote Matrix
~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fx_option_quote_matrix(currency_pair, as_of_date, terms, deltas, quotes)

Create a matrix of FX option volatility quotes for surface construction.

Parameters:
  - ``currency_pair`` (str): Currency pair, e.g., 'EURUSD'.
  - ``as_of_date`` (datetime or str): Reference date for the quotes.
  - ``terms`` (list): List of tenors, e.g., ['1W', '1M', '3M', '6M', '1Y'].
  - ``deltas`` (list): List of delta values, e.g., [0.10, 0.25, 0.50, 0.75, 0.90].
  - ``quotes`` (numpy.ndarray): 2D array of volatility quotes in decimal form.

Returns:
  - FX option quote matrix object.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    import numpy as np
    from datetime import datetime
    
    # Define terms and deltas
    terms = ["1W", "1M", "3M", "6M", "1Y"]
    deltas = [0.10, 0.25, 0.50, 0.75, 0.90]
    
    # Create volatility quote matrix (terms x deltas)
    quotes = np.array([
        [12.5, 10.2, 9.8, 10.5, 12.8],  # 1W vols
        [13.2, 11.0, 10.2, 11.2, 13.5],  # 1M vols
        [13.8, 11.5, 10.8, 11.8, 14.0],  # 3M vols
        [14.5, 12.2, 11.5, 12.5, 14.8],  # 6M vols
        [15.2, 13.0, 12.2, 13.2, 15.5]   # 1Y vols
    ]) / 100.0  # Convert from percentage to decimal
    
    # Create the quote matrix
    quote_matrix = fxanalytics.create_fx_option_quote_matrix(
        currency_pair="EURUSD",
        as_of_date=datetime(2025, 3, 20),
        terms=terms,
        deltas=deltas,
        quotes=quotes
    )

FX Volatility Surface
~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fx_volatility_surface(as_of_date, currency_pair, term_dates, strikes, vols, fx_market_conventions, vol_surf_definition)

Create an FX volatility surface from a grid of strikes and volatilities.

Parameters:
  - ``as_of_date`` (datetime or str): Reference date for the surface.
  - ``currency_pair`` (str): Currency pair, e.g., 'EURUSD'.
  - ``term_dates`` (list): List of term dates.
  - ``strikes`` (numpy.ndarray): 2D array of strike prices.
  - ``vols`` (numpy.ndarray): 2D array of volatilities corresponding to strikes.
  - ``fx_market_conventions`` (object): FX market conventions.
  - ``vol_surf_definition`` (object): Volatility surface definition settings.

Returns:
  - FX volatility surface object.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    import numpy as np
    from datetime import datetime, timedelta
    
    # Create term dates
    as_of_date = datetime(2025, 3, 20)
    term_dates = [
        as_of_date + timedelta(days=7),    # 1W
        as_of_date + timedelta(days=30),   # 1M
        as_of_date + timedelta(days=91),   # 3M
        as_of_date + timedelta(days=182),  # 6M
        as_of_date + timedelta(days=365)   # 1Y
    ]
    
    # Create strike grid and volatility grid
    strikes = np.array([
        [1.00, 1.02, 1.05, 1.08, 1.10, 1.12, 1.15],  # 1W strikes
        [0.98, 1.00, 1.05, 1.08, 1.10, 1.15, 1.18],  # 1M strikes
        [0.95, 0.98, 1.02, 1.08, 1.12, 1.18, 1.22],  # 3M strikes
        [0.92, 0.95, 1.00, 1.08, 1.15, 1.20, 1.25],  # 6M strikes
        [0.90, 0.95, 1.00, 1.08, 1.15, 1.22, 1.30]   # 1Y strikes
    ])
    
    vols = np.array([
        [0.125, 0.115, 0.105, 0.098, 0.105, 0.115, 0.125],  # 1W vols
        [0.132, 0.120, 0.110, 0.102, 0.110, 0.120, 0.132],  # 1M vols
        [0.138, 0.125, 0.115, 0.108, 0.115, 0.125, 0.138],  # 3M vols
        [0.145, 0.130, 0.120, 0.115, 0.120, 0.130, 0.145],  # 6M vols
        [0.152, 0.135, 0.125, 0.122, 0.125, 0.135, 0.152]   # 1Y vols
    ])
    
    # Create volatility surface
    vol_surface = fxanalytics.create_fx_volatility_surface(
        as_of_date=as_of_date,
        currency_pair="EURUSD",
        term_dates=term_dates,
        strikes=strikes,
        vols=vols,
        fx_market_conventions=fx_conventions,
        vol_surf_definition=vol_definition
    )

Flat FX Volatility Surface
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_flat_fx_volatility_surface(as_of_date, currency_pair, vol)

Create a flat FX volatility surface with constant volatility across all strikes and maturities.

Parameters:
  - ``as_of_date`` (datetime or str): Reference date for the surface.
  - ``currency_pair`` (str): Currency pair, e.g., 'EURUSD'.
  - ``vol`` (float): Constant volatility value in decimal form.

Returns:
  - Flat FX volatility surface object.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    # Create a flat volatility surface
    flat_vol_surface = fxanalytics.create_flat_fx_volatility_surface(
        as_of_date=datetime(2025, 3, 20),
        currency_pair="EURUSD",
        vol=0.10  # 10% flat volatility
    )

FX Volatility Surface Builder
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_volatility_surface_builder(as_of_date, currency_pair, fx_market_conventions, quotes, fx_spot_rate, dom_discount_curve, for_discount_curve, vol_surf_definitions, vol_surf_building_settings)

Build an FX volatility surface from market quotes.

Parameters:
  - ``as_of_date`` (datetime or str): Reference date for the surface.
  - ``currency_pair`` (str): Currency pair, e.g., 'EURUSD'.
  - ``fx_market_conventions`` (object): FX market conventions.
  - ``quotes`` (object): Quote matrix from ``create_fx_option_quote_matrix``.
  - ``fx_spot_rate`` (float): FX spot exchange rate.
  - ``dom_discount_curve`` (object): Domestic currency discount curve.
  - ``for_discount_curve`` (object): Foreign currency discount curve.
  - ``vol_surf_definitions`` (object): Volatility surface definition settings.
  - ``vol_surf_building_settings`` (object): Volatility surface building settings.

Returns:
  - Built FX volatility surface object.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Build volatility surface from market data
    built_vol_surface = fxanalytics.fx_volatility_surface_builder(
        as_of_date=datetime(2025, 3, 20), 
        currency_pair="EURUSD", 
        fx_market_conventions=fx_conventions, 
        quotes=quote_matrix,
        fx_spot_rate=1.08,
        dom_discount_curve=usd_curve,
        for_discount_curve=eur_curve, 
        vol_surf_definitions=vol_def, 
        vol_surf_building_settings=vol_settings
    )

FX Option Pricing
---------------

Functions for pricing various types of FX options.

European FX Option Pricer
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_european_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a European-style FX option.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): European FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    # Create a European FX option instrument
    eur_option = create_fx_european_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD",
        premium_currency="USD",
        premium_amount=25000,
        premium_date=datetime(2025, 1, 17)
    )
    
    # Price the European option
    european_results = fxanalytics.fx_european_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=eur_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )
    
    # Access results
    pv = european_results.present_value
    delta = european_results.delta
    gamma = european_results.gamma
    vega = european_results.vega
    theta = european_results.theta

American FX Option Pricer
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_american_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price an American-style FX option.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): American FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create an American FX option instrument
    am_option = create_fx_american_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="PUT",
        buy_sell="BUY",
        strike=1.05,
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD",
        premium_currency="USD",
        premium_amount=30000,
        premium_date=datetime(2025, 1, 17)
    )
    
    # Price the American option
    american_results = fxanalytics.fx_american_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=am_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Asian FX Option Pricer
~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_asian_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price an Asian-style FX option with averaging features.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Asian FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create an Asian FX option instrument
    asian_option = create_fx_asian_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.08,
        averaging_type="ARITHMETIC",
        fixing_dates=[datetime(2025, 5, 15), datetime(2025, 6, 15), datetime(2025, 7, 15)],
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD"
    )
    
    # Price the Asian option
    asian_results = fxanalytics.fx_asian_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=asian_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Digital FX Option Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_digital_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a digital (binary) FX option.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Digital FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a Digital FX option instrument
    digital_option = create_fx_digital_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        payout_currency="USD",
        payout_amount=100000,
        notional_currency="EUR",
        counter_currency="USD"
    )
    
    # Price the Digital option
    digital_results = fxanalytics.fx_digital_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=digital_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Exotic FX Options
---------------

Functions for pricing exotic and path-dependent FX options.

Single Barrier FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_single_barrier_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a single barrier FX option.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Single barrier FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    # Create a single barrier FX option
    barrier_option = create_fx_single_barrier_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        barrier_type="UP_AND_OUT",
        barrier_level=1.15,
        rebate=0.02,
        rebate_currency="USD",
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD"
    )
    
    # Price the single barrier option
    barrier_results = fxanalytics.fx_single_barrier_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=barrier_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Double Barrier FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_double_barrier_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a double barrier FX option with both upper and lower barriers.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Double barrier FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a double barrier FX option
    double_barrier_option = create_fx_double_barrier_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        barrier_type="KNOCK_OUT",
        lower_barrier=1.00,
        upper_barrier=1.20,
        lower_rebate=0.01,
        upper_rebate=0.01,
        rebate_currency="USD",
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD"
    )
    
    # Price the double barrier option
    double_barrier_results = fxanalytics.fx_double_barrier_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=double_barrier_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

One Touch FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_one_touch_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a one-touch FX option that pays out if the FX rate touches a specified level.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): One touch FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a one touch FX option
    one_touch_option = create_fx_one_touch_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        touch_level=1.15,
        touch_type="UP",
        payout_currency="USD",
        payout_amount=100000,
        notional_currency="EUR",
        counter_currency="USD"
    )
    
    # Price the one touch option
    one_touch_results = fxanalytics.fx_one_touch_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=one_touch_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Double Touch FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_double_touch_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a double-touch FX option that pays out if the FX rate touches both specified levels.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Double touch FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a double touch FX option
    double_touch_option = create_fx_double_touch_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        lower_touch_level=1.00,
        upper_touch_level=1.20,
        touch_type="BOTH",
        payout_currency="USD",
        payout_amount=100000,
        notional_currency="EUR",
        counter_currency="USD"
    )
    
    # Price the double touch option
    double_touch_results = fxanalytics.fx_double_touch_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=double_touch_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Range Accrual FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_range_accrual_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a range accrual FX option that pays out based on the number of days the FX rate is within a specified range.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Range accrual FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a range accrual FX option
    range_accrual_option = create_fx_range_accrual_option(
        trade_date=datetime(2025, 1, 15),
        start_date=datetime(2025, 2, 15),
        end_date=datetime(2025, 8, 15),
        settlement_date=datetime(2025, 8, 17),
        observation_frequency="DAILY",
        range_lower=1.05,
        range_upper=1.15,
        coupon_rate=0.05,
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD",
        payout_currency="USD"
    )
    
    # Price the range accrual option
    range_accrual_results = fxanalytics.fx_range_accrual_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=range_accrual_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Structured Products
---------------

Functions for pricing structured FX products.

FX Shark Fin Option Pricer
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_single_shark_fin_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a single shark fin FX option.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Shark fin FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    from datetime import datetime
    
    # Create a shark fin FX option
    shark_fin_option = create_fx_single_shark_fin_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        barrier_type="DOWN_AND_OUT",
        barrier_level=1.00,
        rebate=0.01,
        rebate_currency="USD",
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD",
        coupon_rate=0.05
    )
    
    # Price the shark fin option
    shark_fin_results = fxanalytics.fx_single_shark_fin_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=shark_fin_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

Double Shark Fin FX Option Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_double_shark_fin_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a double shark fin FX option with both upper and lower barriers.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Double shark fin FX option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a double shark fin FX option
    double_shark_fin_option = create_fx_double_shark_fin_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        strike=1.10,
        barrier_type="KNOCK_OUT",
        lower_barrier=1.00,
        upper_barrier=1.20,
        lower_rebate=0.01,
        upper_rebate=0.01,
        rebate_currency="USD",
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD",
        coupon_rate=0.06
    )
    
    # Price the double shark fin option
    double_shark_fin_results = fxanalytics.fx_double_shark_fin_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=double_shark_fin_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

FX Airbag Option Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_airbag_option_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price an FX airbag option with downside protection.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): FX airbag option instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create an FX airbag option
    airbag_option = create_fx_airbag_option(
        trade_date=datetime(2025, 1, 15),
        expiry_date=datetime(2025, 7, 15),
        settlement_date=datetime(2025, 7, 17),
        call_put="CALL",
        buy_sell="BUY",
        participation_rate=1.2,
        strike=1.10,
        airbag_level=1.05,
        notional_currency="EUR",
        notional_amount=1000000,
        counter_currency="USD"
    )
    
    # Price the airbag option
    airbag_results = fxanalytics.fx_airbag_option_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=airbag_option,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

FX Snowball Auto-Callable Note Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_snowball_auto_callable_note_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a snowball auto-callable note linked to FX rates.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Snowball auto-callable note instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a snowball auto-callable note
    snowball_note = create_fx_snowball_auto_callable_note(
        trade_date=datetime(2025, 1, 15),
        start_date=datetime(2025, 1, 17),
        maturity_date=datetime(2028, 1, 17),
        coupon_dates=[datetime(2025, 7, 17), datetime(2026, 1, 17), datetime(2026, 7, 17), 
                      datetime(2027, 1, 17), datetime(2027, 7, 17), datetime(2028, 1, 17)],
        observation_dates=[datetime(2025, 7, 15), datetime(2026, 1, 15), datetime(2026, 7, 15), 
                          datetime(2027, 1, 15), datetime(2027, 7, 15), datetime(2028, 1, 15)],
        coupon_rate=0.05,
        memory_feature=True,
        autocall_trigger=1.00,  # 100% of initial FX rate
        coupon_trigger=0.90,    # 90% of initial FX rate
        barrier_level=0.70,     # 70% of initial FX rate
        notional_currency="USD",
        notional_amount=1000000,
        underlying_currency_pair="EURUSD",
        initial_fx_rate=1.08
    )
    
    # Price the snowball note
    snowball_results = fxanalytics.fx_snowball_auto_callable_note_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=snowball_note,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

FX Phoenix Auto-Callable Note Pricer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    fx_phoenix_auto_callable_note_pricer(pricing_date, instrument, mkt_data, pricing_settings, risk_settings, scn_settings=None)

Price a phoenix auto-callable note linked to FX rates.

Parameters:
  - ``pricing_date`` (datetime or str): Valuation date.
  - ``instrument`` (object): Phoenix auto-callable note instrument.
  - ``mkt_data`` (object): Market data set created by ``create_fx_mkt_data_set``.
  - ``pricing_settings`` (object): Settings for pricing.
  - ``risk_settings`` (object): Risk settings created by ``create_fx_risk_settings``.
  - ``scn_settings`` (object, optional): Scenario settings if needed.

Returns:
  - Pricing results object containing present value, greeks, and other risk metrics.

Example:

.. code-block:: python

    import caplib.fxanalytics as fxanalytics
    
    # Create a phoenix auto-callable note
    phoenix_note = create_fx_phoenix_auto_callable_note(
        trade_date=datetime(2025, 1, 15),
        start_date=datetime(2025, 1, 17),
        maturity_date=datetime(2028, 1, 17),
        coupon_dates=[datetime(2025, 4, 17), datetime(2025, 7, 17), datetime(2025, 10, 17),
                     datetime(2026, 1, 17), datetime(2026, 4, 17), datetime(2026, 7, 17)],
        observation_dates=[datetime(2025, 4, 15), datetime(2025, 7, 15), datetime(2025, 10, 15),
                          datetime(2026, 1, 15), datetime(2026, 4, 15), datetime(2026, 7, 15)],
        autocall_dates=[datetime(2025, 7, 17), datetime(2026, 1, 17), datetime(2026, 7, 17), 
                        datetime(2027, 1, 17), datetime(2027, 7, 17)],
        coupon_rate=0.0125,  # 1.25% quarterly coupon
        autocall_trigger=1.00,  # 100% of initial FX rate
        coupon_trigger=0.85,    # 85% of initial FX rate
        barrier_level=0.65,     # 65% of initial FX rate
        notional_currency="USD",
        notional_amount=1000000,
        underlying_currency_pair="EURUSD",
        initial_fx_rate=1.08
    )
    
    # Price the phoenix note
    phoenix_results = fxanalytics.fx_phoenix_auto_callable_note_pricer(
        pricing_date=datetime(2025, 3, 20),
        instrument=phoenix_note,
        mkt_data=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings
    )

FX Analytics Utilities
--------------------

.. code-block:: python

    from caplib.fxanalytics import fx_delta_to_strike_calculator, fx_atm_strike_calculator, get_fx_volatility
    
    # Calculate strike from delta
    strike = fx_delta_to_strike_calculator(
        delta_type="SPOT_DELTA",
        delta=0.25,  # 25 delta
        expiry_date="2025-09-20",
        vol_surf=vol_surface,
        fx_spot_rate=spot_rate,
        domestic_discount_curve=usd_curve,
        foreign_discount_curve=eur_curve
    )
    
    # Calculate ATM strike
    atm_strike = fx_atm_strike_calculator(
        atm_type="DELTA_NEUTRAL",
        expiry_date="2025-09-20",
        vol_surface=vol_surface,
        fx_spot_rate=spot_rate,
        domestic_discount_curve=usd_curve,
        foreign_discount_curve=eur_curve
    )
    
    # Get volatility for a specific term and strike
    volatility = get_fx_volatility(
        fx_vol_surf=vol_surface,
        terms="6M",
        strike=1.1200
    )
