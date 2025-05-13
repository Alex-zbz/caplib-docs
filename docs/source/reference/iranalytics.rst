Interest Rate Analytics
=====================

This section covers the interest rate analytics functionality available in the caplib.iranalytics module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Market Data Setup
--------------

IR Yield Curve Build Settings
~~~~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    create_ir_curve_build_settings(curve_name, discount_curves, forward_curves, use_on_tn_fx_swap=False)

### Parameters

* **curve_name** (*str*) - Name of the curve to build
* **discount_curves** (*dict*) - Dictionary mapping discount curve names to actual curve names
* **forward_curves** (*dict*) - Dictionary mapping forward curve names to actual curve names
* **use_on_tn_fx_swap** (*bool, optional*) - Flag to use overnight/tomorrow-next FX swaps, default is False

### Returns

* IR curve build settings object

### Example

.. code-block:: python

    from caplib.iranalytics import create_ir_curve_build_settings
    
    # Define discount curves and forward curves
    discount_curves = {
        "USD_DISCOUNT": "USD_3M_DISCOUNT"
    }
    
    forward_curves = {
        "USD_3M": "USD_3M_FORWARD",
        "USD_6M": "USD_6M_FORWARD"
    }
    
    # Create curve build settings
    build_settings = create_ir_curve_build_settings(
        curve_name="USD_3M_CURVE",
        discount_curves=discount_curves,
        forward_curves=forward_curves,
        use_on_tn_fx_swap=False
    )

IR Par Rate Curve
~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    create_ir_par_rate_curve(as_of_date, currency, curve_name, inst_names, inst_types, inst_terms, factors, quotes)

### Parameters

* **as_of_date** (*datetime*) - Reference date for the curve
* **currency** (*str*) - Currency code for the curve
* **curve_name** (*str*) - Name of the par rate curve
* **inst_names** (*list*) - List of instrument names
* **inst_types** (*list*) - List of instrument types (e.g., "DEPO", "SWAP")
* **inst_terms** (*list*) - List of instrument terms (e.g., "3M", "1Y")
* **factors** (*list*) - List of scaling factors for each instrument
* **quotes** (*list*) - List of market rates for each instrument

### Returns

* IR par rate curve object

### Example

.. code-block:: python

    from datetime import datetime
    from caplib.iranalytics import create_ir_par_rate_curve
    
    # Create a par rate curve with market instruments
    as_of_date = datetime(2025, 3, 20)
    
    # Define instruments for the curve
    inst_names = ["USD_3M_DEPO", "USD_6M_SWAP", "USD_1Y_SWAP", "USD_2Y_SWAP", "USD_5Y_SWAP", "USD_10Y_SWAP"]
    inst_types = ["DEPO", "SWAP", "SWAP", "SWAP", "SWAP", "SWAP"]
    inst_terms = ["3M", "6M", "1Y", "2Y", "5Y", "10Y"]
    factors = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]  # Scaling factors
    quotes = [0.0350, 0.0360, 0.0370, 0.0380, 0.0390, 0.0400]  # Market rates
    
    # Create the par rate curve
    par_curve = create_ir_par_rate_curve(
        as_of_date=as_of_date,
        currency="USD",
        curve_name="USD_PAR_CURVE",
        inst_names=inst_names,
        inst_types=inst_types,
        inst_terms=inst_terms,
        factors=factors,
        quotes=quotes
    )

Curve Building
-----------

Single Currency Curve Building
~~~~~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    ir_single_ccy_curve_builder(as_of_date, target_curves, build_settings, par_curves, day_count, compounding_type, frequency, other_curves=None, building_method="BOOTSTRAPPING_METHOD", calc_jacobian=False)

### Parameters

* **as_of_date** (*datetime*) - Reference date for curve building
* **target_curves** (*list*) - List of curve names to build
* **build_settings** (*list*) - List of curve build settings objects
* **par_curves** (*list*) - List of par rate curve objects
* **day_count** (*str*) - Day count convention for the curves
* **compounding_type** (*str*) - Compounding type (e.g., "CONTINUOUS_COMPOUNDING")
* **frequency** (*str*) - Frequency for compounding (e.g., "ANNUAL")
* **other_curves** (*list, optional*) - List of other curves to use
* **building_method** (*str, optional*) - Method for building curves, default is "BOOTSTRAPPING_METHOD"
* **calc_jacobian** (*bool, optional*) - Whether to calculate Jacobian, default is False

### Returns

* List of built yield curve objects

### Example

