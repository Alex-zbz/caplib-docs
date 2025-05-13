Analytics
=========

The analytics module provides various conversion functions for financial analytics data types and methods to create parameter settings for different financial models and pricing techniques.

Type Conversion Functions
------------------------

These functions convert string representations to their corresponding enumeration types in the protocol buffer definitions.

Compounding Type
~~~~~~~~~~~~~~~

.. code-block:: python

    to_compounding_type(src)

Convert a string to ``CompoundingType``.

Parameters:
  - ``src`` (str): String representing the compounding type, e.g., 'CONTINUOUS_COMPOUNDING'.

Returns:
  - ``CompoundingType``

Example:

.. code-block:: python

    import caplib.analytics as analytics
    
    compounding_type = analytics.to_compounding_type('CONTINUOUS_COMPOUNDING')

Pricing Model Name
~~~~~~~~~~~~~~~~~

.. code-block:: python

    to_pricing_model_name(src)

Convert a string to ``PricingModelName``.

Parameters:
  - ``src`` (str): String representing the pricing model, e.g., 'BLACK_SCHOLES_MERTON'.

Returns:
  - ``PricingModelName``

Example:

.. code-block:: python

    model_name = analytics.to_pricing_model_name('BLACK_SCHOLES_MERTON')

Pricing Method Name
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    to_pricing_method_name(src)

Convert a string to ``PricingMethodName``.

Parameters:
  - ``src`` (str): String representing the pricing method, e.g., 'ANALYTICAL'.

Returns:
  - ``PricingMethodName``

Example:

.. code-block:: python

    method_name = analytics.to_pricing_method_name('ANALYTICAL')

Finite Difference Method
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    to_finite_difference_method(src)

Convert a string to ``FiniteDifferenceMethod``.

Parameters:
  - ``src`` (str): String representing the finite difference method, e.g., 'CENTRAL_DIFFERENCE_METHOD'.

Returns:
  - ``FiniteDifferenceMethod``

Example:

.. code-block:: python

    fd_method = analytics.to_finite_difference_method('CENTRAL_DIFFERENCE_METHOD')

Threading Mode
~~~~~~~~~~~~~

.. code-block:: python

    to_threading_mode(src)

Convert a string to ``ThreadingMode``.

Parameters:
  - ``src`` (str): String representing the threading mode, e.g., 'SINGLE_THREADING_MODE'.

Returns:
  - ``ThreadingMode``

Example:

.. code-block:: python

    mode = analytics.to_threading_mode('SINGLE_THREADING_MODE')

Risk Granularity
~~~~~~~~~~~~~~~

.. code-block:: python

    to_risk_granularity(src)

Convert a string to ``RiskGranularity``.

Parameters:
  - ``src`` (str): String representing the risk granularity, e.g., 'TOTAL_RISK'.

Returns:
  - ``RiskGranularity``

Example:

.. code-block:: python

    granularity = analytics.to_risk_granularity('TOTAL_RISK')

IR Yield Curve Building Method
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    to_ir_yield_curve_building_method(src)

Convert a string to ``IrYieldCurveBuildingMethod``.

Parameters:
  - ``src`` (str): String representing the yield curve building method, e.g., 'BOOTSTRAPPING_METHOD'.

Returns:
  - ``IrYieldCurveBuildingMethod``

Example:

.. code-block:: python

    building_method = analytics.to_ir_yield_curve_building_method('BOOTSTRAPPING_METHOD')

IR Yield Curve Type
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    to_ir_yield_curve_type(src)

Convert a string to ``IrYieldCurveType``.

Parameters:
  - ``src`` (str): String representing the yield curve type, e.g., 'ZERO_RATE'.

Returns:
  - ``IrYieldCurveType``

Example:

.. code-block:: python

    curve_type = analytics.to_ir_yield_curve_type('ZERO_RATE')

Volatility Type Conversions
~~~~~~~~~~~~~~~~~~~~~~~~~~

The analytics module provides various conversion functions for volatility-related types:

- ``to_option_quote_value_type``: Convert to ``OptionQuoteValueType``
- ``to_option_quote_term_type``: Convert to ``OptionQuoteTermType``
- ``to_option_quote_strike_type``: Convert to ``OptionQuoteStrikeType``
- ``to_option_underlying_type``: Convert to ``OptionUnderlyingType``
- ``to_smile_quote_type``: Convert to ``SmileQuoteType``
- ``to_vol_smile_type``: Convert to ``VolSmileType``
- ``to_vol_smile_method``: Convert to ``VolSmileMethod``
- ``to_vol_term_time_interp_method``: Convert to ``VolTermInterpMethod``
- ``to_vol_termtime_extrap_method``: Convert to ``VolTermExtrapMethod``
- ``to_volatility_type``: Convert to ``VolatilityType``
- ``to_wing_strike_type``: Convert to ``WingStrikeType``
- ``to_atm_type``: Convert to ``AtmType``
- ``to_delta_type``: Convert to ``DeltaType``

