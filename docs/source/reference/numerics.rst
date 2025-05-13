Numerics
========

This section covers the numerical methods and utilities available in the caplib.numerics module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Type Conversion Functions
----------------------

The module provides functions for converting string representations to various numerical types and methods.

.. code-block:: python

    from caplib.numerics import (
        to_interp_method,
        to_extrap_method,
        to_uniform_random_number_type,
        to_gaussian_number_method,
        to_wiener_process_build_method,
        to_grid_type,
        to_pde_min_max_type
    )
    
    # Convert string to interpolation method
    interp_method = to_interp_method("LINEAR_INTERP")
    
    # Convert string to extrapolation method
    extrap_method = to_extrap_method("FLAT_EXTRAP")
    
    # Convert string to uniform random number type
    random_type = to_uniform_random_number_type("SOBOL_NUMBER")
    
    # Convert string to Gaussian number method
    gaussian_method = to_gaussian_number_method("INVERSE_CUMULATIVE_METHOD")
    
    # Convert string to Wiener process build method
    wiener_method = to_wiener_process_build_method("BROWNIAN_BRIDGE_METHOD")
    
    # Convert string to grid type
    grid_type = to_grid_type("UNIFORM_GRID")
    
    # Convert string to PDE settings min/max type
    min_max_type = to_pde_min_max_type("MMT_NUM_STDEVS")

Matrix Operations
--------------

Functions for creating and manipulating matrices for numerical computations.

.. code-block:: python

    import numpy as np
    from caplib.numerics import create_matrix
    
    # Create a 3x3 matrix from numpy array
    data = np.array([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]
    ])
    
    matrix = create_matrix(data)
    
    # Matrix can now be used with other caplib functions that require matrices

Interpolation and Extrapolation Methods
----------------------------------

The module supports various interpolation and extrapolation methods for numerical analysis.

Interpolation Methods
~~~~~~~~~~~~~~~~

The following interpolation methods are available:

* ``LINEAR_INTERP`` - Linear interpolation between points
* ``LOG_LINEAR_INTERP`` - Linear interpolation in log space
* ``CUBIC_SPLINE_INTERP`` - Cubic spline interpolation for smooth curves

Example:

.. code-block:: python

    # Setting up interpolation for a yield curve
    from caplib.iranalytics import create_ir_curve_build_settings
    from caplib.numerics import to_interp_method
    
    interp_method = to_interp_method("CUBIC_SPLINE_INTERP")
    
    settings = create_ir_curve_build_settings(
        curve_name="USD_LIBOR",
        discount_curves=[],
        forward_curves=[],
        interp_method=interp_method
    )

Extrapolation Methods
~~~~~~~~~~~~~~~~

The following extrapolation methods are available:

* ``FLAT_EXTRAP`` - Uses the nearest known value
* ``LINEAR_EXTRAP`` - Linear extrapolation based on nearest points

Example:

.. code-block:: python

    # Setting up extrapolation for a yield curve
    from caplib.iranalytics import create_ir_curve_build_settings
    from caplib.numerics import to_extrap_method
    
    extrap_method = to_extrap_method("FLAT_EXTRAP")
    
    settings = create_ir_curve_build_settings(
        curve_name="USD_LIBOR",
        discount_curves=[],
        forward_curves=[],
        extrap_method=extrap_method
    )

Random Number Generation
--------------------

The module provides utilities for generating random numbers for Monte Carlo simulations.

Uniform Random Number Types
~~~~~~~~~~~~~~~~~~~~~

* ``PSEUDO_NUMBER`` - Pseudo-random numbers
* ``SOBOL_NUMBER`` - Sobol sequence (quasi-random numbers)

Example:

.. code-block:: python

    from caplib.numerics import to_uniform_random_number_type
    from caplibproto.dqproto import RandomNumberGeneratorSettings
    
    # Create random number generator settings
    rng_settings = RandomNumberGeneratorSettings()
    rng_settings.type = to_uniform_random_number_type("SOBOL_NUMBER")
    rng_settings.dimension = 2
    rng_settings.seed = 42

Gaussian Number Methods
~~~~~~~~~~~~~~~~~~

* ``INVERSE_CUMULATIVE_METHOD`` - Uses inverse cumulative normal distribution
* ``BOX_MULLER_METHOD`` - Box-Muller transform

