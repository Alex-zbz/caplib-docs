from datetime import datetime

from caplib.numerics import *
from caplib.market import *
from caplib.datetime import *
from caplib.analytics import *
from caplib.processrequest import process_request

#NumericalFix
def to_numerical_fix(src):
    """
    Convert the source to a numerical fix representation.

    Parameters
    ----------
    src : str or None
        The source string to convert.

    Returns
    -------
    int
        The numerical fix representation.
    """
    if src is None:
        return NONE_FIX
    
    if src in ['', 'nan']:
        return NONE_FIX
    else:
        return NumericalFix.DESCRIPTOR.values_by_name[src.upper()].number

def to_accrual_bias(src):
    """
    Convert the source to an accrual bias representation.

    Parameters
    ----------
    src : str or None
        The source string to convert.

    Returns
    -------
    int
        The accrual bias representation.
    """
    if src is None:
        return HALFDAYBIAS
    
    if src in ['', 'nan']:
        return HALFDAYBIAS
    else:
        return AccrualBias.DESCRIPTOR.values_by_name[src.upper()].number

def to_forwards_in_coupon_period(src):
    """
    Convert the source to a forwards in coupon period representation.

    Parameters
    ----------
    src : str or None
        The source string to convert.

    Returns
    -------
    int
        The forwards in coupon period representation.
    """
    if src is None:
        return FLAT
    
    if src in ['', 'nan']:
        return FLAT
    else:
        return ForwardsInCouponPeriod.DESCRIPTOR.values_by_name[src.upper()].number

def create_cr_risk_settings(ir_curve_settings, cs_curve_settings, theta_settings):
    """
    Create credit risk settings.

    Parameters
    ----------
    ir_curve_settings : object
        Interest rate curve settings.
    cs_curve_settings : object
        Credit spread curve settings.
    theta_settings : object
        Theta settings.

    Returns
    -------
    object
        Credit risk settings.
    """
    settings = dqCreateProtoCrRiskSettings(ir_curve_settings,
                                           cs_curve_settings,
                                           theta_settings)
    return settings

def create_credit_par_curve(as_of_date, currency, name, pillars, tag, mode, save, location):
    """
    Create a credit par curve.

    Parameters
    ----------
    as_of_date : datetime
        The reference date for the curve.
    currency : str
        The currency of the curve.
    name : str
        The name of the curve.
    pillars : list
        List of tuples representing pillar data.
    tag : str
        Tag for the curve.
    mode : str
        Mode for the curve creation.
    save : bool
        Whether to save the curve.
    location : str
        Location to save the curve.

    Returns
    -------
    object
        The created credit par curve.
    """
    try:
        pillars = list()
        for pillar in pillars:
            pillars.append(dqCreateProtoCreditParCurve_Pillar(str(pillar[0]), 
                                              to_instrument_type(str(pillar[1])), 
                                              to_period(str(pillar[2])), 
                                              float(pillar[3]), 
                                              to_instrument_start_convention('spot_start')))            
        pb_input = dqCreateProtoCreateCreditParCurveInput(create_date(as_of_date),
                                                          currency,
                                                          pillars,
                                                          name)
        req_name = "CREATE_CREDIT_PAR_CURVE"
        res_msg = process_request(req_name, pb_input.SerializeToString())   
        pb_output = CreateCreditParCurveOutput()
        pb_output.ParseFromString(res_msg)        
        if pb_output.success == False:
            raise Exception(pb_output.err_msg)      
        return pb_output.par_curve  
    except Exception as e:
        return str(e)

