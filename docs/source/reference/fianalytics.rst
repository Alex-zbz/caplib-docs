Fixed Income Analytics
=====================

The fixed income analytics module provides functions for building bond curves, pricing fixed income instruments, and calculating risk metrics for fixed income portfolios.

Enumeration Conversions
-------------------

These functions convert string representations to their corresponding enumeration types in the protocol buffer definitions.

Bond Quote Type
~~~~~~~~~~~~~~~

.. code-block:: python

    to_bond_quote_type(src)

Convert a string to ``BondQuoteType``.

Parameters:
  - ``src`` (str): String representing the bond quote type, e.g., 'YIELD_TO_MATURITY', 'PRICE', 'SPREAD_TO_BENCHMARK'.

Returns:
  - ``BondQuoteType``

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    quote_type = fianalytics.to_bond_quote_type("YIELD_TO_MATURITY")

Curve Construction
--------------

Bond Curve Build Settings
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_bond_curve_build_settings(curve_name, curve_type, interp_method, extrap_method)

Create settings for building bond yield curves.

Parameters:
  - ``curve_name`` (str): Name of the curve to build.
  - ``curve_type`` (str): Type of the curve, e.g., 'DISCOUNT_CURVE'.
  - ``interp_method`` (str): Interpolation method, e.g., 'LINEAR_ON_ZERO'.
  - ``extrap_method`` (str): Extrapolation method, e.g., 'FLAT_FORWARDS'.

Returns:
  - Bond curve build settings object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    bond_curve_settings = fianalytics.create_bond_curve_build_settings(
        curve_name="USD_GOVT_CURVE",
        curve_type="DISCOUNT_CURVE",
        interp_method="LINEAR_ON_ZERO",
        extrap_method="FLAT_FORWARDS"
    )

Bond Par Curve
~~~~~~~~~

.. code-block:: python

    create_bond_par_curve(as_of_date, currency, inst_names, quotes, quote_type, curve_name)

Create a market data curve from bond instruments.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the curve.
  - ``currency`` (str): Currency code for the curve.
  - ``inst_names`` (list): List of instrument names used in the curve.
  - ``quotes`` (list): List of quotes corresponding to the instruments.
  - ``quote_type`` (str): Type of quotes, e.g., 'YIELD_TO_MATURITY', 'PRICE'.
  - ``curve_name`` (str): Name of the curve.

Returns:
  - Bond par curve object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    from datetime import datetime
    
    as_of_date = datetime(2025, 3, 20)
    
    # Define bond instruments and quotes
    inst_names = ["US_TBILL_3M", "US_TNOTE_2Y", "US_TNOTE_5Y", "US_TNOTE_10Y", "US_TBOND_30Y"]
    quotes = [0.0340, 0.0360, 0.0375, 0.0390, 0.0410]  # Yield quotes
    
    bond_par_curve = fianalytics.create_bond_par_curve(
        as_of_date=as_of_date,
        currency="USD",
        inst_names=inst_names,
        quotes=quotes,
        quote_type="YIELD_TO_MATURITY",
        curve_name="USD_TREASURY_CURVE"
    )

Bond Yield Curve Building
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    build_bond_yield_curve(build_settings, curve_name, as_of_date, par_curve, day_count, compounding_type, freq, build_method, calc_jacobian)

Build a yield curve from bond par rates.

Parameters:
  - ``build_settings`` (object): Bond curve build settings.
  - ``curve_name`` (str): Name for the curve.
  - ``as_of_date`` (datetime): Reference date for the curve.
  - ``par_curve`` (object): Bond par curve.
  - ``day_count`` (str): Day count convention, e.g., 'ACT_365_FIXED'.
  - ``compounding_type`` (str): Compounding type, e.g., 'CONTINUOUS_COMPOUNDING'.
  - ``freq`` (str): Compounding frequency, e.g., 'ANNUAL'.
  - ``build_method`` (str): Method for building curve, e.g., 'BOOTSTRAPPING_METHOD'.
  - ``calc_jacobian`` (bool): Whether to calculate Jacobian matrix.

