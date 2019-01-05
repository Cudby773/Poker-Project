from random import randint


def table_cards(cards_to_avoid):
    numbers = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(5):
        numbers[i][0] = randint(1, 13)
        numbers[i][1] = randint(1, 4)
    for i in range(4):
        for j in range(i + 1, 5):
            while numbers[i][0] == numbers[j][0] and numbers[i][1] == numbers[j][1]:
                numbers[j][0] = randint(1, 13)
                numbers[j][1] = randint(1, 4)
    for i in range(4):
        for j in range(2):
            while numbers[i][0] == cards_to_avoid[j][0] and numbers[i][1] == cards_to_avoid[j][1]:
                numbers[i][1] = randint(1, 13)
                numbers[i][1] = randint(1, 4)
    return numbers


def sort_hand_numbers(hand):
    sorted_hand = sorted(hand)
    return sorted_hand


def aces_high_sort(num_sorted_hand):
    while num_sorted_hand[0][0] == 1:
        save_suit = num_sorted_hand[0][1]
        num_sorted_hand.remove(num_sorted_hand[0])
        num_sorted_hand.append([14, save_suit])
    return num_sorted_hand


def split_hand_suits(hand):
    hand.sort(key=lambda row: row[1])
    clubs, diamonds, hearts, spades = list(), [], [], []
    #
    for i in range(len(hand)):
        if hand[i][1] == 1:
            clubs = clubs + hand[i]
    nums = [clubs[2 * i] for i in range(len(clubs) / 2)]
    ones = [1] * len(nums)
    clubs = [nums, ones]
    clubs = sort_hand_numbers(clubs)
    #
    for i in range(len(hand)):
        if hand[i][1] == 2:
            diamonds = diamonds + hand[i]
    nums = [diamonds[2 * i] for i in range(len(diamonds) / 2)]
    twos = [2] * len(nums)
    diamonds = [nums, twos]
    diamonds = sort_hand_numbers(diamonds)
    #
    for i in range(len(hand)):
        if hand[i][1] == 3:
            hearts = hearts + hand[i]
    nums = [hearts[2 * i] for i in range(len(hearts) / 2)]
    threes = [3] * len(nums)
    hearts = [nums, threes]
    hearts = sort_hand_numbers(hearts)
    #
    for i in range(len(hand)):
        if hand[i][1] == 4:
            spades = spades + hand[i]
    nums = [spades[2 * i] for i in range(len(spades) / 2)]
    fours = [4] * len(nums)
    spades = [nums, fours]
    spades = sort_hand_numbers(spades)
    #
    return clubs, diamonds, hearts, spades


def straight_flush_test(suit_sorted_hand):
    for i in range(len(suit_sorted_hand)):
        if len(suit_sorted_hand[i]) >= 5:
            for j in range(len(suit_sorted_hand[i]) - 1, 3, -1):
                if suit_sorted_hand[i][j][0] == suit_sorted_hand[i][j - 1][0] + 1 and suit_sorted_hand[i][j - 1][0] == \
                        suit_sorted_hand[i][
                            j - 2][0] + 1 \
                        and suit_sorted_hand[i][j - 2][0] == suit_sorted_hand[i][j - 3][0] + 1 and \
                        suit_sorted_hand[i][j - 3][0] == \
                        suit_sorted_hand[i][j - 4][0] + 1:
                    return suit_sorted_hand[i][j][0]
                elif suit_sorted_hand[i][0][0] == 1 and suit_sorted_hand[i][len(suit_sorted_hand[i]) - 4][0] == 10 and \
                        suit_sorted_hand[i][len(suit_sorted_hand[i]) - 3][0] == 11 \
                        and suit_sorted_hand[i][len(suit_sorted_hand[i]) - 2][0] == 12 and \
                        suit_sorted_hand[i][len(suit_sorted_hand[i]) - 1][0] == 13:
                    return 14
                else:
                    print "Error in straight_flush_test"
                    return 0
    return 0


def four_of_a_kind_test(aces_high_sorted_hand):
    for i in range(len(aces_high_sorted_hand) - 3):
        if aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i + 1][0] and aces_high_sorted_hand[i][0] == \
                aces_high_sorted_hand[i + 2][0] \
                and aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i + 3][0]:
            if i <= 2:
                score = 100 * aces_high_sorted_hand[i][0] + aces_high_sorted_hand[len(aces_high_sorted_hand) - 1][0]
                return score
            elif i == 3:
                score = 100 * aces_high_sorted_hand[i][0] + aces_high_sorted_hand[i - 1][0]
                return score
            else:
                print i
                print "Error in four_of_a_kind test"
                return 0
    return 0


