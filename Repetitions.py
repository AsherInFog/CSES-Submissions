def main() -> None:
    s = input()
    best_length = 1
    current_length = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            current_length = 1
        if current_length > best_length:
            best_length = current_length

    print(best_length)

if __name__ == '__main__':
    main()