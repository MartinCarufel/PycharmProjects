# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from random import randint

class Name_draw:
    def __init__(self):
        self.participant_in = []
        self.participant_out = []
        self.name_draw = ''

    def draw_name(self):
        nb_remained_participants = len(self.participant_in)
        draw_number = randint(0, nb_remained_participants-1)
        self.name_draw = self.participant_in[draw_number]

    def remove_draw_name(self):
        pass

    def convert_file_to_list(self, file):

        with open(file) as f_in:
            # self.participant_in = (line.rstrip() for line in f_in)
            # self.participant_in = list(line for line in self.participant_in if line)  # Non-blank lines in a list
            to_list = (line.rstrip() for line in f_in)
            to_list = list(line for line in to_list if line)  # Non-blank lines in a list
        return to_list
        # with open(file) as f:
        #     self.participant_in = f.read().splitlines()

    def accept_the_name(self):
        # print('Did you accept {} to be the next responsible (Y/N) ? ', )
        while True:
            response = input('Did you accept {} to be the next responsible (y/n) ? ' .format(self.name_draw))
            if response.upper() == 'Y':
                self.participant_in.remove(self.name_draw)
                self.participant_out = self.convert_file_to_list('excluded_participants.txt')
                self.participant_out.append(self.name_draw)
                break
            elif response.upper() == 'N':
                break
            else:
                print('Respond by Y or N')
        return response.upper()
        # return None

    def convert_list_to_file(self, list, file):
        with open(file, 'w') as f:
            for name in list:
                f.writelines(name + '\n')

    def transfert_exclude_participants(self):
        exclude_participant = self.convert_file_to_list('excluded_participants.txt')
        self.convert_list_to_file(exclude_participant, 'participants.txt')
        self.convert_list_to_file([], 'excluded_participants.txt')

    def ask_yes_or_no(self, message):
        while True:
            response = input(message)
            if response.upper() in ['Y', 'n']:
                break
            else:
                print('Respond by Y or N')
        return response.upper()


def main():
    # Use a breakpoint in the code line below to debug your script.
    response = 'N'
    while response.upper() != 'Y':
        o = Name_draw()
        o.participant_in = o.convert_file_to_list('participants.txt')
        try:
            o.draw_name()
        except ValueError:
            print("""
Participant list might be empty,
please check the file participants.txt.
All participant may be moved to the file expluded_participants.txt
                      """)
            answer = o.ask_yes_or_no('Do you want to copy all name in excluded_participants.txt to participants.txt (y/n) ? ')
            if answer == 'Y':
                o.transfert_exclude_participants()
                o.participant_in = o.convert_file_to_list('participants.txt')
                o.draw_name()
        response = o.accept_the_name()
        o.convert_list_to_file(o.participant_in, 'participants.txt')
        o.convert_list_to_file(o.participant_out, 'excluded_participants.txt')







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
