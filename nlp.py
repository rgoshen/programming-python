if __name__ == '__main__':
    lines_to_read = int(input())
    analyze_text = ''
    t_count = 0
    s_count = 0

    for _ in range(lines_to_read):
        line = input().lower()
        analyze_text += line
        analyze_text += ' '

    t_count = analyze_text.count('t')
    s_count = analyze_text.count('s')

    if t_count > s_count:
        print('English')
    else:
        print('French')
