
def name_to_csv(csv_file):
    csv = []

    print('학생 정보 입력 (tab 으로 구분)')

    while True:
        line = input()
        info = line.split('\t')
        if len(info) == 1:
            break
        print(len(info))
        print(info)
        csv.append(','.join(info)+',')

    with open(csv_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(csv))