def full_house_test(aces_high_sorted_hand):
    for i in range(len(aces_high_sorted_hand) - 1, 1, -1):
        for j in range(len(aces_high_sorted_hand) - 1, 0, -1):
            if aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i - 1][0] and \
                    aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i - 2][0]:
                if aces_high_sorted_hand[j][0] == aces_high_sorted_hand[j - 1][0] and (j <= i - 3 or j >= i + 1):
                    if aces_high_sorted_hand[i][0] != 1 and aces_high_sorted_hand[j][0] != 1:
                        score = 100 * aces_high_sorted_hand[i][0] + aces_high_sorted_hand[j][0]
                        return score
    return 0


def flush_test(suit_sorted_hand):
    for i in range(len(suit_sorted_hand)):
        if len(suit_sorted_hand[i]) >= 5:
            n = len(suit_sorted_hand[i])
            if suit_sorted_hand[i][0][0] != 1:
                score = suit_sorted_hand[i][n - 5][0] + 100 * suit_sorted_hand[i][n - 4][0] + 10000 * \
                        suit_sorted_hand[i][n - 3][0] + 1000000 * suit_sorted_hand[i][n - 2][0] + \
                        100000000 * suit_sorted_hand[i][n - 1][0]
                return score
            elif suit_sorted_hand[i][0][0] == 1:
                score = suit_sorted_hand[i][n - 4][0] + 100 * suit_sorted_hand[i][n - 3][0] + 10000 * \
                        suit_sorted_hand[i][n - 2][0] + 1000000 * suit_sorted_hand[i][n - 1][0] + \
                        100000000 * 14
                return score
    return 0


def straight_test(num_sorted_hand):
    i = 0
    while i in range(len(num_sorted_hand) - 1):
        if num_sorted_hand[i][0] == num_sorted_hand[i + 1][0]:
            num_sorted_hand.remove(num_sorted_hand[i])
        else:
            i += 1
    for i in range(len(num_sorted_hand) - 1, 3, -1):
        n = len(num_sorted_hand)
        if num_sorted_hand[0][0] == 1 and num_sorted_hand[n - 1][0] == 13 and num_sorted_hand[n - 2][0] == 12 \
                and num_sorted_hand[n - 3][0] == 11 and num_sorted_hand[n - 4][0] == 10:
            return 14
        elif num_sorted_hand[i][0] == num_sorted_hand[i - 1][0] + 1 and num_sorted_hand[i - 1][0] == \
                num_sorted_hand[i - 2][0] + 1 \
                and num_sorted_hand[i - 2][0] == num_sorted_hand[i - 3][0] + 1 and num_sorted_hand[i - 3][0] == \
                num_sorted_hand[i - 4][0] + 1:
            return num_sorted_hand[i][0]
    return 0


def three_of_a_kind_test(aces_high_sorted_hand):
    for i in range(len(aces_high_sorted_hand) - 1, 1, -1):
        if aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i - 1][0] and aces_high_sorted_hand[i][0] == \
                aces_high_sorted_hand[i - 2][0]:
            triplets = aces_high_sorted_hand[i][0]
            if i == len(aces_high_sorted_hand) - 1:
                kicker = 100 * aces_high_sorted_hand[i - 3][0] + aces_high_sorted_hand[i - 4][0]
            elif i == len(aces_high_sorted_hand) - 2:
                kicker = 100 * aces_high_sorted_hand[i + 1][0] + aces_high_sorted_hand[i - 3][0]
            else:
                kicker = 100 * aces_high_sorted_hand[len(aces_high_sorted_hand) - 1][0] + \
                         aces_high_sorted_hand[len(aces_high_sorted_hand) - 2][0]
            score = 10000 * triplets + kicker
            return score
    return 0


def two_pair_test(aces_high_sorted_hand):
    n = len(aces_high_sorted_hand)
    for i in range(len(aces_high_sorted_hand) - 1, 2, -1):
        for j in range(i - 2, 0, -1):
            if aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i - 1][0]:
                if aces_high_sorted_hand[j][0] == aces_high_sorted_hand[j - 1][0]:
                    score = 10000 * aces_high_sorted_hand[i][0] + aces_high_sorted_hand[j][0] * 100
                    if i == n - 1:
                        if j == n - 3:
                            score += aces_high_sorted_hand[n - 5][0]
                        else:
                            score += aces_high_sorted_hand[n - 3][0]
                    else:
                        score += aces_high_sorted_hand[n - 1][0]
                    return score
    return 0


