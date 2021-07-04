phrase = input("Set a phrase: ")

class TestPhrase:
    def test_len_phrase(self):
        len_phrase = len(phrase)
        assert len_phrase < 15, "The entered phrase is at least 15 characters long"