def main() -> None:
    n = int(input())
    sequence: list[int] = []
    
    while True:
        sequence.append(n)
        if n == 1:
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1

    print(' '.join(str(x) for x in sequence))

if __name__ == '__main__':
    main()

