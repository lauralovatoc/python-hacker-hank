def count_substring(s, sub_s):
    result = 0
    count = 0
    x=1

    for i in range(0, len(s)):
        if sub_s[0] == s[i]:
            count += 1
            x=1

            while x < len(sub_s):
                if i+x >= len(s):
                    break
                if sub_s[x] == s[i + x]:
                    if count == len(sub_s):
                        break
                    count += 1
                else:
                    count = 0
                x += 1

        if count == len(sub_s):
            result += 1
            count = 0

    return result


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = 'TestCaseTestCase'
    sub_string = 'CaseT'

    count = count_substring(string, sub_string)
    print(count)