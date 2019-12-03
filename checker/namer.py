
def name_to_csv():
    csv = []

    while True:
        line = input()
        info = line.split('\t')
        if len(info) == 1:
            break
        print(len(info))
        print(info)
        csv.append(','.join(info)+',')

    with open('checker.csv', 'w', encoding='utf-8') as f:
        f.write('\n'.join(csv))
