import unittest
import file_manager
from msg_split import split_message


test_parsed_str_c1 = """<div>
    Lorem ipsum dolor sit amet
    <strong>
        Aliquid ea illo ipsum
    </strong>
    <a href="">
    Amet at cum deserunt
    </a>
</div>"""

class MyTestCase(unittest.TestCase):
    def test_open_file(self):
        result = file_manager.open_file('for_tests.html')
        self.assertEqual(result, test_parsed_str_c1)

    def test_split_basic(self):
        html = "<p>" + "a" * 6000 + "</p>"
        fragments = list(split_message(html, max_len=4096))
        self.assertEqual(len(fragments), 2)
        self.assertTrue(fragments[0].endswith("</p>"))
        self.assertTrue(fragments[1].startswith("<p>"))


if __name__ == '__main__':
    unittest.main()
