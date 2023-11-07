k = int(input())
l = int(input())
m = int(input())
n = int(input())
k_counter = 0
l_counter = 0
m_counter = 0
n_counter = 0
the_end = ""
counter = 0

for x in range(k, 9):
    for y in range(9, l - 1, -1):
        for a in range(m, 9):
            for b in range(9, n - 1, -1):
                k_counter = x
                l_counter = y
                m_counter = a
                n_counter = b
                if k_counter % 2 == 0 and m_counter % 2 == 0 and l_counter % 2 != 0 and n_counter % 2 != 0:
                    the_end = f"{k_counter}{l_counter} - {m_counter}{n_counter}"
                    if k_counter == m_counter and l_counter == n_counter:
                        print("Cannot change the same player.")
                        continue
                    else:
                        print(f"{the_end}")
                        counter += 1
                        if counter == 6:
                            break
                        continue
                else:
                    continue
            if counter == 6:
                break
        if counter == 6:
            break
    if counter == 6:
        break
