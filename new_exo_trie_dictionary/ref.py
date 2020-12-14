import re       # for bonus
import getkey   # for bonus


class Node:
    def __init__(self, char):
        self.char = char
        self.children = []
        self.is_end_word = False

    def add_child_at(self, index, child):
        if index < 0 or index > len(self.children):
            return False
        self.children.insert(index, child)
        return True

    def insert_char(self, char):
        nb_children = len(self.children)

        for i in range(nb_children):
            if char == self.children[i].char:
                return self.children[i]

            if char < self.children[i].char:
                # insert the char
                self.add_child_at(i, Node(char))
                return self.children[i]

        # at the end
        self.add_child_at(nb_children, Node(char))
        return self.children[nb_children]

    def get_child(self, char):
        for child in self.children:
            if child.char == char:
                return child
        return None

    def get_chars(self, prefix):
        word = prefix + self.char
        words = []

        if self.is_end_word:
            words.append(word)

        for child in self.children:
            words += child.get_chars(word)

        return words

    def __repr__(self):
        return self.char


class Dict:
    def __init__(self):
        self.root = Node('')

    def add_word(self, word):
        current_node = self.root

        for letter in word:
            node_letter = current_node.get_child(letter)
            if not node_letter:
                node_letter = current_node.insert_char(letter)

            current_node = node_letter
        current_node.is_end_word = True

    def exists(self, word):
        current_node = self.root

        for letter in word:
            current_node = current_node.get_child(letter)
            if not current_node:
                return False

        return current_node.is_end_word

    def print_words(self):
        words = self.root.get_chars("")
        for w in words:
            print(w)

    ############ BONUS ############
    # Add all words from file in dico
    # one word per line
    def add_file(self, filename):
        f = open(filename, "r")
        if not f:
            print(f"Cannot find file '{filename}'")

        for line in f:
            self.add_word(line.strip())

        f.close()

    ############ BONUS #############
    # Get words with a given prefix
    def get_words_from_prefix(self, prefix):
        current_node = self.root

        for letter in prefix:
            node_letter = current_node.get_child(letter)
            if not node_letter:
                return []

            current_node = node_letter

        words = current_node.get_chars(prefix[:-1])
        return words


######## BONUS ########
def check_file_with_dico(filename, dico):
    f = open(filename, "r")
    if not f:
        print(f"Cannot find file '{filename}'")

    bad_words = []

    regex = "\.|'|\"|,|:|;|\n|\r| |!|\?|<|>|\[|\]|{|}|=|\+|%|/|\*"
    words = re.split(regex, f.read())
    for word in words:
        if word != '' and not word in bad_words and not dico.exists(word):
            bad_words.append(word)

    f.close()

    if not bad_words:
        print("Tous les mots sont dans le dictionnaire")
        return

    print("Ces mots ne sont pas dans le dictionnaire:")
    for word in bad_words:
        print(f"- {word}")


########## BONUS ###########
def autocomplete(dico):
    def get_last_word(line):
        words = line.split(' ')
        return words[-1]

    line = ""
    while True:
        key = getkey.getkey()

        if key == getkey.keys.ENTER:
            print()
            line = ""
        elif key == getkey.keys.BACKSPACE:
            line = line[:-1]

        elif key == getkey.keys.TAB:
            prefix = get_last_word(line)
            words = dico.get_words_from_prefix(prefix)
            if len(words) == 1:
                line += words[0][len(prefix):]
            elif len(words) > 1:
                print("\r", " - ".join(words), " " * 30, sep='')

        else:
            line += key

        print(f"\r{line}", end='')


def main():
    d = Dict()
    while True:
        word = input("Entrez votre commande: ")
        if word == "exit" or word == "quit":
            break

        if word == "add":
            word = input("Quel mot dois-je ajouter au dictionnaire ?\n")
            d.add_word(word)

        elif word == "import":      # bonus
            filename = input("Quel fichier est le dictionnaire à importer ?\n")
            d.add_file(filename)

        elif word == "test" or word == "exist":
            word = input("Quel mot dois-je tester ?\n")
            if d.exists(word):
                print("Ce mot appartient bien au dictionnaire.")
            else:
                print("Ce mot n'est pas dans le dictionnaire.")

        elif word == "check":       # bonus
            filename = input("Quel fichier dois-je vérifier ?\n")
            check_file_with_dico(filename, d)

        elif word == "print":
            d.print_words()

        elif word == "autocomplete": # bonus
            autocomplete(d)

        else:
            print("Mauvaise commande: utilisez \"exit\", \"add\", \"test\",",
                  "\"print\" et en bonus: \"import\", \"check\", \"autocomplete\"")


if __name__ == "__main__":
    main()
