def main() -> None:
    n = int(input())
    numbers = list(map(int, input().split()))

    total_moves = 0
    prev = numbers[0]

    for i in range(1, n):
        if numbers[i] < prev:
            total_moves += prev - numbers[i]
        else:
            prev = numbers[i]
    
    print(total_moves)

if __name__ == '__main__':
    main()