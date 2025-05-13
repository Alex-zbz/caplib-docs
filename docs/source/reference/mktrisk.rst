Market Risk
===========

This section covers the market risk functionality available in the caplib.mktrisk module.

.. contents:: Table of Contents
   :local:
   :depth: 2

Risk Factor Analysis
-----------------

**Function Signatures**

.. code-block:: python

    calculate_risk_factor_change(risk_factor_values, change_type)
    simulate_risk_factor(risk_factor_changes, change_type, base)

**Parameters for calculate_risk_factor_change**

* **risk_factor_values** (*list*) - Historical values of the risk factor
* **change_type** (*str*) - Type of change calculation (e.g., "LOG_RETURN", "SIMPLE_RETURN", "ABSOLUTE_CHANGE")

**Parameters for simulate_risk_factor**

* **risk_factor_changes** (*list*) - Calculated changes from historical values
* **change_type** (*str*) - Type of change calculation used (must match calculation type)
* **base** (*float*) - Current value of the risk factor

**Returns**

* List of changes (for calculate_risk_factor_change)
* List of simulated scenarios (for simulate_risk_factor)

**Example**

.. code-block:: python

    from caplib.mktrisk import calculate_risk_factor_change, simulate_risk_factor
    
    # Historical risk factor values (e.g., daily closing prices)
    risk_factor_values = [100.0, 101.2, 99.8, 102.5, 103.1]
    
    # Calculate risk factor changes (returns)
    changes = calculate_risk_factor_change(
        risk_factor_values=risk_factor_values,
        change_type="LOG_RETURN"  # Can also use "SIMPLE_RETURN" or "ABSOLUTE_CHANGE"
    )
    
    # Simulate future scenarios based on historical changes
    simulated_scenarios = simulate_risk_factor(
        risk_factor_changes=changes,
        change_type="LOG_RETURN",
        base=103.1  # Current value of risk factor
    )

Return Calculation
--------------

**Function Signatures**

.. code-block:: python

    calculate_inst_raw_returns(settings, inst_price_series)
    calculate_inst_cleansed_returns(settings, inst_quote_series, inst_listed_date, proxy_return_series)

**Parameters for calculate_inst_raw_returns**

* **settings** (*object*) - InstrumentReturnSettings object specifying return calculation method
* **inst_price_series** (*object*) - Time series of instrument prices

**Parameters for calculate_inst_cleansed_returns**

* **settings** (*object*) - InstrumentCleansedReturnSettings object
* **inst_quote_series** (*object*) - Time series of instrument quotes/prices
* **inst_listed_date** (*datetime*) - Date when the instrument was listed/started trading
* **proxy_return_series** (*object*) - Time series of proxy returns for filling gaps

**Returns**

* Time series of calculated returns

**Example**

.. code-block:: python

    from datetime import datetime
    from caplib.mktrisk import calculate_inst_raw_returns, calculate_inst_cleansed_returns
    from caplib.datetime import create_date
    from caplib.market import create_time_series
    
    # Create a price time series for an instrument
    as_of_date = datetime(2025, 3, 20)
    dates = [
        create_date(as_of_date, "-4D", "PRECEDING", ["US"]),
        create_date(as_of_date, "-3D", "PRECEDING", ["US"]),
        create_date(as_of_date, "-2D", "PRECEDING", ["US"]),
        create_date(as_of_date, "-1D", "PRECEDING", ["US"]),
        as_of_date
    ]
    
    prices = [50.25, 51.30, 51.15, 52.40, 52.75]
    
    price_series = create_time_series(
        dates=dates,
        values=prices,
        mode="TS_FORWARD_MODE",
        name="AAPL_PRICE_TS"
    )
    
    # Create return calculation settings
    from caplibproto.dqproto import InstrumentReturnSettings
    
    return_settings = InstrumentReturnSettings()
    return_settings.type = 1  # LOG_RETURN
    
    # Calculate raw returns
    raw_returns = calculate_inst_raw_returns(
        settings=return_settings,
        inst_price_series=price_series
    )
    
    # For cleansed returns, we would need proxy return series and listed date
    # This is just a conceptual example
    listed_date = create_date(as_of_date, "-1Y", "PRECEDING", ["US"])
    
    cleansed_settings = InstrumentCleansedReturnSettings()
    cleansed_settings.type = 1  # LOG_RETURN
    
    cleansed_returns = calculate_inst_cleansed_returns(
        settings=cleansed_settings,
        inst_quote_series=price_series,
        inst_listed_date=listed_date,
        proxy_return_series=proxy_returns  # This would need to be defined
    )