Returns:
  - Bond yield curve object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    bond_yield_curve = fianalytics.build_bond_yield_curve(
        build_settings=bond_curve_settings,
        curve_name="USD_GOVT_CURVE",
        as_of_date=as_of_date,
        par_curve=bond_par_curve,
        day_count="ACT_365_FIXED",
        compounding_type="CONTINUOUS_COMPOUNDING",
        freq="ANNUAL",
        build_method="BOOTSTRAPPING_METHOD",
        calc_jacobian=False
    )

Bond Credit Spread Curve Building
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    build_bond_sprd_curve(build_settings, curve_name, as_of_date, par_curve, discount_curve, build_method, calc_jacobian)

Build a credit spread curve using bond yields and a risk-free discount curve.

Parameters:
  - ``build_settings`` (object): Bond curve build settings.
  - ``curve_name`` (str): Name for the curve.
  - ``as_of_date`` (datetime): Reference date for the curve.
  - ``par_curve`` (object): Bond par curve with credit-risky bonds.
  - ``discount_curve`` (object): Risk-free discount curve.
  - ``build_method`` (str): Method for building curve, e.g., 'BOOTSTRAPPING_METHOD'.
  - ``calc_jacobian`` (bool): Whether to calculate Jacobian matrix.

Returns:
  - Credit spread curve object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    import caplib.iranalytics as iranalytics
    
    # Assuming we have a risk-free discount curve (ois_curve) from IR analytics
    
    credit_spread_curve = fianalytics.build_bond_sprd_curve(
        build_settings=bond_curve_settings,
        curve_name="USD_CORP_SPREAD_CURVE",
        as_of_date=as_of_date,
        par_curve=bond_par_curve,
        discount_curve=ois_curve,
        build_method="BOOTSTRAPPING_METHOD",
        calc_jacobian=False
    )

Market Data Sets and Risk Settings
------------------------------

Fixed Income Market Data Set
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fi_mkt_data_set(as_of_date, discount_curve, credit_sprd_curve, forward_curve, underlying_discount_curve, underlying_income_curve)

Create a market data set for fixed income instruments.

Parameters:
  - ``as_of_date`` (datetime): Reference date for the market data.
  - ``discount_curve`` (object): Discount curve for the instrument's currency.
  - ``credit_sprd_curve`` (object, optional): Credit spread curve for bond issuers.
  - ``forward_curve`` (object, optional): Forward curve for floating rate bonds.
  - ``underlying_discount_curve`` (object, optional): Discount curve for cross-currency bonds.
  - ``underlying_income_curve`` (object, optional): Income curve for dividend-paying assets.

Returns:
  - Fixed income market data set object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    fi_mkt_data = fianalytics.create_fi_mkt_data_set(
        as_of_date=as_of_date,
        discount_curve=ois_curve,
        credit_sprd_curve=credit_spread_curve,
        forward_curve=bond_yield_curve,
        underlying_discount_curve=None,
        underlying_income_curve=None
    )

Fixed Income Risk Settings
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_fi_risk_settings(ir_curve_settings, credit_curve_settings, xtras_curve_settings, theta_settings, price_settings)

Create settings for calculating sensitivities of fixed income instruments.

Parameters:
  - ``ir_curve_settings`` (object): Settings for interest rate curve risk.
  - ``credit_curve_settings`` (object): Settings for credit spread curve risk.
  - ``xtras_curve_settings`` (object, optional): Settings for cross-asset curve risk.
  - ``theta_settings`` (object): Settings for theta risk.
  - ``price_settings`` (object, optional): Settings for price risk.

