if __name__ == '__main__':
    records = [
        ['chi', 20.0],  # x
        ['beta', 50.0],  # x
        ['alpha', 50.0]  # x
    ]

    records = sorted(records, key=lambda x: (x[1], x[0]))

    print(records)
