
table_left = 0.33
table_right = 0.90
table_bottom = 0.55
table_top = 0.40

card_width = 0.052121
card_height = 0.130595

# convert yolo classes in calculator format
def get_class_name(class_num):
    if class_num== '0':
        return 'card'
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

# define is class a value or a suit
def is_value(class_name):
    if 'S' == class_name or 'C' == class_name or 'D' == class_name or 'H' == class_name:
        return False
    else:
        return True

# argument: card_classes is a list of classes(values and suits) inside  one card.
# return: one card for calculator
def create_card_from_classes(card_classes):
    card = ''
    unique_classes = list(set(card_classes))
    class_names = [get_class_name(str(el)) for el in unique_classes]
    if len(unique_classes) > 2:
        print("more than two classes for one card. Bad recognition")
    if is_value(class_names[0]):
        card += class_names[0] + class_names[1]
    else:
        card += class_names[1] + class_names[0]
    print(card)

# argument: get a list of all cards (yolo strings) which are exactly on table
# return: list of cards in calculator format
def define_cards_on_table(card_list):
    table_list = []
    for i in range(len(card_list)):
        cur_card_list = []
        class_name = card_list[i].split()[0]
        if get_class_name(class_name) == 'card':
            continue
        x, y = float(card_list[i].split()[1]), float(card_list[i].split()[2])
        cur_card_list.append(class_name)
        for j in range(i+1, len(card_list)):
            class_name_next = card_list[j].split()[0]
            x_next, y_next = float(card_list[j].split()[1]), float(card_list[j].split()[2])
            if abs(x_next - x) < card_width * 2 / 3 and abs(y_next - y) < card_height * 2 / 3:
                cur_card_list.append(class_name_next)
                card_list[j] = card_list[j].replace(class_name_next, "0")
        table_list.append(create_card_from_classes(cur_card_list))
    return table_list

# argument: get a list of strings in yolo format, which contain info about classes in one file(frame)
# return: two lists (cards on table and cards in hand)
def get_cards(card_list):
    cards_on_table = []
    cards_on_hand = []
    for el in card_list:
        class_name = el.split()[0]
        if get_class_name(class_name) == 'card':
            continue
        x, y = el.split()[1], el.split()[2]
        if table_left < float(x) < table_right and table_top < float(y) < table_bottom:
            cards_on_table.append(el)
        else:
            cards_on_hand.append(el)
    return define_cards_on_table(cards_on_table)

def main():
    with open('./dataset/test_for_convertation/clubs3_clubs4_580_329.txt', "r") as f:
        str = f.read().split('\n')
        if "" in str:
            del str[str.index("")]
    print(str)
    get_cards(str)

if __name__ == "__main__":
    main()