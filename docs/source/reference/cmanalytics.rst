Commodity Analytics
==================

The cmanalytics module provides functions for building commodity market curves, volatility surfaces, and pricing various commodity derivative instruments.

Market Data Functions
--------------------

These functions help create and manage commodity market data structures.

PM Par Rate Curve
~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pm_par_rate_curve(as_of_date, currency, curve_name, pillars)

Create a PM Par Rate Curve.

Parameters:
  - ``as_of_date`` (datetime): The reference date for the curve.
  - ``currency`` (str): The currency of the curve.
  - ``curve_name`` (str): The name of the curve.
  - ``pillars`` (list): List of tuples representing pillar data.

Returns:
  - ``ParCurve``

Example:

.. code-block:: python

    import caplib.cmanalytics as cmanalytics
    
    pillars = [
        ("2025-06-20", "FUTURE", "3M", 95.0),
        ("2025-09-20", "FUTURE", "6M", 94.5),
        ("2025-12-20", "FUTURE", "9M", 94.0),
        ("2026-03-20", "FUTURE", "1Y", 93.5)
    ]
    
    par_curve = cmanalytics.create_pm_par_rate_curve(
        as_of_date="2025-03-20",
        currency="USD",
        curve_name="CM_PAR_CURVE",
        pillars=pillars
    )

PM Yield Curve Builder
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    pm_yield_curve_builder(as_of_date, par_curve, inst_template, discount_curve, spot_price, curve_type, interp_method, extrap_method, day_count, curve_name, jacobian, shift, finite_diff_method, threading_mode)

Build a PM Yield Curve.

Parameters:
  - ``as_of_date`` (datetime): The reference date for the curve.
  - ``par_curve`` (ParCurve): The par rate curve.
  - ``inst_template`` (InstrumentTemplate): The instrument template.
  - ``discount_curve`` (DiscountCurve): The discount curve.
  - ``spot_price`` (float): The spot price.
  - ``curve_type`` (str): The type of the yield curve.
  - ``interp_method`` (str): The interpolation method.
  - ``extrap_method`` (str): The extrapolation method.
  - ``day_count`` (str): The day count convention.
  - ``curve_name`` (str): The name of the curve.
  - ``jacobian`` (list): The Jacobian matrix.
  - ``shift`` (float): The shift for calculation.
  - ``finite_diff_method`` (str): The finite difference method.
  - ``threading_mode`` (str): The threading mode.

Returns:
  - ``YieldCurve``

Example:

.. code-block:: python

    yield_curve = cmanalytics.pm_yield_curve_builder(
        as_of_date="2025-03-20",
        par_curve=par_curve,
        inst_template=instrument_template,
        discount_curve=discount_curve,
        spot_price=75.0,
        curve_type="ZERO_CURVE",
        interp_method="LINEAR",
        extrap_method="FLAT",
        day_count="ACT_365",
        curve_name="CM_YIELD_CURVE",
        jacobian=[],
        shift=0.0001,
        finite_diff_method="CENTRAL",
        threading_mode="MULTI_THREAD"
    )

PM Market Conventions
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pm_mkt_conventions(atm_type, short_delta_type, long_delta_type, short_delta_cutoff, risk_reversal, smile_quote_type)

Create PM market conventions.

Parameters:
  - ``atm_type`` (str): The ATM type.
  - ``short_delta_type`` (str): The short delta type.
  - ``long_delta_type`` (str): The long delta type.
  - ``short_delta_cutoff`` (str): The short delta cutoff period.
  - ``risk_reversal`` (str): The type of risk reversal.
  - ``smile_quote_type`` (str): The type of smile quote.

Returns:
  - ``ProtoPmMarketConventions``

Example:

.. code-block:: python

    mkt_conventions = cmanalytics.create_pm_mkt_conventions(
        atm_type="DELTA_NEUTRAL",
        short_delta_type="SPOT_DELTA",
        long_delta_type="FORWARD_DELTA",
        short_delta_cutoff="1M",
        risk_reversal="STANDARD",
        smile_quote_type="RISK_REVERSAL_BUTTERFLY"
    )

Option Quote Matrix Functions
----------------------------

These functions create option quote matrices for commodity markets.

PM Option Quote Matrix
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pm_option_quote_matrix(underlying, terms, payoff_types, deltas, quotes)