def pair_test(aces_high_sorted_hand):
    for i in range(len(aces_high_sorted_hand) - 1, 1, -1):
        if aces_high_sorted_hand[i][0] == aces_high_sorted_hand[i - 1][0]:
            score = aces_high_sorted_hand[i][0] * (10 ** 6)
            n = len(aces_high_sorted_hand)
            if i == n - 1:
                score += aces_high_sorted_hand[n - 3][0] * 10000 + aces_high_sorted_hand[n - 4][0] * 100 + \
                         aces_high_sorted_hand[n - 5][0]
            elif i == n - 2:
                score += aces_high_sorted_hand[n - 1][0] * 10000 + aces_high_sorted_hand[n - 4][0] * 100 + \
                         aces_high_sorted_hand[n - 5][0]
            elif i == n - 3:
                score += aces_high_sorted_hand[n - 1][0] * 10000 + aces_high_sorted_hand[n - 2][0] * 100 + \
                         aces_high_sorted_hand[n - 5][0]
            else:
                score += aces_high_sorted_hand[n - 1][0] * 10000 + aces_high_sorted_hand[n - 2][0] * 100 + \
                         aces_high_sorted_hand[n - 3][0]
            return score
    return 0


def high_card_test(aces_high_sorted_hand):
    n = len(aces_high_sorted_hand)
    score = 0
    for i in range(1, 6):
        score += aces_high_sorted_hand[n - i][0] * 100 ** (5 - i)
    return score


def hand_score(hand):
    num_sorted_hand = sort_hand_numbers(hand)
    suit_sorted_hand = split_hand_suits(hand)
    aces_high_sorted_hand = aces_high_sort(sort_hand_numbers(hand))
    score_vector = [0] * 9
    score_vector[0] = straight_flush_test(suit_sorted_hand)
    score_vector[1] = four_of_a_kind_test(aces_high_sorted_hand)
    score_vector[2] = full_house_test(aces_high_sorted_hand)
    score_vector[3] = flush_test(suit_sorted_hand)
    score_vector[5] = three_of_a_kind_test(aces_high_sorted_hand)
    score_vector[6] = two_pair_test(aces_high_sorted_hand)
    score_vector[7] = pair_test(aces_high_sorted_hand)
    score_vector[8] = high_card_test(aces_high_sorted_hand)
    score_vector[4] = straight_test(num_sorted_hand)
    return score_vector


def other_player_cards(all_cards):
    cards = [[0, 0], [0, 0]]
    for i in range(2):
        cards[i][0] = randint(1, 13)
        cards[i][1] = randint(1, 4)
    for i in range(2):
        for j in range(len(all_cards)):
            while cards[i][0] == all_cards[j][0] and cards[i][1] == all_cards[j][1]:
                cards[0][i] = randint(1, 13)
                cards[1][i] = randint(1, 4)
    return cards


def other_player_hands(all_cards, cards_to_add):
    player_two_cards = other_player_cards(all_cards)
    all_cards.extend(player_two_cards)
    player_three_cards = other_player_cards(all_cards)
    all_cards.extend(player_three_cards)
    player_four_cards = other_player_cards(all_cards)
    player_two_cards.extend(cards_to_add)
    player_three_cards.extend(cards_to_add)
    player_four_cards.extend(cards_to_add)
    return player_two_cards, player_three_cards, player_four_cards


num_1 = raw_input("Number 1:")
num_2 = raw_input("Number 2:")
suit = raw_input("Suited or Unsuited? (S/U):")
if suit == "S":
    player_cards = [[int(num_1), 1], [int(num_2), 1]]
elif suit == "U":
    player_cards = [[int(num_1), 1], [int(num_2), 2]]
else:
    print "Error: suit should be S/U"
    raise SystemExit
count = 0
total = 0
while count <= 50000:
    cards_on_table = table_cards(player_cards)
    player_hand = player_cards + cards_on_table
    other_hands = other_player_hands(player_hand, cards_on_table)
    I = len(player_hand)
    while I > 7:
        player_hand.remove(player_hand[I-1])
        I = len(player_hand)
    scores = [[0], [0], [0], [0]]
    scores[0] = hand_score(player_hand)
    scores[1] = hand_score(other_hands[0])
    scores[2] = hand_score(other_hands[1])
    scores[3] = hand_score(other_hands[2])
    sorted_scores = sorted(scores, reverse=True)
    if scores[0] == sorted_scores[0]:
        total += 1
    count += 1
print "Your chance of winning is %d %%" % (total / 500)