Scenario Generation
---------------

**Function Signatures**

.. code-block:: python

    generate_hist_sim_scenarios(settings, inst_return_series, risk_factor_name, as_of_date)
    identify_stress_dates(settings, benchmark_return_series, as_of_date)
    generate_stressed_scenarios(settings, inst_return_series, risk_factor_name, stress_dates, as_of_date)

**Parameters for generate_hist_sim_scenarios**

* **settings** (*object*) - HsScnGenSettings object with scenario generation parameters
* **inst_return_series** (*object*) - Time series of instrument returns
* **risk_factor_name** (*str*) - Name of the risk factor
* **as_of_date** (*datetime*) - Reference date for scenario generation

**Parameters for identify_stress_dates**

* **settings** (*object*) - StressedScnGenSettings object
* **benchmark_return_series** (*object*) - Time series of benchmark returns
* **as_of_date** (*datetime*) - Reference date for identifying stress dates

**Parameters for generate_stressed_scenarios**

* **settings** (*object*) - StressedScnGenSettings object
* **inst_return_series** (*object*) - Time series of instrument returns
* **risk_factor_name** (*str*) - Name of the risk factor
* **stress_dates** (*list*) - List of stress dates identified
* **as_of_date** (*datetime*) - Reference date for scenario generation

**Returns**

* Generated scenarios based on method used
* List of stress dates (for identify_stress_dates)

**Example**

.. code-block:: python

    from caplib.mktrisk import (
        generate_hist_sim_scenarios,
        identify_stress_dates,
        generate_stressed_scenarios
    )
    
    # Create historical simulation settings
    from caplibproto.dqproto import HsScnGenSettings
    
    hs_settings = HsScnGenSettings()
    hs_settings.lookback_days = 252  # One year of trading days
    hs_settings.holding_period = 1  # One-day VaR
    
    # Generate historical simulation scenarios
    # This is conceptual; actual implementation would require proper return series
    hist_scenarios = generate_hist_sim_scenarios(
        settings=hs_settings,
        inst_return_series=return_series,
        risk_factor_name="AAPL",
        as_of_date=as_of_date
    )
    
    # Identify stress dates using a benchmark
    from caplibproto.dqproto import StressedScnGenSettings
    
    stress_settings = StressedScnGenSettings()
    stress_settings.num_of_scenarios = 10  # Number of stress scenarios to generate
    
    stress_dates = identify_stress_dates(
        settings=stress_settings,
        benchmark_return_series=benchmark_returns,  # E.g., S&P 500 returns
        as_of_date=as_of_date
    )
    
    # Generate stressed scenarios
    stressed_scenarios = generate_stressed_scenarios(
        settings=stress_settings,
        inst_return_series=return_series,
        risk_factor_name="AAPL",
        stress_dates=stress_dates,
        as_of_date=as_of_date
    )

Portfolio Construction
-------------------

**Function Signatures**

.. code-block:: python

    create_trading_position(buy_sell, norminal, inst_name, tier)
    create_portfolio(portfolio_id, trading_positions)

**Parameters for create_trading_position**

* **buy_sell** (*enum*) - Buy or sell flag (use to_buy_sell_flag)
* **norminal** (*float*) - Nominal amount of the position
* **inst_name** (*str*) - Name of the instrument
* **tier** (*int*) - Instrument tier for margin calculations

