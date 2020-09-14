import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def bonus_calculation(order):
    df = pd.DataFrame(order)

    g = df.groupby(['offerName', 'status'])[['basePoints', 'bonusPoints']].sum().rename(
        columns={'basePoints': 'Total base points', 'bonusPoints': 'Total bonus points'})

    j = df.groupby(['offerName', 'status'])['memberId'].nunique().to_frame('Unique members')

    return pd.merge(g, j, left_index=True, right_index=True).reset_index()

