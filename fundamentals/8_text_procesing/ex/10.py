def win_tickets(word):
    if len(word) != 20:
        return "invalid ticket"
    left_part = word[:10]
    right_part = word[10:]
    for symbol in winning_symbols:
        for matching in range(10, 5, -1):
            winning_streak = symbol * matching
            if winning_streak in left_part and winning_streak in right_part:
                if symbol * 10 in left_part and symbol * 10 in right_part:
                    return f'ticket "{word}" - 10{symbol} Jackpot!'
                return f'ticket "{word}" - {matching}{symbol}'
    return f'ticket "{word}" - no match'


tickets = input()
tickets = [x.strip() for x in tickets.split(", ")]
winning_symbols = ['@', '#', '$', '^']
for word in tickets:
    print(win_tickets(word))
