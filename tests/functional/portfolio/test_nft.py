import ape


def test_no_portfolio(portfolio, accounts):
    a = accounts[0]
    assert portfolio.balanceOf(a) == 0
    with ape.reverts():
        portfolio.estimatedValue(0)