.. code-block:: python

    from caplib.iranalytics import ir_single_ccy_curve_builder
    
    # Build a single currency yield curve
    target_curves = ["USD_3M_CURVE"]
    build_settings_list = [build_settings]  # From previous example
    par_curves_list = [par_curve]  # From previous example
    
    # Additional curves to be used in the curve building process
    other_curves = []
    
    # Build the yield curve
    yield_curves = ir_single_ccy_curve_builder(
        as_of_date=as_of_date,
        target_curves=target_curves,
        build_settings=build_settings_list,
        par_curves=par_curves_list,
        day_count="ACT_365_FIXED",
        compounding_type="CONTINUOUS_COMPOUNDING",
        frequency="ANNUAL",
        other_curves=other_curves,
        building_method="BOOTSTRAPPING_METHOD",
        calc_jacobian=False
    )
    
    # The result contains the built USD_3M_CURVE
    usd_3m_curve = yield_curves[0]

Cross-Currency Curve Building
~~~~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    ir_cross_ccy_curve_builder(as_of_date, target_curves, build_settings, par_curves, day_count, compounding_type, frequency, other_curves, fx_spot)

### Parameters

* **as_of_date** (*datetime*) - Reference date for curve building
* **target_curves** (*list*) - List of curve names to build
* **build_settings** (*list*) - List of curve build settings objects
* **par_curves** (*list*) - List of par rate curve objects
* **day_count** (*str*) - Day count convention for the curves
* **compounding_type** (*str*) - Compounding type (e.g., "CONTINUOUS_COMPOUNDING")
* **frequency** (*str*) - Frequency for compounding (e.g., "ANNUAL")
* **other_curves** (*list*) - List of other curves to use in building
* **fx_spot** (*float*) - FX spot rate for cross-currency calculations

### Returns

* List of built cross-currency yield curve objects

### Example

.. code-block:: python

    from caplib.iranalytics import ir_cross_ccy_curve_builder
    
    # Define FX spot rate
    fx_spot = 1.1000  # EUR/USD
    
    # Build a EUR discount curve using USD curve and FX swaps
    target_curves = ["EUR_DISCOUNT"]
    
    # Set up appropriate build settings and par curves
    eur_build_settings = create_ir_curve_build_settings(
        curve_name="EUR_DISCOUNT",
        discount_curves={"USD_DISCOUNT": "USD_3M_DISCOUNT"},
        forward_curves={}
    )
    
    # Create par curve with EUR/USD FX swap points
    eur_par_curve = create_ir_par_rate_curve(
        as_of_date=as_of_date,
        currency="EUR",
        curve_name="EUR_PAR_CURVE",
        inst_names=["EUR_USD_1M", "EUR_USD_3M", "EUR_USD_6M", "EUR_USD_1Y"],
        inst_types=["XCCY_BASIS_SWAP", "XCCY_BASIS_SWAP", "XCCY_BASIS_SWAP", "XCCY_BASIS_SWAP"],
        inst_terms=["1M", "3M", "6M", "1Y"],
        factors=[1.0, 1.0, 1.0, 1.0],
        quotes=[-0.0010, -0.0015, -0.0020, -0.0025]  # Basis spreads
    )
    
    # Build the cross-currency curve
    xccy_curves = ir_cross_ccy_curve_builder(
        as_of_date=as_of_date,
        target_curves=["EUR_DISCOUNT"],
        build_settings=[eur_build_settings],
        par_curves=[eur_par_curve],
        day_count="ACT_365_FIXED",
        compounding_type="CONTINUOUS_COMPOUNDING",
        frequency="ANNUAL",
        other_curves=[usd_3m_curve],  # Use USD curve from previous example
        fx_spot=fx_spot
    )
    
    # The result contains the built EUR_DISCOUNT curve
    eur_discount_curve = xccy_curves[0]

Market Data Sets and Risk Settings
------------------------------

IR Market Data Sets
~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    create_ir_mkt_data_set(as_of_date, discount_curve, underlyings, forward_curves)

### Parameters

* **as_of_date** (*datetime*) - Reference date for the market data set
* **discount_curve** (*object*) - Discount curve for present value calculations
* **underlyings** (*list*) - List of underlying interest rate indices
* **forward_curves** (*list*) - List of forward curves for pricing

### Returns

* IR market data set object

### Example

.. code-block:: python

    from caplib.iranalytics import create_ir_mkt_data_set
    
    # Create a market data set with discount and forward curves
    underlyings = []  # List of underlying indices
    forward_curves = [usd_3m_curve]  # Forward curves for pricing
    
    ir_mkt_data = create_ir_mkt_data_set(
        as_of_date=as_of_date,
        discount_curve=usd_3m_curve,
        underlyings=underlyings,
        forward_curves=forward_curves
    )

