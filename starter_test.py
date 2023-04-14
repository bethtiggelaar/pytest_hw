# test_friend.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov

# test_oop_loan_pmt.py

# test_oop_loan_pmt.py

import pytest
from oop_loan_pmt import Loan, collectLoanDetails
 
def test_getDiscountFactor():
    loan = Loan(100000, 30, 0.06)
    loan.calculateDiscountFactor()
    assert loan.getDiscountFactor() == pytest.approx(166.7916, 0.01)
 
def test_calculateLoanPmt():
    loan = Loan(100000, 30, 0.06)
    loan.calculateLoanPmt()
    assert loan.getLoanPmt() == pytest.approx(599.55, 0.01)
 
def test_collectLoanDetails(monkeypatch):
    input_values = [100000, 30, 0.06]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr('builtins.input', mock_input)
    loan = collectLoanDetails()
    assert loan.loanAmount == 100000
    assert loan.numberOfPmts == 360
    assert loan.periodicIntRate == pytest.approx(0.005, 0.01)
    assert loan.annualRate == 0.06