**Parameters for create_portfolio**

* **portfolio_id** (*str*) - Unique identifier for the portfolio
* **trading_positions** (*list*) - List of trading positions

**Returns**

* Trading position object (for create_trading_position)
* Portfolio object (for create_portfolio)

**Example**

.. code-block:: python

    from caplib.mktrisk import create_trading_position, create_portfolio
    from caplib.market import to_buy_sell_flag
    
    # Create a buy position
    buy_flag = to_buy_sell_flag("BUY")
    
    position_1 = create_trading_position(
        buy_sell=buy_flag,
        norminal=1000000.0,
        inst_name="AAPL",
        tier=1  # Instrument tier for margin calculations
    )
    
    # Create a sell position
    sell_flag = to_buy_sell_flag("SELL")
    
    position_2 = create_trading_position(
        buy_sell=sell_flag,
        norminal=500000.0,
        inst_name="MSFT",
        tier=1
    )
    
    # Create a portfolio from positions
    portfolio = create_portfolio(
        portfolio_id="TECH_PORTFOLIO",
        trading_positions=[position_1, position_2]
    )

Risk Metrics Calculation
--------------------

**Function Signatures**

.. code-block:: python

    calculate_profit_loss_distribution(portfolio, scenarios)
    calculate_value_at_risk(profit_loss_samples, probability, antithetic=False)
    calculate_expected_short_fall(profit_loss_samples, probability, antithetic=False)

**Parameters for calculate_profit_loss_distribution**

* **portfolio** (*object*) - Portfolio object with trading positions
* **scenarios** (*object*) - Scenarios for risk calculation

**Parameters for calculate_value_at_risk**

* **profit_loss_samples** (*list*) - Distribution of profit/loss samples
* **probability** (*float*) - Confidence level (e.g., 0.99 for 99% VaR)
* **antithetic** (*bool, optional*) - Whether to use antithetic sampling

**Parameters for calculate_expected_short_fall**

* **profit_loss_samples** (*list*) - Distribution of profit/loss samples
* **probability** (*float*) - Confidence level (e.g., 0.99 for 99% ES)
* **antithetic** (*bool, optional*) - Whether to use antithetic sampling

**Returns**

* Profit/loss distribution (for calculate_profit_loss_distribution)
* Value at Risk (for calculate_value_at_risk)
* Expected Shortfall (for calculate_expected_short_fall)

**Example**

.. code-block:: python

    from caplib.mktrisk import (
        calculate_profit_loss_distribution,
        calculate_value_at_risk,
        calculate_expected_short_fall
    )
    
    # Calculate P&L distribution from scenarios
    pnl_distribution = calculate_profit_loss_distribution(
        portfolio=portfolio,
        scenarios=hist_scenarios  # From previous example
    )
    
    # Calculate Value at Risk (VaR)
    var_result = calculate_value_at_risk(
        profit_loss_samples=pnl_distribution,
        probability=0.99,  # 99% VaR
        antithetic=False
    )
    
    # Calculate Expected Shortfall (ES)
    es_result = calculate_expected_short_fall(
        profit_loss_samples=pnl_distribution,
        probability=0.99,  # 99% ES
        antithetic=False
    )

Initial Margin Calculation
----------------------

**Function Signatures**

.. code-block:: python

    calculate_tier_p_initial_margin(settings, portfolio, portfolio_hs_profit_loss_samples, position_hs_profit_loss_samples, portfolio_stressed_profit_loss_samples, position_stressed_profit_loss_samples)
    calculate_tier_n_initial_margin_rate(settings, reference_date, benchmark_1, benchmark_2)
    calculate_tier_n_initial_margin(portfolio, margin_rate)
    calculate_total_initial_margin(p_initial_margins, n_initial_margin, round_up_value)

**Parameters for calculate_tier_p_initial_margin**

