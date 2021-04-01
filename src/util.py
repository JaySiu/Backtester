def turnover(pos):
    return pos.fillna(0).diff(1).abs()

def t_cost(to, cost):
    return to * (cost/10000)

def daily(df):
    return df.sum(axis=1)
