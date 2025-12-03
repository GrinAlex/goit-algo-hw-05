def float_binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iterations = 1

    while low <= high:
        mid = (high + low) // 2
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
            iterations += 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1
            iterations += 1
        # якщо x присутній на позиції повертаємо його
        else:
            return (iterations, x)

    #якщо елемент не знайдено і нижня границя менше довжини масиву, то беремо елемент за індексом low
    if low < len(arr):
        return(iterations, arr[low])
    
    # якщо елемент не знайдений
    return (iterations, -1)


# Приклад пошуку
# arr = [-1.2, 0.33, 2.5, 3.1, 4.4]
# x = 2.6

# print(float_binary_search(arr, x))