* **settings** (*object*) - TierPInitialMarginSettings object
* **portfolio** (*object*) - Portfolio object
* **portfolio_hs_profit_loss_samples** (*list*) - Historical simulation profit/loss samples for the portfolio
* **position_hs_profit_loss_samples** (*list*) - Historical simulation profit/loss samples for each position
* **portfolio_stressed_profit_loss_samples** (*list*) - Stressed profit/loss samples for the portfolio
* **position_stressed_profit_loss_samples** (*list*) - Stressed profit/loss samples for each position

**Parameters for calculate_tier_n_initial_margin_rate**

* **settings** (*object*) - TierNInitialMarginSettings object
* **reference_date** (*datetime*) - Reference date for calculation
* **benchmark_1** (*object*) - First benchmark for calculation
* **benchmark_2** (*object*) - Second benchmark for calculation

**Parameters for calculate_tier_n_initial_margin**

* **portfolio** (*object*) - Portfolio object
* **margin_rate** (*float*) - Margin rate calculated

**Parameters for calculate_total_initial_margin**

* **p_initial_margins** (*list*) - Tier P initial margins for each position
* **n_initial_margin** (*float*) - Tier N initial margin for the portfolio
* **round_up_value** (*int*) - Value to round up to

**Returns**

* Tier P initial margin (for calculate_tier_p_initial_margin)
* Tier N initial margin rate (for calculate_tier_n_initial_margin_rate)
* Tier N initial margin (for calculate_tier_n_initial_margin)
* Total initial margin (for calculate_total_initial_margin)

**Example**

.. code-block:: python

    from caplib.mktrisk import (
        calculate_tier_p_initial_margin,
        calculate_tier_n_initial_margin_rate,
        calculate_tier_n_initial_margin,
        calculate_total_initial_margin
    )
    
    # For tier P initial margin (conceptual example)
    from caplibproto.dqproto import TierPInitialMarginSettings
    
    tier_p_settings = TierPInitialMarginSettings()
    tier_p_settings.confidence_level = 0.995
    tier_p_settings.lookback_period = 252
    tier_p_settings.liquidity_horizon = 1
    
    # Calculate tier P initial margin
    # This requires portfolio and position P&L samples
    tier_p_result = calculate_tier_p_initial_margin(
        settings=tier_p_settings,
        portfolio=portfolio,
        portfolio_hs_profit_loss_samples=portfolio_hs_pnl,
        position_hs_profit_loss_samples=position_hs_pnl_list,
        portfolio_stressed_profit_loss_samples=portfolio_stress_pnl,
        position_stressed_profit_loss_samples=position_stress_pnl_list
    )
    
    # Calculate tier N initial margin rate
    from caplibproto.dqproto import TierNInitialMarginSettings
    
    tier_n_settings = TierNInitialMarginSettings()
    tier_n_settings.lookback_days = 252
    
    tier_n_rate = calculate_tier_n_initial_margin_rate(
        settings=tier_n_settings,
        reference_date=as_of_date,
        benchmark_1=benchmark_1_returns,
        benchmark_2=benchmark_2_returns
    )
    
    # Calculate tier N initial margin
    tier_n_margin = calculate_tier_n_initial_margin(
        portfolio=portfolio,
        margin_rate=tier_n_rate
    )
    
    # Calculate total initial margin
    total_margin = calculate_total_initial_margin(
        p_initial_margins=tier_p_result.margin,
        n_initial_margin=tier_n_margin,
        round_up_value=1000  # Round up to nearest 1000
    )

Running Risk Engines
----------------

**Function Signatures**

.. code-block:: python

    run_data_cleansing_engine(settings, index_series, inst_quote_series)
    run_initial_margin_engine(im_settings, hs_scn_gen_settings, stressed_scn_gen_settings, portfolios, use_arbitrary_scenario, hs_scenarios, stressed_scenarios)
    run_initial_margin_backtesting_engine(im_settings, hs_scn_gen_settings, stressed_scn_gen_settings, portfolios, cleansed_return_data, raw_return_data, schedule, name, tag)
    get_im_backtesting_result(initial_margin_backtesting_engine, portfolio, instrument, backtesting_date, option)