def credit_curve_builder(as_of_date, curve_name, build_settings, par_curve, discount_curve, building_method, calc_jacobian):
    """
    Build a credit curve.

    Parameters
    ----------
    as_of_date : datetime
        The reference date for the curve.
    curve_name : str
        The name of the curve.
    build_settings : object
        Build settings for the curve.
    par_curve : object
        Par curve for the credit curve.
    discount_curve : object
        Discount curve for the credit curve.
    building_method : str
        Method to build the curve.
    calc_jacobian : bool
        Whether to calculate the Jacobian.

    Returns
    -------
    object
        The built credit curve.
    """
    try:
        pb_input = dqCreateProtoCreditCurveBuildingInput(par_curve,
                                                         curve_name,
                                                         create_date(as_of_date),
                                                         discount_curve,
                                                         building_method)        
        
        req_name = "CREDIT_CURVE_BUILDER"
        res_msg = process_request(req_name, pb_input.SerializeToString())   
        pb_output = CreditCurveBuildingOutput()
        pb_output.ParseFromString(res_msg)        
        if pb_output.success == False:
            raise Exception(pb_output.err_msg)      
        return pb_output.credit_curve  
    except Exception as e:
        return str(e)

def create_cds_pricing_settings(pricing_currency,
                                include_current_flow,
                                cash_flows,
                                include_settlement_flow,
                                numerical_fix,
                                accrual_bias,
                                fwds_in_cpn_period,
                                name,
                                tag):
    """
    Create CDS pricing settings.

    Parameters
    ----------
    pricing_currency : str
        The currency for pricing.
    include_current_flow : bool
        Whether to include current flow.
    cash_flows : object
        Cash flows for pricing.
    include_settlement_flow : bool
        Whether to include settlement flow.
    numerical_fix : str
        Numerical fix setting.
    accrual_bias : str
        Accrual bias setting.
    fwds_in_cpn_period : str
        Forwards in coupon period setting.
    name : str
        Name for the pricing settings.
    tag : str
        Tag for the pricing settings.

    Returns
    -------
    object
        The created CDS pricing settings.
    """
    try:
        model_params = [int(include_current_flow), 
                        int(to_numerical_fix(numerical_fix)), 
                        int(to_accrual_bias(accrual_bias)), 
                        int(to_forwards_in_coupon_period(fwds_in_cpn_period)) ]
        model_settings = create_model_settings("", model_params)
        settings = create_pricing_settings(
            pricing_currency,
            include_current_flow,
            cash_flows,
            None
        )
        settings.model_settings = model_settings
        return settings
    except Exception as e:
        return str(e)

def create_cr_mkt_data_set(as_of_date, discount_curve, credit_curve, name, tag):
    """
    Create credit market data set.

    Parameters
    ----------
    as_of_date : datetime
        The reference date for the market data set.
    discount_curve : object
        The discount curve.
    credit_curve : object
        The credit curve.
    name : str
        Name for the market data set.
    tag : str
        Tag for the market data set.

    Returns
    -------
    object
        The created credit market data set.
    """
    try:
        mkt_data = dqCreateProtoCrMktDataSet(create_date(as_of_date),
                                             discount_curve,
                                             credit_curve)
        return mkt_data
    except Exception as e:
        return str(e)

def credit_default_swap_pricer(instrument,
                               pricing_date,
                               mkt_data_set,
                               pricing_settings,
                               risk_settings,
                               result_tag,
                               rtn_type,
                               mode):
    """
    Price a credit default swap.

    Parameters
    ----------
    instrument : object
        The credit default swap instrument.
    pricing_date : datetime
        The date for pricing.
    mkt_data_set : object
        Market data set for pricing.
    pricing_settings : object
        Pricing settings for the swap.
    risk_settings : object
        Risk settings for the swap.
    result_tag : str
        Tag for the result.
    rtn_type : str
        Return type for the result.
    mode : str
        Mode for the pricing.

    Returns
    -------
    object
        The result of credit default swap pricing.
    """
    try:
        credit_default_swap_pricing_input = dqCreateProtoCreditDefaultSwapPricingInput(create_date(pricing_date),
                                                                                       instrument,
                                                                                       mkt_data_set,
                                                                                       pricing_settings,
                                                                                       risk_settings,
                                                                                       False, '', '', '', '')
        req_name = "CREDIT_DEFAULT_SWAP_PRICER"
        res_msg = process_request(req_name, credit_default_swap_pricing_input.SerializeToString())   
        pb_output = CreditDefaultSwapPricingOutput()
        pb_output.ParseFromString(res_msg)        
        if pb_output.success == False:
            raise Exception(pb_output.err_msg)      
        return pb_output
    except Exception as e:
        return str(e)