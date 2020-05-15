
import numpy as np
import pandas as pd
import operator

def roll():
    return np.random.randint(1,21,1)[0]

def roll_with_advantage():
    return max(np.random.randint(1,21,2))

def roll_with_disadvantage():
    return min(np.random.randint(1,21,2))

def advantage_of_disadvantage():
    return max(roll_with_disadvantage(), roll_with_disadvantage())

def disadvantage_of_advantage():
    return min(roll_with_advantage(), roll_with_advantage())

def which_strategy_is_best():

    data = []

    for i in range(1,10000):
        data.append([i,roll(),roll_with_advantage(),roll_with_disadvantage(),advantage_of_disadvantage(),disadvantage_of_advantage()])

    data = pd.DataFrame(data, columns = ['turn','normal','advantage','disadvantage','advantage_of_disadvantage','disadvantage_of_advantage'])

    data = data.merge(data.iloc[:,1:].cumsum().divide(data.turn,axis=0), how='outer', left_index=True, right_index=True,suffixes=['','_mean'])

    results = data.iloc[:,9:].tail(1).to_dict(orient='records')[0]

    winning_strat = max(results.items(), key=operator.itemgetter(1))[0]

    print("The best strateghy is {} with an expected value of {}".format(winning_strat,results[winning_strat]))

if __name__ == '__main__':
    
    which_strategy_is_best()