Example:

.. code-block:: python

    from caplib.numerics import to_gaussian_number_method
    
    # Set Gaussian number generation method
    gaussian_method = to_gaussian_number_method("INVERSE_CUMULATIVE_METHOD")

Wiener Process Methods
----------------

Methods for building Wiener processes in stochastic simulations.

* ``BROWNIAN_BRIDGE_METHOD`` - Brownian bridge construction
* ``STANDARD_METHOD`` - Standard incremental construction

Example:

.. code-block:: python

    from caplib.numerics import to_wiener_process_build_method
    
    # Set Wiener process construction method
    wiener_method = to_wiener_process_build_method("BROWNIAN_BRIDGE_METHOD")

Grid Types for PDE Solvers
----------------------

Grid types used in partial differential equation (PDE) solvers.

* ``UNIFORM_GRID`` - Evenly spaced grid points
* ``CONCENTRATION_POINT_GRID`` - Grid with points concentrated around specific values

Example:

.. code-block:: python

    from caplib.numerics import to_grid_type
    from caplibproto.dqproto import PdeSettings
    
    # Create PDE settings with grid type
    pde_settings = PdeSettings()
    pde_settings.grid_type = to_grid_type("UNIFORM_GRID")
    pde_settings.num_space_steps = 100
    pde_settings.num_time_steps = 50

PDE Min/Max Types
-------------

Methods for specifying minimum and maximum bounds in PDE solvers.

* ``MMT_NUM_STDEVS`` - Number of standard deviations from mean
* ``MMT_ABS_LEVEL`` - Absolute minimum and maximum levels

Example:

.. code-block:: python

    from caplib.numerics import to_pde_min_max_type
    from caplibproto.dqproto import PdeSettings
    
    # Create PDE settings with min/max type
    pde_settings = PdeSettings()
    pde_settings.min_max_type = to_pde_min_max_type("MMT_NUM_STDEVS")
    pde_settings.upper_bound = 5.0  # 5 standard deviations above mean
    pde_settings.lower_bound = -5.0  # 5 standard deviations below mean

Complete Workflow Example
--------------------

Here's a complete workflow demonstrating the use of numerical methods:

.. code-block:: python

    import numpy as np
    from datetime import datetime
    from caplib.datetime import create_date
    from caplib.numerics import (
        to_interp_method,
        to_extrap_method,
        to_uniform_random_number_type,
        to_wiener_process_build_method,
        create_matrix
    )
    
    # Step 1: Set up dates for curve construction
    as_of_date = datetime(2025, 3, 20)
    
    # Step 2: Set up numerical methods
    interp_method = to_interp_method("CUBIC_SPLINE_INTERP")
    extrap_method = to_extrap_method("FLAT_EXTRAP")
    
    # Step 3: Create correlation matrix for multi-factor model
    correlation_data = np.array([
        [1.0, 0.5, 0.3],
        [0.5, 1.0, 0.2],
        [0.3, 0.2, 1.0]
    ])
    
    correlation_matrix = create_matrix(correlation_data)
    
    # Step 4: Set up Monte Carlo simulation settings
    random_type = to_uniform_random_number_type("SOBOL_NUMBER")
    wiener_method = to_wiener_process_build_method("BROWNIAN_BRIDGE_METHOD")
    
    # Step 5: Configure and run a hypothetical Monte Carlo simulation
    # (This is conceptual; actual implementation would use appropriate caplib functions)
    from caplibproto.dqproto import MonteCarloSettings
    
    mc_settings = MonteCarloSettings()
    mc_settings.num_paths = 10000
    mc_settings.time_steps = 50
    mc_settings.random_type = random_type
    mc_settings.wiener_method = wiener_method
    
    # Step 6: Output configuration
    print(f"As-of Date: {as_of_date}")
    print(f"Interpolation Method: {interp_method}")
    print(f"Extrapolation Method: {extrap_method}")
    print(f"Correlation Matrix: 3x3 matrix")
    print(f"Random Number Type: {random_type}")
    print(f"Wiener Process Method: {wiener_method}")
    print(f"Monte Carlo Paths: {mc_settings.num_paths}")
    print(f"Monte Carlo Time Steps: {mc_settings.time_steps}")