Create PM option quote matrix.

Parameters:
  - ``underlying`` (str): The underlying instrument.
  - ``terms`` (list): List of terms.
  - ``payoff_types`` (list): List of payoff types.
  - ``deltas`` (list): List of deltas.
  - ``quotes`` (list): List of quotes.

Returns:
  - ``OptionQuoteMatrix``

Example:

.. code-block:: python

    pm_option_matrix = cmanalytics.create_pm_option_quote_matrix(
        underlying="WTI",
        terms=["1M", "3M", "6M", "1Y"],
        payoff_types=["CALL", "PUT"],
        deltas=[10.0, 25.0, 50.0, 75.0, 90.0],
        quotes=[
            [12.5, 15.2, 18.7, 15.6, 13.1],  # 1M CALL
            [13.2, 15.9, 19.4, 16.3, 13.8],  # 1M PUT
            [15.1, 17.8, 21.5, 18.3, 15.7],  # 3M CALL
            [15.8, 18.5, 22.2, 19.0, 16.4],  # 3M PUT
            [17.2, 19.9, 23.6, 20.4, 17.8],  # 6M CALL
            [17.9, 20.6, 24.3, 21.1, 18.5],  # 6M PUT
            [18.9, 21.6, 25.3, 22.1, 19.5],  # 1Y CALL
            [19.6, 22.3, 26.0, 22.8, 20.2]   # 1Y PUT
        ]
    )

CM Option Quote Matrix
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cm_option_quote_matrix(exercise_type, underlying_type, term_dates, payoff_types, strikes, prices, underlying)

Create CM option quote matrix.

Parameters:
  - ``exercise_type`` (str): The type of option exercise.
  - ``underlying_type`` (str): The type of option underlying.
  - ``term_dates`` (list): List of term dates.
  - ``payoff_types`` (list): List of payoff types.
  - ``strikes`` (list): List of strike prices.
  - ``prices`` (list): List of option prices.
  - ``underlying`` (str): The underlying instrument.

Returns:
  - ``OptionQuoteMatrix``

Example:

.. code-block:: python

    cm_option_matrix = cmanalytics.create_cm_option_quote_matrix(
        exercise_type="EUROPEAN",
        underlying_type="COMMODITY",
        term_dates=["2025-06-20", "2025-09-20", "2025-12-20", "2026-03-20"],
        payoff_types=["CALL", "PUT"],
        strikes=[65.0, 70.0, 75.0, 80.0, 85.0],
        prices=[
            [10.55, 7.27, 4.63, 2.69, 1.44],  # 2025-06-20 CALL
            [0.78, 2.49, 4.85, 7.90, 11.65],  # 2025-06-20 PUT
            [12.87, 9.35, 6.44, 4.21, 2.65],  # 2025-09-20 CALL
            [2.13, 3.62, 5.70, 8.48, 11.91],  # 2025-09-20 PUT
            [14.76, 11.07, 7.97, 5.51, 3.68],  # 2025-12-20 CALL
            [3.01, 4.31, 6.22, 8.75, 11.93],  # 2025-12-20 PUT
            [16.39, 12.59, 9.38, 6.74, 4.69],  # 2026-03-20 CALL
            [3.85, 5.06, 6.85, 9.20, 12.15]   # 2026-03-20 PUT
        ],
        underlying="WTI"
    )

Volatility Surface Functions
---------------------------

These functions build volatility surfaces for commodity markets.

PM Volatility Surface Builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    pm_vol_surface_builder(as_of_date, vol_surf_definition, option_quote_matrix, mkt_conventions, spot_price, discount_curve, fwd_curve, building_settings, spot_template, underlying, vol_surf_name)

Build PM volatility surface.

Parameters:
  - ``as_of_date`` (datetime): The reference date.
  - ``vol_surf_definition`` (VolatilitySurfaceDefinition): The volatility surface definition.
  - ``option_quote_matrix`` (OptionQuoteMatrix): The option quote matrix.
  - ``mkt_conventions`` (ProtoPmMarketConventions): The market conventions.
  - ``spot_price`` (float): The spot price.
  - ``discount_curve`` (DiscountCurve): The discount curve.
  - ``fwd_curve`` (ForwardCurve): The forward curve.
  - ``building_settings`` (list): The building settings.
  - ``spot_template`` (SpotTemplate): The spot template.
  - ``underlying`` (str): The underlying instrument.
  - ``vol_surf_name`` (str): The name of the volatility surface.

