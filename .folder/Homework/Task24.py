def max_berry_count(berry_counts):
    max_berry = 0
    n = len(berry_counts)

    for i in range(n):
        # Вычисляем количество ягод для текущего положения собирающего модуля
        curr_berry = berry_counts[i] + berry_counts[(i-1) % n] + berry_counts[(i+1) % n]

        # Обновляем максимальное количество ягод
        max_berry = max(max_berry, curr_berry)

    return max_berry
