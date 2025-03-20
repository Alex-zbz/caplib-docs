# -*- coding: utf-8 -*-
import unittest
from datetime import datetime

from caplib.datetime import *
from caplib.market import *
from caplib.irmarket import *

class TestIrMarket(unittest.TestCase):
    
    def setUp(self):
        cny_ccy = 'cny'
        cal_cfets = 'CAL_CFETS'
        
        hol_serial_numbers =[44654, 44954]
        sbd_serial_numbers = [44655]
        # Convert list of serial numbers to datetime objects
        holidays = [datetime.fromordinal(sn) for sn in hol_serial_numbers]
        specials = [datetime.fromordinal(sn) for sn in sbd_serial_numbers]
        create_calendar(cal_cfets, holidays, specials)
        
        shibor_3m = 'shibor_3m'
        create_ibor_index(shibor_3m, '3m', cny_ccy, [cal_cfets], 1)
        
        freq = 'QUARTERLY'
        self.cny_shibor_3m_fixed_leg_def = create_fixed_leg_definition(cny_ccy, cal_cfets, freq)
        self.cny_shibor_3m_flt_leg_def = create_floating_leg_definition(cny_ccy, shibor_3m, cal_cfets, [cal_cfets], freq, freq)
        self.cny_shibor_3m_swap_template = create_ir_vanilla_swap_template('cny_shibor_3m', 1,
                                                                           self.cny_shibor_3m_fixed_leg_def,
                                                                           self.cny_shibor_3m_flt_leg_def,
                                                                           'SPOTSTART')
        self.fr_007_fixings = create_time_series([datetime(2022, 3, 22), datetime(2022,3,23)], [0.026, 0.027])
        self.shibor_3m_fixings = create_time_series([datetime(2022, 3, 22), datetime(2022,3,23)], [0.031, 0.032])
        
        self.cny_cash_depo_template = create_depo_template('cny_cash', 'cny', 'CAL_CFETS')
        self.cny_shibor_3m_fra_tempalte = create_fra_template('cny_shibor_3m', 'shibor_3m', 'cny', 'CAL_CFETS', ['CAL_CFETS'], freq)
        
    def test_create_default_ibor_index(self):
        test = create_ibor_index('shibor_3m', '3m', 'CNY', ['CAL_CFETS'], 1)
        self.assertEqual(test, True)
        
    def test_create_ibor_index(self):
        test = create_ibor_index('shibor_3m', '3m', 'CNY', ['CAL_CFETS'], 1, 
                                 'ACT_365_FIXED', 'MODIFIED_FOLLOWING', 
                                 'INVALID_DATE_ROLL_CONVENTION', 
                                 'STANDARD_IBOR_INDEX')
        self.assertEqual(test, True)

    def test_create_leg_definition(self):
        expected = b'\x08\x01\x12\x03CNY\x18\x02(\x010\x018\x01@\x01jB\n\x14\x08\x01\x1a\x08CAL_FETS \x04(\x020\x018\x01\x12\x1c\x08\x03\x10\x01\x1a\x08CAL_FETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02'
        test = create_leg_definition('FIXED_LEG', 'cny', 'ACT_365_FIXED', '', 
                                     'NO_DISCOUNT', 'STANDARD', 'INVALID_NOTIONAL_EXCHANGE', False, False, False, 
                                     'CAL_FETS', 'QUARTERLY', 'MODIFIED_FOLLOWING', 'INITIAL', 'SHORT', 0, 'MODIFIED_FOLLOWING', 
                                     [], 'INVALID_FREQUENCY', 'INVALID_BUSINESS_DAY_CONVENTION', 'INVALID_DATE_GENERATION_MODE', 0)  
        self.assertEqual(test.SerializeToString(), expected)
    
    def test_create_fixed_leg_definition(self):
        expected = b'\x08\x01\x12\x03CNY\x18\x02(\x010\x018\x01@\x01jD\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02'
        test = create_fixed_leg_definition('cny', 'CAL_CFETS', 'QUARTERLY')
        self.assertEqual(test.SerializeToString(), expected)
        
    def test_create_floating_leg_definition(self):
        expected = b'\x08\x02\x12\x03CNY\x18\x01"\tSHIBOR_3M(\x010\x018\x01@\x01j`\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a(\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x040\x018\x01B\r\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01H\x02'
        test = create_floating_leg_definition('cny', 'shibor_3m', 'CAL_CFETS', ['CAL_CFETS'], 'QUARTERLY', 'QUARTERLY')
        self.assertEqual(test.SerializeToString(), expected)
    
    def test_create_depo_template(self):
        expected = b'\x08\xe9\x07\x12\x08CNY_CASH\x1a\x04\x08\x01\x10\x01"[\x08\x01\x12\x03CNY\x18\x01(\x010\x018\x01@\x01H\x05jF\n\x16\x08\x01\x1a\tCAL_CFETS \xe7\x07(\x020\x018\x02\x12\x1e\x08\x03\x10\x01\x1a\tCAL_CFETS \xe7\x07(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02(\x01'
        test = create_depo_template('cny_cash', 'cny', 'CAL_CFETS')        
        self.assertEqual(test.SerializeToString(), expected)
        
    def test_create_fra_template(self):
        expected =b'\x08\xd1\x0f\x12\rCNY_SHIBOR_3M\x1a\x02\x10\x01"\x82\x01\x08\x02\x12\x03CNY\x18\x01"\tSHIBOR_3M(\x020\x018\x01@\x01H\x05P\x01j`\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a(\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x040\x018\x01B\r\x08\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01H\x02(\x01'  
        test = create_fra_template('cny_shibor_3m', 'shibor_3m', 'cny', 'CAL_CFETS', ['CAL_CFETS'], 'QUARTERLY')
        
        self.assertEqual(test.SerializeToString(), expected)
        
    def test_create_ir_vanilla_swap_template(self):
        expected = b'\x08\xd2\x0f\x12\rCNY_SHIBOR_3M\x1a\x04\x08\x01\x10\x01"W\x08\x01\x12\x03CNY\x18\x02(\x010\x018\x01@\x01jD\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02"~\x08\x02\x12\x03CNY\x18\x01"\tSHIBOR_3M(\x010\x018\x01@\x01j`\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a(\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x040\x018\x01B\r\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01H\x02(\x01'
        test = create_ir_vanilla_swap_template('cny_shibor_3m', 1, 
                                               self.cny_shibor_3m_fixed_leg_def, 
                                               self.cny_shibor_3m_flt_leg_def,
                                               'SPOTSTART')            
        self.assertEqual(test.SerializeToString(), expected)
        
    def test_create_leg_fixings(self):
        expected = b'\n6\n\x06FR_007\x12,\n\x07\x08\xe6\x0f\x10\x03\x18\x16\n\x07\x08\xe6\x0f\x10\x03\x18\x17\x12\x18\x08\x02\x10\x01\x1a\x109\xb4\xc8v\xbe\x9f\x9a?\xd9\xce\xf7S\xe3\xa5\x9b? \x01\n9\n\tSHIBOR_3M\x12,\n\x07\x08\xe6\x0f\x10\x03\x18\x16\n\x07\x08\xe6\x0f\x10\x03\x18\x17\x12\x18\x08\x02\x10\x01\x1a\x10X9\xb4\xc8v\xbe\x9f?\xfc\xa9\xf1\xd2Mb\xa0? \x01'
        fixings = list()
        fixings.append(['fr_007', self.fr_007_fixings])
        fixings.append(['shibor_3m', self.shibor_3m_fixings])
        test = create_leg_fixings(fixings)
        self.assertEqual(test.SerializeToString(), expected)        
    
    def test_build_depo(self):
        expected = b'\n\x07\n\x00\x10\x01\x18\xe9\x07\x12\xb7\x01\n\x9b\x01\x12[\x08\x01\x12\x03CNY\x18\x01(\x010\x018\x01@\x01H\x05jF\n\x16\x08\x01\x1a\tCAL_CFETS \xe7\x07(\x020\x018\x02\x12\x1e\x08\x03\x10\x01\x1a\tCAL_CFETS \xe7\x07(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02\x1a<\n:\n\x07\x08\xe6\x0f\x10\x06\x18\x1b\x12&\n$\n\x07\x08\xe6\x0f\x10\x03\x18\x19\x12\x07\x08\xe6\x0f\x10\x03\x18\x19\x1a\x07\x08\xe6\x0f\x10\x06\x18\x1b)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\x11\x85\xebQ\xb8\x1e\x85\xd3?\x1a\x0e\n\x03CNY\x11\x00\x00\x00\x00`\xe3F\xc1'
        start = datetime(2022,3,25)
        maturity = datetime(2022,6,25)
        test = build_depo('PAY', 0.305, start, maturity, self.cny_cash_depo_template, 3000000.0)   
        #print('Depo:')
        #print(print_cash_flow_sched(test.legs[0].interest_rate_leg.cash_flow_schedule))
        self.assertEqual(test.SerializeToString(), expected) 
        
    def test_build_fra(self):
        expected = b'\n\x07\n\x00\x10\x01\x18\xd1\x0f\x12\xdf\x01\n\xc3\x01\x12\x82\x01\x08\x02\x12\x03CNY\x18\x01"\tSHIBOR_3M(\x020\x018\x01@\x01H\x05P\x01j`\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a(\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x040\x018\x01B\r\x08\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01H\x02\x1a<\n:\n\x07\x08\xe6\x0f\x10\t\x18\x1a\x12&\n$\n\x07\x08\xe6\x0f\x10\x06\x18\x18\x12\x07\x08\xe6\x0f\x10\x06\x18\x1b\x1a\x07\x08\xe6\x0f\x10\t\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\x11\x85\xebQ\xb8\x1e\x85\xd3\xbf\x1a\x0e\n\x03CNY\x11\x00\x00\x00\x00`\xe3F\xc1'
        start = datetime(2022,6,25)
        maturity = datetime(2022,9,25)
        leg_fixings = create_leg_fixings([['shibor_3m', self.shibor_3m_fixings]])
        test = build_fra('PAY', 0.305, start, maturity, self.cny_shibor_3m_fra_tempalte, leg_fixings, 3000000.0) 
        #print('FRA:')
        #print(print_cash_flow_sched(test.legs[0].interest_rate_leg.cash_flow_schedule))
        self.assertEqual(test.SerializeToString(), expected) 
        
    def test_build_ir_vanilla_swap(self):
        expected = b'\n\x07\n\x00\x10\x02\x18\xd2\x0f\x12\xc8\x06\n\xac\x06\x12W\x08\x01\x12\x03CNY\x18\x02(\x010\x018\x01@\x01jD\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a\x0c\x08\x03\x10\x018\x01B\x02\x10\x01H\x02\x1a\xd0\x05\n:\n\x07\x08\xe6\x0f\x10\x06\x18\x1b\x12&\n$\n\x07\x08\xe6\x0f\x10\x03\x18\x19\x12\x07\x08\xe6\x0f\x10\x03\x18\x19\x1a\x07\x08\xe6\x0f\x10\x06\x18\x1b)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe6\x0f\x10\t\x18\x1a\x12&\n$\n\x07\x08\xe6\x0f\x10\x06\x18\x1b\x12\x07\x08\xe6\x0f\x10\x06\x18\x1b\x1a\x07\x08\xe6\x0f\x10\t\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe6\x0f\x10\x0c\x18\x1a\x12&\n$\n\x07\x08\xe6\x0f\x10\t\x18\x1a\x12\x07\x08\xe6\x0f\x10\t\x18\x1a\x1a\x07\x08\xe6\x0f\x10\x0c\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe7\x0f\x10\x03\x18\x1b\x12&\n$\n\x07\x08\xe6\x0f\x10\x0c\x18\x1a\x12\x07\x08\xe6\x0f\x10\x0c\x18\x1a\x1a\x07\x08\xe7\x0f\x10\x03\x18\x1b)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe7\x0f\x10\x06\x18\x1a\x12&\n$\n\x07\x08\xe7\x0f\x10\x03\x18\x1b\x12\x07\x08\xe7\x0f\x10\x03\x18\x1b\x1a\x07\x08\xe7\x0f\x10\x06\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe7\x0f\x10\t\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\x06\x18\x1a\x12\x07\x08\xe7\x0f\x10\x06\x18\x1a\x1a\x07\x08\xe7\x0f\x10\t\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe7\x0f\x10\x0c\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\t\x18\x19\x12\x07\x08\xe7\x0f\x10\t\x18\x19\x1a\x07\x08\xe7\x0f\x10\x0c\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe8\x0f\x10\x03\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\x0c\x18\x19\x12\x07\x08\xe7\x0f\x10\x0c\x18\x19\x1a\x07\x08\xe8\x0f\x10\x03\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe8\x0f\x10\x06\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x03\x18\x19\x12\x07\x08\xe8\x0f\x10\x03\x18\x19\x1a\x07\x08\xe8\x0f\x10\x06\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe8\x0f\x10\t\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x06\x18\x19\x12\x07\x08\xe8\x0f\x10\x06\x18\x19\x1a\x07\x08\xe8\x0f\x10\t\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe8\x0f\x10\x0c\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\t\x18\x19\x12\x07\x08\xe8\x0f\x10\t\x18\x19\x1a\x07\x08\xe8\x0f\x10\x0c\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\n:\n\x07\x08\xe9\x0f\x10\x03\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x0c\x18\x19\x12\x07\x08\xe8\x0f\x10\x0c\x18\x19\x1a\x07\x08\xe9\x0f\x10\x03\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3F\xc1\x11\xecQ\xb8\x1e\x85\xeb\xa1?\x1a\x0e\n\x03CNY\x11\x00\x00\x00\x00`\xe3F\xc1\x12\xf1\x06\n\xde\x06\x08\x01\x12~\x08\x02\x12\x03CNY\x18\x01"\tSHIBOR_3M(\x010\x018\x01@\x01j`\n\x15\x08\x01\x1a\tCAL_CFETS \x04(\x020\x018\x02\x12\x1d\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x020\x028\x01B\x02\x10\x01H\x02\x1a(\x08\x03\x10\x01\x1a\tCAL_CFETS \x04(\x040\x018\x01B\r\x08\xfe\xff\xff\xff\xff\xff\xff\xff\xff\x01\x10\x01H\x02\x1a\xd9\x05\nC\n\x07\x08\xe6\x0f\x10\x06\x18\x1b\x12/\n-\n\x07\x08\xe6\x0f\x10\x03\x18\x17\x12\x07\x08\xe6\x0f\x10\x03\x18\x19\x1a\x07\x08\xe6\x0f\x10\x06\x18\x1b!\xfc\xa9\xf1\xd2Mb\xa0?)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe6\x0f\x10\t\x18\x1a\x12&\n$\n\x07\x08\xe6\x0f\x10\x06\x18\x17\x12\x07\x08\xe6\x0f\x10\x06\x18\x1b\x1a\x07\x08\xe6\x0f\x10\t\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe6\x0f\x10\x0c\x18\x1a\x12&\n$\n\x07\x08\xe6\x0f\x10\t\x18\x16\x12\x07\x08\xe6\x0f\x10\t\x18\x1a\x1a\x07\x08\xe6\x0f\x10\x0c\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe7\x0f\x10\x03\x18\x1b\x12&\n$\n\x07\x08\xe6\x0f\x10\x0c\x18\x16\x12\x07\x08\xe6\x0f\x10\x0c\x18\x1a\x1a\x07\x08\xe7\x0f\x10\x03\x18\x1b)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe7\x0f\x10\x06\x18\x1a\x12&\n$\n\x07\x08\xe7\x0f\x10\x03\x18\x17\x12\x07\x08\xe7\x0f\x10\x03\x18\x1b\x1a\x07\x08\xe7\x0f\x10\x06\x18\x1a)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe7\x0f\x10\t\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\x06\x18\x16\x12\x07\x08\xe7\x0f\x10\x06\x18\x1a\x1a\x07\x08\xe7\x0f\x10\t\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe7\x0f\x10\x0c\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\t\x18\x15\x12\x07\x08\xe7\x0f\x10\t\x18\x19\x1a\x07\x08\xe7\x0f\x10\x0c\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe8\x0f\x10\x03\x18\x19\x12&\n$\n\x07\x08\xe7\x0f\x10\x0c\x18\x15\x12\x07\x08\xe7\x0f\x10\x0c\x18\x19\x1a\x07\x08\xe8\x0f\x10\x03\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe8\x0f\x10\x06\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x03\x18\x15\x12\x07\x08\xe8\x0f\x10\x03\x18\x19\x1a\x07\x08\xe8\x0f\x10\x06\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe8\x0f\x10\t\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x06\x18\x15\x12\x07\x08\xe8\x0f\x10\x06\x18\x19\x1a\x07\x08\xe8\x0f\x10\t\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe8\x0f\x10\x0c\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\t\x18\x17\x12\x07\x08\xe8\x0f\x10\t\x18\x19\x1a\x07\x08\xe8\x0f\x10\x0c\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\n:\n\x07\x08\xe9\x0f\x10\x03\x18\x19\x12&\n$\n\x07\x08\xe8\x0f\x10\x0c\x18\x17\x12\x07\x08\xe8\x0f\x10\x0c\x18\x19\x1a\x07\x08\xe9\x0f\x10\x03\x18\x19)\x00\x00\x00\x00\x00\x00\xf0?\x19\x00\x00\x00\x00`\xe3FA\x1a\x0e\n\x03CNY\x11\x00\x00\x00\x00`\xe3FA'
        leg_fixings = create_leg_fixings([['shibor_3m', self.shibor_3m_fixings]])
        test = build_ir_vanilla_instrument('PAY', 0.035, 0.0, datetime(2022,3,25), datetime(2025,3,25), self.cny_shibor_3m_swap_template, 3000000.0, leg_fixings)
        #print('IR Vanilla Swap:')
        #print('Leg 1')
        #print(print_cash_flow_sched(test.legs[0].interest_rate_leg.cash_flow_schedule))
        #print('Leg 2')
        #print(print_cash_flow_sched(test.legs[1].interest_rate_leg.cash_flow_schedule))
        self.assertEqual(test.SerializeToString(), expected)
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestIrMarket)
    unittest.TextTestRunner(verbosity=2).run(suite)