**Parameters for run_data_cleansing_engine**

* **settings** (*object*) - RiskFactorDataCleansingSettings object
* **index_series** (*object*) - Time series of index values
* **inst_quote_series** (*object*) - Time series of instrument quotes

**Parameters for run_initial_margin_engine**

* **im_settings** (*object*) - InitialMarginSettings object
* **hs_scn_gen_settings** (*object*) - HsScnGenSettings object
* **stressed_scn_gen_settings** (*object*) - StressedScnGenSettings object
* **portfolios** (*list*) - List of portfolios
* **use_arbitrary_scenario** (*bool*) - Whether to use arbitrary scenario
* **hs_scenarios** (*object*) - Historical simulation scenarios
* **stressed_scenarios** (*object*) - Stressed scenarios

**Parameters for run_initial_margin_backtesting_engine**

* **im_settings** (*object*) - InitialMarginSettings object
* **hs_scn_gen_settings** (*object*) - HsScnGenSettings object
* **stressed_scn_gen_settings** (*object*) - StressedScnGenSettings object
* **portfolios** (*list*) - List of portfolios
* **cleansed_return_data** (*object*) - Cleansed return data
* **raw_return_data** (*object*) - Raw return data
* **schedule** (*object*) - Schedule for backtesting
* **name** (*str*) - Name of the backtesting engine
* **tag** (*str*) - Tag for the backtesting engine

**Parameters for get_im_backtesting_result**

* **initial_margin_backtesting_engine** (*str*) - Name of the initial margin backtesting engine
* **portfolio** (*str*) - Portfolio ID
* **instrument** (*str*) - Instrument ID
* **backtesting_date** (*datetime*) - Backtesting date
* **option** (*str*) - Option for the result (e.g., "DETAILED")

**Returns**

* Cleansed data (for run_data_cleansing_engine)
* Initial margin results (for run_initial_margin_engine)
* Backtesting results (for run_initial_margin_backtesting_engine)
* Backtesting result (for get_im_backtesting_result)

**Example**

.. code-block:: python

    from caplib.mktrisk import (
        run_data_cleansing_engine,
        run_initial_margin_engine,
        run_initial_margin_backtesting_engine,
        get_im_backtesting_result
    )
    
    # Run data cleansing engine (conceptual example)
    from caplibproto.dqproto import RiskFactorDataCleansingSettings
    
    cleansing_settings = RiskFactorDataCleansingSettings()
    cleansing_settings.window_size = 21  # 21-day window
    
    cleansed_data = run_data_cleansing_engine(
        settings=cleansing_settings,
        index_series=benchmark_ts,
        inst_quote_series=instrument_quotes
    )
    
    # Run initial margin engine
    from caplibproto.dqproto import InitialMarginSettings
    
    im_settings = InitialMarginSettings()
    im_settings.tier_p_settings.confidence_level = 0.995
    im_settings.tier_p_settings.lookback_period = 252
    
    im_result = run_initial_margin_engine(
        im_settings=im_settings,
        hs_scn_gen_settings=hs_settings,
        stressed_scn_gen_settings=stress_settings,
        portfolios=[portfolio],
        use_arbitrary_scenario=False,
        hs_scenarios=None,
        stressed_scenarios=None
    )
    
    # Run initial margin backtesting
    schedule = create_schedule(start_date, end_date, "1D", "FOLLOWING", ["US"])
    
    backtesting_result = run_initial_margin_backtesting_engine(
        im_settings=im_settings,
        hs_scn_gen_settings=hs_settings,
        stressed_scn_gen_settings=stress_settings,
        portfolios=[portfolio],
        cleansed_return_data=cleansed_returns,
        raw_return_data=raw_returns,
        schedule=schedule,
        name="BACKTEST_1",
        tag="PRODUCTION"
    )
    
    # Get backtesting results
    specific_result = get_im_backtesting_result(
        initial_margin_backtesting_engine="BACKTEST_1",
        portfolio="TECH_PORTFOLIO",
        instrument="AAPL",
        backtesting_date=as_of_date,
        option="DETAILED"
    )

