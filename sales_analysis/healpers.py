def cal_total(q, p):
    """ Calculate total for a single item"""
    return q*p

def format_currency(amount):
    """ Format number as currency"""
    return f"${amount:,.2f}"