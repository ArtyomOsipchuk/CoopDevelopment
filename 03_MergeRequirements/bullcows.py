import random
import urllib.request
import argparse

def bullscows(answer: str, jigsaw: str) -> (int, int):
    b, c = 0, 0
    an = list(answer)
    jig = list(jigsaw)
    for i in range(len(answer)):
        if answer[i] == jigsaw[i]:
            jig = jig[:i - b] + jig[i+1 - b:]
            an = an[:i - b] + an[i+1 - b:]
            b += 1
    for i in an:
        if i in jig:
            jig.remove(i)
            c += 1
    return b, c

def ask(prompt: str, valid: list[str] = None) -> str:
    answer = input(prompt)
    if valid:
        while answer not in valid:
            answer = input(prompt)
    return answer

def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))

def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    jigsaw = random.choice(words)
    tries = 0
    answer = 'not' + jigsaw
    while answer != jigsaw:
        tries += 1
        answer = ask("Введите слово: ", words)
        b, c = bullscows(answer, jigsaw)
        inform("Быки: {}, Коровы: {}", b, c)
    ask(f"🏆Победа-победа вместо обеда!🏆\n{tries} попыток.\nНажмите любую кнопку для выхода...")
    return tries

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                    prog='bullscows',
                    description='Bulls-Cows game',
                    epilog='Cool game for cool students.')
    parser.add_argument("dictionary", help="это имя файла или URL со словарём слов для игры")
    parser.add_argument("length", nargs="?", default=5, type=int, help="необязательный параметр, указывающий длину используемых слов (по умолчанию 5)")
    args = parser.parse_args()
    if args.dictionary.startswith('https://'):
        with urllib.request.urlopen(args.dictionary) as response:
            words = response.read().decode('utf-8').splitlines()
    else:
        with open(args.dictionary, "r") as f:
            words = f.read().split('\n')
    words = [i for i in words if len(i) == args.length]
    gameplay(ask, inform, words)