Returns:
  - Fixed income risk settings object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    import caplib.analytics as analytics
    
    # Create interest rate curve risk settings
    ir_curve_settings = analytics.create_ir_curve_risk_settings(
        bump_size=0.0001,  # 1 basis point
        bump_type="ABSOLUTE_BUMP"
    )
    
    # Create credit spread curve risk settings
    cs_curve_settings = analytics.create_credit_curve_risk_settings(
        bump_size=0.0001,  # 1 basis point
        bump_type="ABSOLUTE_BUMP"
    )
    
    # Create theta risk settings
    theta_settings = analytics.create_theta_risk_settings(
        bump_days=1  # 1 day forward for theta
    )
    
    # Combine into fixed income risk settings
    fi_risk_settings = fianalytics.create_fi_risk_settings(
        ir_curve_settings=ir_curve_settings,
        credit_curve_settings=cs_curve_settings,
        xtras_curve_settings=None,
        theta_settings=theta_settings,
        price_settings=None
    )

Bond Pricing
--------

Zero Coupon Bond Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    zero_coupon_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a zero coupon bond.

Parameters:
  - ``instrument`` (object): The zero coupon bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Zero coupon bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    import caplib.analytics as analytics
    
    # Create pricing settings
    pricing_settings = analytics.create_pricing_settings(
        pricing_currency="USD",
        inc_current=True,
        model_settings=None,
        method_name="ANALYTICAL",
        pricing_date=as_of_date,
        calc_base_npv=True,
        calc_sensitivities=True,
        num_threads=1,
        thread_mode="MULTI_THREADING_MODE"
    )
    
    # Create scenario settings (for base case only)
    scn_settings = analytics.create_base_scenario_settings()
    
    # Price the zero coupon bond
    zcb_results = fianalytics.zero_coupon_bond_pricer(
        instrument=zero_coupon_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )

Fixed Rate Bond Pricer
~~~~~~~~~~~~~~~~~

.. code-block:: python

    fixed_rate_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a fixed rate bond.

Parameters:
  - ``instrument`` (object): The fixed rate bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Fixed rate bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    # Price the fixed rate bond
    fixed_rate_results = fianalytics.fixed_rate_bond_pricer(
        instrument=fixed_rate_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )

Floating Rate Bond Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    floating_rate_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a floating rate bond.

Parameters:
  - ``instrument`` (object): The floating rate bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Floating rate bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    # Price the floating rate bond
    floating_rate_results = fianalytics.floating_rate_bond_pricer(
        instrument=floating_rate_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )

Structured Bonds
------------

Callable Bond Pricer
~~~~~~~~~~~~~~~~

.. code-block:: python

    callable_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a callable bond.

Parameters:
  - ``instrument`` (object): The callable bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Callable bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    # Price the callable bond
    callable_results = fianalytics.callable_bond_pricer(
        instrument=callable_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )

Putable Bond Pricer
~~~~~~~~~~~~~~~

.. code-block:: python

    putable_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a putable bond.

Parameters:
  - ``instrument`` (object): The putable bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Putable bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    # Price the putable bond
    putable_results = fianalytics.putable_bond_pricer(
        instrument=putable_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )

Convertible Bond Pricer
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    convertible_bond_pricer(instrument, pricing_date, mkt_data_set, pricing_settings, risk_settings, scn_settings)

Price a convertible bond.

Parameters:
  - ``instrument`` (object): The convertible bond instrument.
  - ``pricing_date`` (datetime): Date for the pricing calculation.
  - ``mkt_data_set`` (object): Market data set for the pricing.
  - ``pricing_settings`` (object): Settings for the pricing.
  - ``risk_settings`` (object): Risk settings for the calculation.
  - ``scn_settings`` (object): Scenario settings for the calculation.

Returns:
  - Convertible bond pricing result object

Example:

.. code-block:: python

    import caplib.fianalytics as fianalytics
    
    # Price the convertible bond
    convertible_results = fianalytics.convertible_bond_pricer(
        instrument=convertible_bond,
        pricing_date=as_of_date,
        mkt_data_set=fi_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=fi_risk_settings,
        scn_settings=scn_settings
    )
