import os
from ref import Node, Dict, check_file_with_dico, autocomplete, main

class TestBonus:
    class TestDictAddFile:
        def test_dict_add_file_empty(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("")
            d = Dict()
            d.add_file(filename)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == []
            assert d.root.children == []

        def test_dict_add_file_simple(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("a")
            d = Dict()
            d.add_file(filename)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == []
            assert len(d.root.children) == 1
            assert d.root.children[0].char == 'a'
            assert d.root.children[0].is_end_word == True

        def test_dict_add_file_simple2(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("ab")
            d = Dict()
            d.add_file(filename)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == []
            assert len(d.root.children) == 1
            assert d.root.children[0].char == 'a'
            assert d.root.children[0].is_end_word == False
            assert len(d.root.children[0].children) == 1
            assert d.root.children[0].children[0].char == 'b'
            assert d.root.children[0].children[0].is_end_word == True

        def test_dict_add_file_list(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("ab\nqwerty\namelie\noui\nle\nla")
            d = Dict()
            d.add_file(filename)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == []
            assert len(d.root.children) == 4
            assert d.root.children[0].char == 'a'
            assert d.root.children[0].is_end_word == False
            assert d.root.children[1].char == 'l'
            assert d.root.children[1].is_end_word == False
            assert d.root.children[2].char == 'o'
            assert d.root.children[2].is_end_word == False
            assert d.root.children[3].char == 'q'
            assert d.root.children[3].is_end_word == False

            assert len(d.root.children[0].children) == 2
            assert d.root.children[0].children[0].char == 'b' # ab
            assert d.root.children[0].children[0].is_end_word == True
            assert d.root.children[0].children[1].char == 'm'
            assert d.root.children[0].children[1].is_end_word == False

            assert len(d.root.children[1].children) == 2
            assert d.root.children[1].children[0].char == 'a' # la
            assert d.root.children[1].children[0].is_end_word == True
            assert d.root.children[1].children[1].char == 'e' # le
            assert d.root.children[1].children[1].is_end_word == True

            assert len(d.root.children[2].children) == 1
            assert d.root.children[2].children[0].char == 'u'
            assert d.root.children[2].children[0].is_end_word == False
            assert len(d.root.children[2].children[0].children) == 1
            assert d.root.children[2].children[0].children[0].char == 'i' # oui
            assert d.root.children[2].children[0].children[0].is_end_word == True

            assert len(d.root.children[3].children) == 1
            assert d.root.children[3].children[0].char == 'w'
            assert d.root.children[3].children[0].is_end_word == False


    class TestDictGetWordsFromPrefix:
        def test_dict_get_words_from_prefix_empty(self):
            d = Dict()
            words = d.get_words_from_prefix("")
            assert words == []

        def test_dict_get_words_from_prefix_basic_empty(self):
            d = Dict()
            d.root.children.append(Node('a'))
            d.root.children[0].is_end_word = False
            words = d.get_words_from_prefix("")
            assert words == []

        def test_dict_get_words_from_prefix_basic(self):
            d = Dict()
            d.root.children.append(Node('a'))
            d.root.children[0].is_end_word = True
            words = d.get_words_from_prefix("")
            assert words == ["a"]

        def test_dict_get_words_from_prefix_basic2(self):
            d = Dict()
            d.root.children.append(Node('a'))
            d.root.children.append(Node('b'))
            d.root.children.append(Node('c'))
            for child in d.root.children:
                child.is_end_word = True

            words = d.get_words_from_prefix("")
            assert words == ["a", "b", "c"]

        def test_dict_get_words_from_prefix_multiple(self):
            d = Dict()
            d.root.children.append(Node('a'))
            d.root.children.append(Node('b'))
            d.root.children.append(Node('c'))
            d.root.children[0].children.append(Node('l'))
            d.root.children[0].children.append(Node('m'))
            d.root.children[0].children.append(Node('v'))
            d.root.children[0].children[0].children.append(Node('e'))
            d.root.children[1].is_end_word = True
            d.root.children[2].is_end_word = True
            d.root.children[0].children[1].is_end_word = True
            d.root.children[0].children[2].is_end_word = True
            d.root.children[0].children[0].children[0].is_end_word = True

            words = d.get_words_from_prefix("")
            assert words == ["ale", "am", "av", "b", "c"]


    class TestCheckFileWithDico:
        def test_check_file_with_dico_empty(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("")

            d = Dict()
            check_file_with_dico(filename, d)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == ["Tous les mots sont dans le dictionnaire"]

        def test_check_file_with_dico_empty_dict(self, tmp_path, capsys):
            filename = tmp_path / "file"
            filename.write_text("a la recherche")

            d = Dict()
            check_file_with_dico(filename, d)
            array = capsys.readouterr().out.split('\n')[:-1]
            assert array == ["Ces mots ne sont pas dans le dictionnaire:",
                             "- a",
                             "- la",
                             "- recherche"]
