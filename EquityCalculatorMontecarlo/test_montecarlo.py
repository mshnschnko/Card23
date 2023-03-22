"""Test numpy based equity calculator"""

import time
import cppimport
import pytest
import tkinter as tk
from tkinter.ttk import Button

start_comp = time.perf_counter()
calculator = cppimport.imp("Scoring")
finish_comp = time.perf_counter()

def _runner(my_cards, cards_on_table, players, expected_result):
    """Montecarlo test"""
    if len(cards_on_table) == 0:
        cards_on_table = {'\0'}
    equity = calculator.montecarlo(my_cards, cards_on_table, players, 10000)
    return equity
    # assert equity == pytest.approx(expected_result, abs=1)


def test_montecarlo1():
    """Montecarlo test"""
    my_cards = {'3H', '3S'}
    cards_on_table = {'8S', '4S', 'QH', '8C', '4H'}
    expected_results = 40.2
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo2():
    """Montecarlo test"""
    my_cards = {'8H', '8D'}
    cards_on_table = {'QH', '7H', '9H', 'JH', 'TH'}
    expected_results = 95.6
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo3():
    """Montecarlo test"""
    my_cards = {'AS', 'KS'}
    cards_on_table = {}
    expected_results = 49.9 + 1.9
    players = 3
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo4():
    """Montecarlo test"""
    my_cards = {'AS', 'KS'}
    cards_on_table = {}
    expected_results = 66.1 + 1.6
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo5():
    """Montecarlo test"""
    my_cards = {'8S', 'TS'}
    cards_on_table = {'8H', 'KS', '9S', 'TH', 'KH'}
    expected_results = 71.5 + 5.9
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo6():
    """Montecarlo test"""
    my_cards = {'8S', 'TS'}
    cards_on_table = {'2S', '3S', '4S', 'KS', 'AS'}
    expected_results = 87
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo7():
    """Montecarlo test"""
    my_cards = {'8S', '2S'}
    cards_on_table = {'5S', '3S', '4S', 'KS', 'AS'}
    expected_results = 100
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo8():
    """Montecarlo test"""
    my_cards = {'8S', 'TS'}
    cards_on_table = {}
    expected_results = 22.6 + 2.9
    players = 5
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo8b():
    """Montecarlo test"""
    my_cards = {'2C', 'QS'}
    cards_on_table = {}
    expected_results = 49.6  # 45 win and 4 tie
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo9():
    """Montecarlo test"""
    my_cards = {'7H', '7S'}
    cards_on_table = {'7C', '8C', '8S', 'AC', 'AH'}
    expected_results = 83
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo10():
    """Montecarlo test"""
    my_cards = {'3S', 'QH'}
    cards_on_table = {'2C', '5H', '7C'}
    expected_results = 30.9 + 2.2
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo11():
    """Montecarlo test"""
    my_cards = {'5C', 'JS'}
    cards_on_table = {}
    expected_results = 23
    players = 4
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo12():
    """Montecarlo test"""
    my_cards = {'TC', 'TH'}
    cards_on_table = {'4D', 'QD', 'KC'}
    expected_results = 66.7 + 0.38
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo13():
    """Montecarlo test"""
    my_cards = {'JH', 'QS'}
    cards_on_table = {'5C', 'JD', 'AS', 'KS', 'QD'}
    expected_results = 77
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo14():
    """Montecarlo test"""
    my_cards = {'2H', '8S'}
    cards_on_table = {'AC', 'AD', 'AS', 'KS', 'KD'}
    expected_results = 95
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo15():
    """Montecarlo test"""
    my_cards = {'KD', 'KS'}
    cards_on_table = {'4D', '6S', '9C', '9S', 'TC'}
    expected_results = 88
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo16():
    """Montecarlo test"""
    my_cards = {'5H', 'KD'}
    cards_on_table = {'KH', 'JS', '2C', 'QS'}
    expected_results = 75.6 + 3.6
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo17():
    """Montecarlo test"""
    my_cards = {'JD', 'JS'}
    cards_on_table = {'8C', 'TC', 'JC', '5H', 'QC'}
    expected_results = 26.1
    players = 3
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards


def test_montecarlo19():
    """Montecarlo test"""
    my_cards = {'TD', '7D'}
    cards_on_table = {'8D', 'QD', '7C', '5D', '6D'}
    expected_results = 87
    players = 2
    return _runner(my_cards, cards_on_table, players, expected_results), my_cards




root = tk.Tk()
root.geometry("250x100")
root.attributes('-topmost',True)
cards_label = tk.Label(root, text= f"Yout cards: ",font=('Helvetica bold', 12))
cards_label.pack()
eq_label = tk.Label(root, text= f"Equity = ",font=('Helvetica bold', 12))
eq_label.pack()
rec_label = tk.Label(root, text= f"Recomendation: ",font=('Helvetica bold', 12))
rec_label.pack()

tests = [test_montecarlo1, test_montecarlo2, test_montecarlo3, test_montecarlo4,
         test_montecarlo5, test_montecarlo6, test_montecarlo7, test_montecarlo8, test_montecarlo10]
i = 0

def get_rec():
    global i
    if i < len(tests):
        eq, my_cards = tests[i]()
        eq_label.configure(text="Equity =  {0:.2f}%".format(eq))
        cards_label.configure(text=f"Your cards: {my_cards}")
        rec = str()
        if eq < 15:
            rec = "fold"
        elif eq < 60:
            rec = "call or check"
        elif eq < 95:
            rec = "raise or bet"
        else:
            rec = "all-in"
        rec_label.configure(text="Recomendation: " + rec)
        i += 1
        root.after(1000, get_rec)



if __name__ == "__main__":
    # root = tk.Tk()
    # root.geometry("250x100")
    # root.attributes('-topmost',True)
    # cards_label = tk.Label(root, text= f"Yout cards: ",font=('Helvetica bold', 12))
    # cards_label.pack()
    # eq_label = tk.Label(root, text= f"Equity = ",font=('Helvetica bold', 12))
    # eq_label.pack()
    # start_button = Button(root, text="start", command=lambda: clicked(eq_label, cards_label, start_button))
    # start_button.pack()
    root.after(1000, get_rec)
    root.mainloop()