Model Settings
-------------

Creating Pricing Model Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_model_settings(model_name, constant_params=[0.0], 
                          time_homogeneous_model_params=[], 
                          underlying='', model_calibrated=False)

Create a parameter settings object for a pricing model.

Parameters:
  - ``model_name`` (str): Name of the model. Check supported models in 'PricingModelName'.
  - ``constant_params`` (list, optional): Non-time-dependent model parameters, such as Displacement in Displaced Black model.
  - ``time_homogeneous_model_params`` (list, optional): Term structure model parameters, such as volatility P parameter in Hull-White interest rate model.
  - ``underlying`` (str, optional): Name of the underlying asset, e.g., 'USDCNY' currency pair or CSI 300 index.
  - ``model_calibrated`` (bool, optional): Flag indicating whether the model parameters have been calibrated. Default is False.

Returns:
  - ``PricingModelSettings``: Parameter settings object for the pricing model.

Example:

.. code-block:: python

    # Create settings for Black-Scholes model with volatility of 0.2
    bs_settings = analytics.create_model_settings('BLACK_SCHOLES_MERTON', constant_params=[0.2])

PDE Settings
-----------

Creating PDE Settings
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pde_settings(t_size=50, 
                        x_size=100, x_min=-4.0, x_max=4.0, x_min_max_type='MMT_NUM_STDEVS',
                        x_density=1.0, x_grid_type='UNIFORM_GRID', x_interp_method='LINEAR_INTERP',
                        y_size=3, y_min=-4.0, y_max=4.0, y_min_max_type='MMT_NUM_STDEVS',
                        y_density=1.0, y_grid_type='UNIFORM_GRID', y_interp_method='LINEAR_INTERP',
                        z_size=3, z_min=-4.0, z_max=4.0, z_min_max_type='MMT_NUM_STDEVS',
                        z_density=1.0, z_grid_type='UNIFORM_GRID', z_interp_method='LINEAR_INTERP')

Create a parameter settings object for PDE numerical methods.

Parameters:
  - ``t_size`` (int, optional): Size of the time grid. Default is 50.
  - ``x_size`` (int, optional): Size of the first dimension spatial grid. Default is 100.
  - ``x_min`` (float, optional): Lower boundary of first dimension spatial grid. Can be absolute value or number of standard deviations. Default is -4.0.
  - ``x_max`` (float, optional): Upper boundary of first dimension spatial grid. Can be absolute value or number of standard deviations. Default is 4.0.
  - ``x_min_max_type`` (str, optional): Boundary value type for first dimension. Default is 'MMT_NUM_STDEVS'.
  - ``x_density`` (float, optional): Density parameter for first dimension when the grid is non-uniform. Default is 1.0.
  - ``x_grid_type`` (str, optional): Type of first dimension spatial grid. Default is 'UNIFORM_GRID'.
  - ``x_interp_method`` (str, optional): Interpolation method for first dimension. Default is 'LINEAR_INTERP'.
  
  *Additional parameters for second (y) and third (z) dimensions follow the same pattern.*

Returns:
  - ``PdeSettings``: Parameter settings object for PDE numerical methods.

Example:

.. code-block:: python

    # Create standard PDE settings with 200 points in x-dimension
    pde_settings = analytics.create_pde_settings(x_size=200)

Monte Carlo Settings
------------------

Creating Monte Carlo Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_monte_carlo_settings(num_simulations=1024,
                                uniform_number_type='SOBOL_NUMBER',
                                seed=1024,
                                wiener_process_build_method='BROWNIAN_BRIDGE_METHOD',
                                gaussian_number_method='INVERSE_CUMULATIVE_METHOD',
                                use_antithetic=False,
                                num_steps=1)

Create a parameter settings object for Monte Carlo simulation.

Parameters:
  - ``num_simulations`` (int, optional): Number of Monte Carlo simulations. Default is 1024.
  - ``uniform_number_type`` (str, optional): Type of uniform random number. Default is 'SOBOL_NUMBER'.
  - ``seed`` (int, optional): Seed value for generating uniform random numbers. Default is 1024.
  - ``wiener_process_build_method`` (str, optional): Method for building Brownian motion process. Default is 'BROWNIAN_BRIDGE_METHOD'.
  - ``gaussian_number_method`` (str, optional): Method for generating normal distribution random numbers from uniform distribution. Default is 'INVERSE_CUMULATIVE_METHOD'.
  - ``use_antithetic`` (bool, optional): Flag to enable Antithetic variance reduction method. Default is False.
  - ``num_steps`` (int, optional): Number of additional steps required for each time interval when creating Brownian motion process. Default is 1.