Cross-Currency Market Data Sets
~~~~~~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    create_cross_ccy_mkt_data_set(as_of_date, base_discount_curve, xccy_discount_curve, underlying_interest_rates, underlying_forward_curves, fx_spot_rate)

### Parameters

* **as_of_date** (*datetime*) - Reference date for the market data set
* **base_discount_curve** (*object*) - Base currency discount curve
* **xccy_discount_curve** (*object*) - Foreign currency discount curve
* **underlying_interest_rates** (*list*) - List of underlying interest rate indices
* **underlying_forward_curves** (*list*) - List of forward curves for pricing
* **fx_spot_rate** (*float*) - FX spot rate for cross-currency calculations

### Returns

* Cross-currency market data set object

### Example

.. code-block:: python

    from caplib.iranalytics import create_cross_ccy_mkt_data_set
    
    # Create a cross-currency market data set
    xccy_mkt_data = create_cross_ccy_mkt_data_set(
        as_of_date=as_of_date,
        base_discount_curve=usd_3m_curve,  # Base currency (USD) discount curve
        xccy_discount_curve=eur_discount_curve,  # Foreign currency (EUR) discount curve
        underlying_interest_rates=[],
        underlying_forward_curves=[usd_3m_curve],
        fx_spot_rate=1.1000  # EUR/USD spot rate
    )

Interest Rate Instrument Pricing
----------------------------

Vanilla IR Instrument Pricing
~~~~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    ir_vanilla_instrument_pricer(instrument, pricing_date, mkt_data, pricing_settings, risk_settings)

### Parameters

* **instrument** (*object*) - Interest rate instrument to price
* **pricing_date** (*datetime*) - Pricing date for the instrument
* **mkt_data** (*object*) - Market data set for pricing
* **pricing_settings** (*object*) - Pricing settings for the instrument
* **risk_settings** (*object*) - Risk settings for the instrument

### Returns

* Pricing result object

### Example

.. code-block:: python

    from caplib.analytics import create_pricing_settings
    from caplib.iranalytics import ir_vanilla_instrument_pricer
    from caplib.irmarket import build_ir_vanilla_instrument
    
    # Create pricing settings
    pricing_settings = create_pricing_settings(
        calc_pv=True,
        calc_delta=True,
        calc_gamma=False,
        calc_vega=False,
        calc_theta=True
    )
    
    # Assuming we have a vanilla swap instrument
    # This would typically be created with build_ir_vanilla_instrument
    from caplib.irmarket import build_depo
    
    # Create a simple deposit instrument
    depo = build_depo(
        pay_rec="RECEIVE",  # Receive fixed
        rate=0.035,  # 3.5%
        start_date=as_of_date,
        maturity="3M",
        inst_template=depo_template,  # This would be created with create_depo_template
        nominal=1000000.0  # 1 million notional
    )
    
    # Price the instrument
    pricing_result = ir_vanilla_instrument_pricer(
        instrument=depo,
        pricing_date=as_of_date,
        mkt_data=ir_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=ir_risk_settings
    )
    
    # Access the pricing results
    pv = pricing_result.present_value
    delta = pricing_result.delta
    theta = pricing_result.theta

Cross-Currency Swap Pricing
~~~~~~~~~~~~~~~~~~~~

### Function Signature

.. code-block:: python

    cross_currency_swap_pricer(instrument, pricing_date, mkt_data, pricing_settings, risk_settings)

### Parameters

* **instrument** (*object*) - Cross-currency swap instrument to price
* **pricing_date** (*datetime*) - Pricing date for the instrument
* **mkt_data** (*object*) - Market data set for pricing
* **pricing_settings** (*object*) - Pricing settings for the instrument
* **risk_settings** (*object*) - Risk settings for the instrument

### Returns

* Pricing result object

### Example

.. code-block:: python

    from caplib.iranalytics import cross_currency_swap_pricer
    
    # Assuming we have a cross-currency swap instrument
    # This would be created with appropriate build functions
    
    # Price the cross-currency swap
    xccy_pricing_result = cross_currency_swap_pricer(
        instrument=xccy_swap,  # Cross currency swap instrument
        pricing_date=as_of_date,
        mkt_data=xccy_mkt_data,  # Cross currency market data set
        pricing_settings=pricing_settings,
        risk_settings=xccy_risk_settings
    )
    
    # Access the pricing results
    xccy_pv = xccy_pricing_result.present_value
    xccy_delta = xccy_pricing_result.delta
    xccy_theta = xccy_pricing_result.theta

