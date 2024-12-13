import pytest
from terminal import MyTerminal
import tarfile


@pytest.fixture
def terminal():
    user_name = 'test_user'
    fs_path = 'archive.tar'
    tarfile.open(fs_path)
    t = MyTerminal(user_name, fs_path)
    return t


@pytest.mark.parametrize(
    'arg, expected', [
        ([],
         '''desktop
hello.txt
users
'''),
        (['desktop'],
         '''folder
more_textes.txt
'''),
        (['users'],
         '''root
user
''')
    ]
)
def test_ls(terminal, arg, expected):
    val = terminal.ls(arg)
    assert val == expected


@pytest.mark.parametrize(
    'arg, expected', [
        ([],
         'root directory'),
        (['desktop'],
         'change to desktop'),
        (['users'],
         'change to users')
    ]
)
def test_cd(terminal, arg, expected):
    val = terminal.cd(arg)
    assert val == expected


@pytest.mark.parametrize(
    'arg, expected', [
        ([],
         '''.
./desktop
./desktop/folder
./desktop/folder/bin
./desktop/folder/world
./desktop/more_textes.txt
./hello.txt
./users
./users/root
./users/user\n'''),
        (['desktop'],
         '''desktop
desktop/folder
desktop/folder/bin
desktop/folder/world
desktop/more_textes.txt\n'''),
    ]
)
def test_find(terminal, arg, expected):
    val = terminal.find(arg)
    assert val == expected


@pytest.mark.parametrize(
    'arg, expected', [
        (['hello.txt'],
         '''here is
some
text
order:
1
2
3
'''),
        (['hello.txt', '-n', '3'],
         '''1
2
3
''')
    ]
)
def test_cd(terminal, arg, expected):
    val = terminal.tail(arg)
    assert val == expected