Returns:
  - ``MonteCarloSettings``: Parameter settings object for Monte Carlo simulation.

Example:

.. code-block:: python

    # Create Monte Carlo settings with 10,000 simulations and antithetic variance reduction
    mc_settings = analytics.create_monte_carlo_settings(num_simulations=10000, use_antithetic=True)

Pricing Settings
--------------

Creating Pricing Settings
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_pricing_settings(pricing_currency,
                            inc_current,
                            model_settings,
                            pricing_method,
                            pde_settings,
                            mc_settings,
                            specific_pricing_requests=[],
                            cash_flows=False)

Create parameter settings for product pricing, including model parameters, pricing method, PDE numerical method parameters, Monte Carlo parameters, and user-specified metrics.

Parameters:
  - ``pricing_currency`` (str): Currency specified for instrument pricing.
  - ``inc_current`` (bool): Flag to include current cash flow in the present value of the product.
  - ``model_settings`` (PricingModelSettings): Pricing model parameter settings.
  - ``pricing_method`` (str): Pricing method, such as analytical solution or other numerical methods.
  - ``pde_settings`` (PdeSettings): PDE numerical method parameters, if pricing method is PDE.
  - ``mc_settings`` (MonteCarloSettings): Monte Carlo simulation parameters, if pricing method is Monte Carlo.
  - ``specific_pricing_requests`` (list, optional): Product-specific calculation metrics, such as yield to maturity, dirty price, clean price for bonds. Default is empty.
  - ``cash_flows`` (bool, optional): Flag for cash flow calculation. Default is False.

Returns:
  - ``PricingSettings``: Parameter settings for product pricing.

Creating Model-Free Pricing Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_model_free_pricing_settings(pricing_currency='',
                                       inc_current=True,
                                       specific_pricing_requests=[],
                                       cash_flows=False)

Create parameter settings for model-free product pricing.

Parameters:
  - ``pricing_currency`` (str, optional): Currency specified for instrument pricing.
  - ``inc_current`` (bool, optional): Flag to include current cash flow in the present value of the product. Default is True.
  - ``specific_pricing_requests`` (list, optional): Product-specific calculation metrics. Default is empty.
  - ``cash_flows`` (bool, optional): Flag for cash flow calculation. Default is False.

Returns:
  - ``PricingSettings``: Parameter settings for product pricing.

Example:

.. code-block:: python

    # Create a model-free pricing setting in USD currency
    pricing_settings = analytics.create_model_free_pricing_settings(pricing_currency='USD')

Risk Settings
-----------

Creating IR Curve Risk Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    create_ir_curve_risk_settings(delta=False,
                                  gamma=False,
                                  curvature=False,
                                  shift=1.0e-4,
                                  curvature_shift=5.0e-3,
                                  method='CENTRAL_DIFFERENCE_METHOD',
                                  granularity='TOTAL_RISK',
                                  scaling_factor=1.0e-4,
                                  threading_mode='SINGLE_THREADING_MODE')

Create risk parameter settings for calculating interest rate yield curve sensitivities.

Parameters:
  - ``delta`` (bool, optional): Flag to calculate curve Delta (DV01). Default is False.
  - ``gamma`` (bool, optional): Flag to calculate curve Gamma. Default is False.
  - ``curvature`` (bool, optional): Flag to calculate curve Curvature according to FRTB definition. Default is False.
  - ``shift`` (float, optional): Perturbation size for calculating curve Delta and Gamma. Default is 1 basis point (1.0e-4).
  - ``curvature_shift`` (float, optional): Perturbation size for calculating curve Curvature. Default is 50 basis points (5.0e-3).
  - ``method`` (str, optional): Finite difference method for calculating curve Delta. Default is 'CENTRAL_DIFFERENCE_METHOD'.
  - ``granularity`` (str, optional): Granularity for calculating curve Delta and Gamma. Default is 'TOTAL_RISK'.
  - ``scaling_factor`` (float, optional): Factor for converting percentage sensitivity to actual absolute price change. Default is 1 basis point (1.0e-4).
  - ``threading_mode`` (str, optional): Threading mode for sensitivity calculation, can be single-threaded or multi-threaded. Default is 'SINGLE_THREADING_MODE'.

Returns:
  - ``IrCurveRiskSettings``: Risk parameter settings for calculating interest rate yield curve sensitivities.

Example:

.. code-block:: python

    # Create risk settings to calculate Delta with central difference method
    risk_settings = analytics.create_ir_curve_risk_settings(delta=True)
