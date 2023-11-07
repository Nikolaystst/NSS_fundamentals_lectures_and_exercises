import re

nss_pattern = r"\b(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})\b"
word = input()
searched = re.findall(nss_pattern, word)

for day_month_year in searched:
    day = day_month_year[0]
    month = day_month_year[2]
    year = day_month_year[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")
