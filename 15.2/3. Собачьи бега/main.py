dogs_score = [5, 2, 3, 4, 1]
dogs = 5

score_min = 1
score_max = 5

for temp in dogs_score:
    if temp > score_max:
        score_max = temp
    if temp < score_min:
        score_min = temp

for i_dog in range(dogs):
    if dogs_score[i_dog] == score_min:
        dogs_score[i_dog] = score_max
        continue
    if dogs_score[i_dog] == score_max:
        dogs_score[i_dog] = score_min

print(dogs_score)