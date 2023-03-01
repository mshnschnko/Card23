import cppimport
import time

mc = cppimport.imp("Scoring")


def _run(my_cards, cards_on_table, players):
    equity = mc.montecarlo(my_cards, cards_on_table, players, 10000)
    # print(equity)
    return equity

def avg_eq(my_cards, cards_on_table, players):
    max_eq = 0
    min_eq = 100
    avg = 0
    for i in range(100):
        eq = _run(my_cards, cards_on_table, players)
        avg += eq
        if eq > max_eq:
            max_eq = eq
        if eq < min_eq:
            min_eq = eq
    avg = avg / 100
    print(f"max equity = {max_eq}\nmin equity = {min_eq}\ndifference = {max_eq - min_eq}\naverage = {avg}")


if __name__ == "__main__":
    tic = time.perf_counter()
    my_cards = {'3H', '3S'}
    cards_on_table = {'8S', '4S', 'QH', '8C', '4H'}
    players = 2
    avg_eq(my_cards, cards_on_table, players)
    # _run(my_cards, cards_on_table, players)
    print(f"общее время: {time.perf_counter() - tic:0.4f}")
