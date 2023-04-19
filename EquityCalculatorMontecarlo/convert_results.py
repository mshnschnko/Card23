#import cppimport
import EquityCalculatorMontecarlo.test_montecarlo

table_left = 0.45
table_right = 0.80
table_bottom = 0.5
table_top = 0.40

card_width = 0.052121
card_height = 0.130595


# convert yolo classes in calculator format
def get_class_name(class_num):
    if class_num== '0':
        return 'back'
    if class_num == '1':
        return 'D'
    if class_num == '2':
        return 'H'
    if class_num == '3':
        return 'S'
    if class_num == '4':
        return 'C'
    if class_num == '5':
        return '2'
    if class_num == '6':
        return '3'
    if class_num == '7':
        return '4'
    if class_num == '8':
        return '5'
    if class_num == '9':
        return '6'
    if class_num == '10':
        return '7'
    if class_num == '11':
        return '8'
    if class_num == '12':
        return '9'
    if class_num == '13':
        return 'T'
    if class_num == '14':
        return 'J'
    if class_num == '15':
        return 'Q'
    if class_num == '16':
        return 'K'
    if class_num == '17':
        return 'A'
    if class_num == '18':
        return ''

# define is class a value or a suit
def is_value(class_name):
    if 'S' == class_name or 'C' == class_name or 'D' == class_name or 'H' == class_name:
        return False
    else:
        return True

def create_card_from_classes(card_classes_str):
    card = ''
    val, suit = '', ''
    card_classes = []
    for el in card_classes_str:
        el = el.split()
        card_classes.append(el)
    sorted(card_classes, key=lambda x: float(x[-1]), reverse=True)
    card_classes = [get_class_name(el[0]) for el in card_classes]
    for el in card_classes:
        if is_value(el) and val == '':
            val = el
        elif not is_value(el) and suit == '':
            suit = el
        if val != '' and suit != '':
            break

    return val+suit

def is_one_card_on_table(x, y, x_next, y_next):
    return abs(x_next - x) < card_width * 2 / 3 and abs(y_next - y) < card_height * 2 / 3

def is_one_card_on_hand(x, y, x_next, y_next):
    return abs(x_next - x) < card_width / 4 and abs(y_next - y) < card_height * 2 / 3

def is_one_player(x, y, x_next, y_next):
    return abs(x_next - x) < card_width and abs(y_next - y) < card_height / 4


def is_on_table(y, y_centre):
    return y > y_centre * 0.5

def is_hand_card(y):
    return y > 0.6

def is_player_back(x, y):
    return x > table_right or x < table_left or y > table_bottom or y < table_top


# def define_cards(cards_list):
#     table_list = []
#     hand_list = []
#     amount_players = 0
#     for i in range(len(cards_list)):
#         cur_card_table = []
#         cur_card_hand = []
#         cur_players = []
#         class_name = cards_list[i].split()[0]
#         x, y = cards_list[i].split()[1], cards_list[i].split()[2]
#         # если это рубашка то добавить в игрока и потом проверить, что она не на столе и найти рубашки того же игрока
#         if get_class_name(class_name) == 'back' and is_player_back(float(x), float(y)):
#             cur_players.append(cards_list[i])
#         for j in range(i+1, len(cards_list)):
#             class_name_next = cards_list[j].split()[0]
#             x_next, y_next = float(cards_list[j].split()[1]), float(cards_list[j].split()[2])
#             # если следующая карта (одна из) - рубашка, то проверить, что это не на столе и что это один игрок
#             if get_class_name(class_name_next) == 'back' and is_player_back(float(x_next), float(y_next))\
#                     and is_one_player(float(x), float(y), float(x_next), float(y_next)):
#                 cur_players.append(cards_list[j])
#
#                 cards_list[j] = cards_list[j].replace(class_name_next, "18")
#                 # amount_players += 1
#             if is_hand_card(float(y)) and is_one_card_on_hand(float(x), float(y), float(x_next), float(y_next)):
#                 cur_card_hand.append(cards_list[j])
#                 cards_list[j] = cards_list[j].replace(class_name_next, "18")
#             elif not is_hand_card(float(y)) and not is_player_back(float(x), float(y)) and is_one_card_on_table(float(x), float(y), float(x_next), float(y_next)):
#                 cur_card_table.append(cards_list[j])
#                 cards_list[j] = cards_list[j].replace(class_name_next, "18")
#         if is_hand_card(float(y)) and len(cur_card_hand) >= 1:
#             cur_card_hand.append(class_name)
#             card = create_card_from_classes(cur_card_hand)
#             if card != '':
#                 hand_list.append(card)
#         if len(cur_players) > 0 :
#             amount_players += 1
#         elif (not is_hand_card(float(y)) ) and (len(cur_card_table) >= 2):
#             cur_card_table.append(class_name)
#             card = create_card_from_classes(cur_card_table)
#             if card != "":
#                 table_list.append(card)
#     print(table_list)
#     print(hand_list)
#     print(amount_players)
#     return table_list, hand_list, amount_players
#


