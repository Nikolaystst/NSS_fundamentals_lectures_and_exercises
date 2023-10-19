snowbows_count = int(input())
final_w = 0
final_t = 0
final_q = 0
final_c = 0

for i in range(snowbows_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    calculated_snow_bow = (weight / time) ** quality
    if final_c < calculated_snow_bow:
        final_w = weight
        final_t = time
        final_q = quality
        final_c = calculated_snow_bow
    else:
        continue

print(f"{final_w} : {final_t} = {int(final_c)} ({final_q})")
