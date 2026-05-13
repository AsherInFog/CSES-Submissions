def main() -> None: 
    n = int(input())
    numbers = list(map(int, input().split()))

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    print(expected_sum - actual_sum)



if __name__ == '__main__':
    main()