Returns:
  - ``VolatilitySurface``

Example:

.. code-block:: python

    pm_vol_surface = cmanalytics.pm_vol_surface_builder(
        as_of_date="2025-03-20",
        vol_surf_definition=vol_surf_definition,
        option_quote_matrix=pm_option_matrix,
        mkt_conventions=mkt_conventions,
        spot_price=75.0,
        discount_curve=discount_curve,
        fwd_curve=forward_curve,
        building_settings=building_settings,
        spot_template=spot_template,
        underlying="WTI",
        vol_surf_name="WTI_VOL_SURFACE"
    )

CM Volatility Surface Builder
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    cm_vol_surface_builder(as_of_date, smile_method, wing_strike_type, lower, upper, option_quote_matrix, underlying_prices, discount_curve, fwd_curve, building_settings, underlying)

Build CM volatility surface.

Parameters:
  - ``as_of_date`` (datetime): The reference date.
  - ``smile_method`` (str): The smile method.
  - ``wing_strike_type`` (str): The wing strike type.
  - ``lower`` (float): The lower bound.
  - ``upper`` (float): The upper bound.
  - ``option_quote_matrix`` (OptionQuoteMatrix): The option quote matrix.
  - ``underlying_prices`` (list): List of underlying prices.
  - ``discount_curve`` (DiscountCurve): The discount curve.
  - ``fwd_curve`` (ForwardCurve): The forward curve.
  - ``building_settings`` (list): The building settings.
  - ``underlying`` (str): The underlying instrument.

Returns:
  - ``VolatilitySurface``

Example:

.. code-block:: python

    cm_vol_surface = cmanalytics.cm_vol_surface_builder(
        as_of_date="2025-03-20",
        smile_method="CUBIC_SPLINE",
        wing_strike_type="ABSOLUTE",
        lower=55.0,
        upper=95.0,
        option_quote_matrix=cm_option_matrix,
        underlying_prices=[75.0],
        discount_curve=discount_curve,
        fwd_curve=forward_curve,
        building_settings=building_settings,
        underlying="WTI"
    )

Market Data and Risk Settings
----------------------------

These functions create market data sets and risk settings for commodity pricing.

CM Risk Settings
~~~~~~~~~~~~~~

.. code-block:: python

    create_cm_risk_settings(ir_curve_settings, price_settings, vol_settings, price_vol_settings, dividend_curve_settings, theta_settings)

Create CM risk settings.

Parameters:
  - ``ir_curve_settings``: Settings for interest rate curve.
  - ``price_settings``: Settings for pricing.
  - ``vol_settings``: Settings for volatility.
  - ``price_vol_settings``: Settings for price volatility.
  - ``dividend_curve_settings``: Settings for dividend curve.
  - ``theta_settings``: Settings for theta.

Returns:
  - ``ProtoCmRiskSettings``

Example:

.. code-block:: python

    risk_settings = cmanalytics.create_cm_risk_settings(
        ir_curve_settings=ir_curve_settings,
        price_settings=price_settings,
        vol_settings=vol_settings,
        price_vol_settings=price_vol_settings,
        dividend_curve_settings=dividend_curve_settings,
        theta_settings=theta_settings
    )

CM Market Data Set
~~~~~~~~~~~~~~~~

.. code-block:: python

    create_cm_mkt_data_set(as_of_date, discount_curve, underlying_price, vol_surf, fwd_curve, quanto_discount_curve, quanto_fx_vol_curve, quanto_correlation, underlying='')

Create CM market data set.

Parameters:
  - ``as_of_date`` (datetime): The reference date.
  - ``discount_curve`` (DiscountCurve): The discount curve.
  - ``underlying_price`` (float): The underlying price.
  - ``vol_surf`` (VolatilitySurface): The volatility surface.
  - ``fwd_curve`` (ForwardCurve): The forward curve.
  - ``quanto_discount_curve`` (DiscountCurve): The quanto discount curve.
  - ``quanto_fx_vol_curve`` (VolatilityCurve): The quanto FX volatility curve.
  - ``quanto_correlation`` (float): The quanto correlation.
  - ``underlying`` (str, optional): The underlying instrument.