Complete Workflow Example
--------------------

Here's a complete workflow that demonstrates curve building and instrument pricing:

.. code-block:: python

    from datetime import datetime
    from caplib.datetime import create_date
    from caplib.analytics import create_pricing_settings, create_ir_curve_risk_settings, create_theta_risk_settings
    from caplib.iranalytics import (
        create_ir_curve_build_settings, 
        create_ir_par_rate_curve, 
        ir_single_ccy_curve_builder, 
        create_ir_mkt_data_set,
        create_ir_risk_settings,
        ir_vanilla_instrument_pricer
    )
    from caplib.irmarket import create_depo_template, build_depo
    
    # Set up date
    as_of_date = datetime(2025, 3, 20)
    
    # Step 1: Create par rate curve
    inst_names = ["USD_3M_DEPO", "USD_6M_SWAP", "USD_1Y_SWAP", "USD_2Y_SWAP", "USD_5Y_SWAP", "USD_10Y_SWAP"]
    inst_types = ["DEPO", "SWAP", "SWAP", "SWAP", "SWAP", "SWAP"]
    inst_terms = ["3M", "6M", "1Y", "2Y", "5Y", "10Y"]
    factors = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
    quotes = [0.0350, 0.0360, 0.0370, 0.0380, 0.0390, 0.0400]
    
    par_curve = create_ir_par_rate_curve(
        as_of_date=as_of_date,
        currency="USD",
        curve_name="USD_PAR_CURVE",
        inst_names=inst_names,
        inst_types=inst_types,
        inst_terms=inst_terms,
        factors=factors,
        quotes=quotes
    )
    
    # Step 2: Create build settings
    discount_curves = {"USD_DISCOUNT": "USD_3M_DISCOUNT"}
    forward_curves = {"USD_3M": "USD_3M_FORWARD"}
    
    build_settings = create_ir_curve_build_settings(
        curve_name="USD_3M_CURVE",
        discount_curves=discount_curves,
        forward_curves=forward_curves
    )
    
    # Step 3: Build yield curve
    yield_curves = ir_single_ccy_curve_builder(
        as_of_date=as_of_date,
        target_curves=["USD_3M_CURVE"],
        build_settings=[build_settings],
        par_curves=[par_curve],
        day_count="ACT_365_FIXED",
        compounding_type="CONTINUOUS_COMPOUNDING",
        frequency="ANNUAL",
        other_curves=[],
        building_method="BOOTSTRAPPING_METHOD"
    )
    
    usd_curve = yield_curves[0]
    
    # Step 4: Create market data set
    ir_mkt_data = create_ir_mkt_data_set(
        as_of_date=as_of_date,
        discount_curve=usd_curve,
        underlyings=[],
        forward_curves=[usd_curve]
    )
    
    # Step 5: Create deposit template
    depo_template = create_depo_template(
        inst_name="USD_DEPO",
        currency="USD",
        calendar="US",
        start_delay=2,
        day_count="ACT_360"
    )
    
    # Step 6: Create deposit instrument
    depo = build_depo(
        pay_rec="RECEIVE",
        rate=0.035,
        start_date=as_of_date,
        maturity="3M",
        inst_template=depo_template,
        nominal=1000000.0
    )
    
    # Step 7: Create risk settings
    ir_curve_settings = create_ir_curve_risk_settings(
        bump_size=0.0001,
        bump_type="ABSOLUTE_BUMP"
    )
    
    theta_settings = create_theta_risk_settings(
        bump_days=1
    )
    
    ir_risk_settings = create_ir_risk_settings(
        ir_curve_settings=ir_curve_settings,
        theta_settings=theta_settings
    )
    
    # Step 8: Create pricing settings
    pricing_settings = create_pricing_settings(
        calc_pv=True,
        calc_delta=True,
        calc_gamma=False,
        calc_vega=False,
        calc_theta=True
    )
    
    # Step 9: Price the deposit
    pricing_result = ir_vanilla_instrument_pricer(
        instrument=depo,
        pricing_date=as_of_date,
        mkt_data=ir_mkt_data,
        pricing_settings=pricing_settings,
        risk_settings=ir_risk_settings
    )
    
    # Step 10: Access results
    print(f"Present Value: {pricing_result.present_value}")
    print(f"Delta: {pricing_result.delta}")
    print(f"Theta: {pricing_result.theta}")
