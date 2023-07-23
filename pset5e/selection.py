def selection_sort(data):
    for i in range(len(data) - 1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        data[i], data[min_index] = data[min_index], data[i]


def main():
    data = [5, 3, 1, 2, 4]
    print(data)
    selection_sort(data)
    print(data)


if __name__ == "__main__":
    main()
