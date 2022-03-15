"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import sorting_hats, financial, financial_aid, summary_fee 

import mock
import builtins

def test_sorting_hats():
    assert callable(sorting_hats)
    
    # test whether input will return proper output 
    with mock.patch.object(builtins, 'input', lambda _: 'sdf'):

        # execute function and specify something that asserts True
        output_houses = sorting_hats()
        assert output_houses == 'As a wizard, be careful with your spells. '
        
    with mock.patch.object(builtins, 'input', lambda _: 'Bravery'):

        output_houses = sorting_hats()
        assert output_houses == 'Congratuations! You are in House Gryffindor!'
        
def test_financial():
    assert callable(financial)
    
    with mock.patch.object(builtins, 'input', lambda _: 10000):

        chat_2, fee = financial()
        assert fee == 20000
        assert chat_2 == False

def test_financial_aid():
    assert callable(financial_aid)
             
def test_summary_fee():
    assert callable(summary_fee)

                 
    