Returns:
  - ``ProtoCmMktDataSet``

Example:

.. code-block:: python

    mkt_data = cmanalytics.create_cm_mkt_data_set(
        as_of_date="2025-03-20",
        discount_curve=usd_curve,
        underlying_price=75.0,
        vol_surf=cm_vol_surface,
        fwd_curve=forward_curve,
        quanto_discount_curve=None,
        quanto_fx_vol_curve=None,
        quanto_correlation=0.0,
        underlying="WTI"
    )

Pricing Functions
---------------

These functions price different types of commodity options and structured products.

Standard Option Pricing
~~~~~~~~~~~~~~~~~~~~~

CM European Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_european_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM European option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    european_results = cmanalytics.cm_european_option_pricer(
        instrument=eur_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM American Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_american_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM American option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    american_results = cmanalytics.cm_american_option_pricer(
        instrument=am_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Asian Option Pricer
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_asian_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Asian option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    asian_results = cmanalytics.cm_asian_option_pricer(
        instrument=asian_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Digital Option Pricer
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_digital_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Digital option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    digital_results = cmanalytics.cm_digital_option_pricer(
        instrument=digital_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Range Accrual Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_range_accrual_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Range Accrual option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    range_accrual_results = cmanalytics.cm_range_accrual_option_pricer(
        instrument=range_accrual_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Barrier Option Pricing
~~~~~~~~~~~~~~~~~~~~

CM Single Barrier Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_single_barrier_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Single Barrier option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    single_barrier_results = cmanalytics.cm_single_barrier_option_pricer(
        instrument=single_barrier_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Double Barrier Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_double_barrier_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Double Barrier option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    double_barrier_results = cmanalytics.cm_double_barrier_option_pricer(
        instrument=double_barrier_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Touch Option Pricing
~~~~~~~~~~~~~~~~~~

CM One Touch Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_one_touch_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM One Touch option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    one_touch_results = cmanalytics.cm_one_touch_option_pricer(
        instrument=one_touch_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Double Touch Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_double_touch_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Double Touch option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    double_touch_results = cmanalytics.cm_double_touch_option_pricer(
        instrument=double_touch_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Structured Commodity Products
---------------------------

These functions price structured commodity products and notes.

CM Single Shark Fin Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_single_shark_fin_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Single Shark Fin option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    shark_fin_results = cmanalytics.cm_single_shark_fin_option_pricer(
        instrument=shark_fin_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Double Shark Fin Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_double_shark_fin_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Double Shark Fin option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    dbl_shark_fin_results = cmanalytics.cm_double_shark_fin_option_pricer(
        instrument=dbl_shark_fin_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Ping Pong Option Pricer
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_ping_pong_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Ping Pong option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    ping_pong_results = cmanalytics.cm_ping_pong_option_pricer(
        instrument=ping_pong_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Airbag Option Pricer
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_airbag_option_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Airbag option.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    airbag_results = cmanalytics.cm_airbag_option_pricer(
        instrument=airbag_option,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

Autocallable Notes
~~~~~~~~~~~~~~~~

CM Snowball Auto Callable Note Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_snowball_auto_callable_note_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Snowball Auto Callable Note.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    snowball_results = cmanalytics.cm_snowball_auto_callable_note_pricer(
        instrument=snowball_note,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )

CM Phoenix Auto Callable Note Pricer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    cm_phoenix_auto_callable_note_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a CM Phoenix Auto Callable Note.

Parameters:
  - ``instrument`` (Instrument): The option instrument.
  - ``pricing_date`` (datetime): The pricing date.
  - ``mkt_data_set`` (MarketDataSet): The market data set.
  - ``pricing_settings`` (PricingSettings): The pricing settings.
  - ``risk_settings`` (RiskSettings): The risk settings.
  - ``scn_settings`` (ScenarioSettings): The scenario settings.

Returns:
  - ``CmPricingOutput``

Example:

.. code-block:: python

    phoenix_results = cmanalytics.cm_phoenix_auto_callable_note_pricer(
        instrument=phoenix_note,
        pricing_date="2025-03-20",
        mkt_data_set=mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=risk_settings,
        scn_settings=scenario_settings
    )