Complete Workflow Example
--------------------

Here's a complete workflow demonstrating VaR calculation for a portfolio:

.. code-block:: python

    from datetime import datetime
    from caplib.datetime import create_date
    from caplib.market import create_time_series, to_buy_sell_flag
    from caplib.mktrisk import (
        calculate_risk_factor_change,
        simulate_risk_factor,
        create_trading_position,
        create_portfolio,
        calculate_profit_loss_distribution,
        calculate_value_at_risk,
        calculate_expected_short_fall
    )
    
    # Step 1: Set up dates and time series
    as_of_date = datetime(2025, 3, 20)
    
    # Create historical price data for risk factor (equity price)
    dates = []
    prices = []
    
    # Create a year of trading days (simplified)
    for i in range(252):
        dates.append(create_date(as_of_date, f"-{252-i}D", "PRECEDING", ["US"]))
    
    # Dummy price data (in reality, this would be actual historical data)
    import random
    random.seed(42)  # For reproducibility
    
    current_price = 100.0
    prices.append(current_price)
    
    for i in range(1, 252):
        # Generate random daily return between -3% and +3%
        daily_return = random.uniform(-0.03, 0.03)
        current_price = current_price * (1 + daily_return)
        prices.append(current_price)
    
    # Create time series
    price_ts = create_time_series(
        dates=dates,
        values=prices,
        mode="TS_FORWARD_MODE",
        name="EQUITY_PRICE_TS"
    )
    
    # Step 2: Calculate risk factor changes
    changes = calculate_risk_factor_change(
        risk_factor_values=prices,
        change_type="LOG_RETURN"
    )
    
    # Step 3: Create portfolio
    buy_flag = to_buy_sell_flag("BUY")
    
    position = create_trading_position(
        buy_sell=buy_flag,
        norminal=1000000.0,  # $1 million position
        inst_name="EQUITY",
        tier=1
    )
    
    portfolio = create_portfolio(
        portfolio_id="SAMPLE_PORTFOLIO",
        trading_positions=[position]
    )
    
    # Step 4: Generate scenarios (simplified approach)
    from caplibproto.dqproto import Scenario
    
    # Create 1000 scenarios by resampling historical returns
    num_scenarios = 1000
    scenarios = Scenario()
    
    for i in range(num_scenarios):
        # Randomly select a historical return
        idx = random.randint(0, len(changes) - 1)
        scenario_change = changes[idx]
        
        # Add to scenarios (in a real implementation, this would use proper API calls)
        # This is simplified for illustration
        scenarios.values.append(scenario_change)
    
    # Step 5: Calculate P&L distribution
    pnl_distribution = calculate_profit_loss_distribution(
        portfolio=portfolio,
        scenarios=scenarios
    )
    
    # Step 6: Calculate risk metrics
    var_result = calculate_value_at_risk(
        profit_loss_samples=pnl_distribution,
        probability=0.99,  # 99% VaR
        antithetic=False
    )
    
    es_result = calculate_expected_short_fall(
        profit_loss_samples=pnl_distribution,
        probability=0.99,  # 99% ES
        antithetic=False
    )
    
    # Step 7: Output results
    print(f"Portfolio: {portfolio.id}")
    print(f"Position Size: ${position.nominal:,.2f}")
    print(f"Number of Scenarios: {num_scenarios}")
    print(f"99% Value at Risk: ${-var_result.value:,.2f}")
    print(f"99% Expected Shortfall: ${-es_result.value:,.2f}")
