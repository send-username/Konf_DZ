from sys import argv
from os.path import exists
from terminal import MyTerminal


def main():
    if len(argv) >= 3:
        user_name = argv[1]
        fs_path = argv[2]
    else:
        print('Введены не все ключи для корректного запуска')
        return

    if not exists(fs_path):
        print("Файловая система с таким названием отсутствует")
        return

    terminal = MyTerminal(user_name, fs_path)
    terminal.start_polling()


if __name__ == '__main__':
    main()
