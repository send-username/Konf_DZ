import json
import tarfile
from datetime import datetime


class MyTerminal:
    def __init__(self, user_name, file_system):
        self.us_name = user_name
        self.fs = file_system

        self.cur_d = ''
        self.polling = False

    def output(self, message, end='\n'):
        print(message)
        return message

    def start_polling(self):
        self.polling = True
        while self.polling:
            message = f'{self.us_name}:~{self.cur_d}$ '
            enter = input(message).strip()
            if len(enter) > 0:
                self.command_dispatcher(enter)
        self.output('stop polling...')

    def command_dispatcher(self, command):
        params = command.split()
        if params[0] == 'exit':
            self.polling = False
        elif params[0] == 'cd':
            self.cd(params[1:])
        elif params[0] == 'ls':
            self.ls(params[1:])
        elif params[0] == 'tail':
            self.output(self.tail(params[1:]))
        elif params[0] == 'find':
            self.find(params[1:])
        else:
            self.output("Command not found")

    def find_path(self, path):
        current_path = self.cur_d

        while '//' in path:
            path = path.replace('//', '/')
        if path[-1] == '/':
            path = path[:-1]

        path = path.split('/')
        if path[0] == '/':
            current_path = ''
            path.pop(0)

        while path:
            name = path.pop(0)
            if name == '.':
                current_path = self.cur_d
            elif name == '..':
                index = current_path.rfind('/')
                if index > -1:
                    current_path = current_path[:index]
                else:
                    current_path = ''
            else:
                if current_path:
                    current_path += '/' + name
                else:
                    current_path += name
                with tarfile.open(self.fs, 'r') as tar:
                    paths = [member.name for member in tar]
                    if current_path not in paths:
                        return None

        return current_path

    def ls(self, prmtrs):
        message = ""

        def ls_names(c_directory):
            m_names = set()
            with tarfile.open(self.fs, 'r') as tar:
                for member in tar:
                    m_name = member.name
                    if m_name.find(c_directory) > -1:
                        if m_name == c_directory:
                            if member.type == tarfile.DIRTYPE:
                                continue
                            return (c_directory[c_directory.rfind('/') + 1:],)

                        m_name = m_name[len(c_directory):]
                        if m_name[0] == '/':
                            m_name = m_name[1:]
                        erase = m_name.find('/')
                        if erase > -1:
                            m_name = m_name[:m_name.find('/')]
                        m_names.add(m_name)
            return sorted(m_names)

        if len(prmtrs) > 1:
            prmtrs.sort()
            while prmtrs:
                directory = self.find_path(prmtrs[0])
                name = prmtrs.pop(0)
                if directory is None:
                    self.output(f"ls: cannot access '{name}': No such file or directory")
                    continue

                message += self.output(f'{name}:') + '\n'
                names = ls_names(directory)
                if names:
                    message += self.output(' '.join(names)) + '\n'
                if prmtrs:
                    message += self.output('') + '\n'

            return message

        directory = self.cur_d
        if len(prmtrs) == 1:
            directory = self.find_path(prmtrs[0])
            if directory is None:
                message += self.output(f"ls: cannot access '{prmtrs[0]}': No such file or directory") + '\n'
                return message

        names = ls_names(directory)
        if names:
            message += self.output('\n'.join(names)) + '\n'
        return message

    def cd(self, prmtrs):
        if not prmtrs:
            self.cur_d = ''
            return 'root directory'

        if len(prmtrs) > 1:
            return self.output("cd: too many arguments")

        new_directory = self.find_path(prmtrs[0])
        if new_directory is None:
            return self.output(f"cd: {prmtrs[0]}: No such file or directory")
        if new_directory == '':
            self.cur_d = new_directory
            return f"change to " + new_directory

        with tarfile.open(self.fs, 'r') as tar:
            for member in tar:
                if member.name == new_directory:
                    if member.type != tarfile.DIRTYPE:
                        return self.output(f"cd: {prmtrs[0]}: Not a directory")
                    self.cur_d = new_directory
                    return f"change to " + new_directory

    def find(self, prmtrs):
        message = ""

        def find_names(directory_):
            names_ = []
            with tarfile.open(self.fs, 'r') as tar:
                for member in tar:
                    name_ = member.name
                    if name_ == directory_:
                        continue
                    if name_.find(directory_) > -1:
                        name_ = name_[len(directory_):]
                        if name_[0] != '/':
                            name_ = '/' + name_
                        names_.append(name_)
            return names_

        if len(prmtrs) > 1:
            while prmtrs:
                name = prmtrs.pop(0)
                directory = self.find_path(name)
                if directory is None:
                    message += self.output(f"find: '{name}': No such file or directory") + '\n'
                    continue

                names = find_names(directory)
                message += self.output(name) + '\n'
                if name[-1] == '/':
                    name = name[:-1]
                for path in names:
                    message += self.output(name + path) + '\n'

            return message

        name = prmtrs[0] if prmtrs else '.'
        directory = self.find_path(name)
        if directory is None:
            message += self.output(f"find: '{prmtrs[0]}': No such file or directory") + '\n'
            return message

        names = sorted(find_names(directory))
        message += self.output(name) + '\n'
        if name[-1] == '/':
            name = name[:-1]
        for path in names:
            message += self.output(name + path) + '\n'
        return message

    def tail(self, params):
        file = params[0]
        n = 10
        if len(params) >= 3:
            if params[1] == '-n':
                try:
                    n = int(params[2])
                except:
                    return 'Wring lines amount'

        f_name = self.find_path(file)
        try:
            with tarfile.open(self.fs, 'r') as tar:
                for f in tar:
                    if f.name == f_name:
                        if f.type != tarfile.DIRTYPE:
                            with tar.extractfile(f) as read_file:
                                lines = []
                                for i in read_file:
                                    lines.append(i.decode('UTF-8').replace('\r', ''))
                                return ''.join(lines[-n:])
                        else:
                            return 'Is directory'
        except:
            return 'Wrong file name'