def define_cards(cards_list):
    table_list = []
    hand_list = []
    amount_players = 0
    for i in range(len(cards_list)):
        cur_card_table = []
        cur_card_hand = []
        cur_players = []
        class_name = cards_list[i].split()[0]
        x, y = cards_list[i].split()[1], cards_list[i].split()[2]
        # если это рубашка то добавить в игрока и потом проверить, что она не на столе и найти рубашки того же игрока
        if get_class_name(class_name) == 'back' and is_player_back(float(x), float(y)):
            cur_players.append(cards_list[i])
        for j in range(i+1, len(cards_list)):
            class_name_next = cards_list[j].split()[0]
            x_next, y_next = float(cards_list[j].split()[1]), float(cards_list[j].split()[2])
            # если следующая карта (одна из) - рубашка, то проверить, что это не на столе и что это один игрок
            if get_class_name(class_name_next) == 'back' and is_player_back(float(x_next), float(y_next))\
                    and is_one_player(float(x), float(y), float(x_next), float(y_next)):
                cur_players.append(cards_list[j])

                cards_list[j] = cards_list[j].replace(class_name_next, "18")
                # amount_players += 1
            if is_hand_card(float(y)) and is_one_card_on_hand(float(x), float(y), float(x_next), float(y_next)):
                cur_card_hand.append(cards_list[j])
                cards_list[j] = cards_list[j].replace(class_name_next, "18")
            elif not is_hand_card(float(y)) and not is_player_back(float(x), float(y)) and is_one_card_on_table(float(x), float(y), float(x_next), float(y_next)):
                cur_card_table.append(cards_list[j])
                cards_list[j] = cards_list[j].replace(class_name_next, "18")
        if is_hand_card(float(y)) and len(cur_card_hand) >= 1:
            cur_card_hand.append(class_name)
            card = create_card_from_classes(cur_card_hand)
            if card != '':
                hand_list.append(card)
        if len(cur_players) > 0 :
            amount_players += 1
        elif (not is_hand_card(float(y)) ) and (len(cur_card_table) >= 2):
            cur_card_table.append(class_name)
            card = create_card_from_classes(cur_card_table)
            if card != "":
                table_list.append(card)
    print(table_list)
    print(hand_list)
    print(amount_players)
    return table_list, hand_list, amount_players


def convert(file_path):
    with open(file_path, "r") as f:
        str = f.read().split('\n')
        if "" in str:
            del str[str.index("")]
    table_list, hand_list, players_amount = define_cards(str)
    #_runner(hand_list, table_list, 9, )
    if len(hand_list) != 0:
        EquityCalculatorMontecarlo.test_montecarlo._runner(set(hand_list), set(table_list), 9)
    else:
        print("No cards on hand")

def main():
    with open('../dataset/test_for_calculator/label.txt', "r") as f:
        str = f.read().split('\n')
        if "" in str:
            del str[str.index("")]
    table_list, hand_list, players = define_cards(str)
    #_runner(hand_list, table_list, 9, )
    EquityCalculatorMontecarlo.test_montecarlo._runner(set(hand_list), set(table_list), 9)

if __name__ == "__main__":
    main()