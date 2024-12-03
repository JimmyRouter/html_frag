from bs4 import BeautifulSoup, element
from typing import Generator

from constants import MAX_LEN, BLOCK_TAGS, FRAG_STRING
from file_manager import open_file   # should build high level app logic in separate file, my_parser_module.py/main.py for  example


def split_message(source: str, max_len: int = MAX_LEN) -> Generator[str, None, tuple]:
    """
    Splits the original message (`source`) into fragments of the specified length
    (`max_len`).
    :param source: The string message to be split.
    :param max_len: The maximum length of each chunk. Defaults to MAX_LEN.
    :return: A generator that yields sub markups of the original markup, each up to `max_len` characters long.
    """
    soup = BeautifulSoup(source, 'lxml')
    current = 0
    cursor = 0
    parents = []
    number = 1

    def build_opening_tags() -> str:
        """Generate opening tags for the current parent hierarchy."""
        return ''.join(f'<{tag}>' for tag in parents if tag is not None)

    def build_closing_tags() -> str:
        """Generate closing tags for the current parent hierarchy."""
        return ''.join(f'</{tag}>' for tag in reversed(parents) if tag is not None)

    def split_tag(tag: element.Tag | element.NavigableString, chunk:str, cur_len:int ):
        nonlocal parents
        nonlocal cursor
        if isinstance(tag, element.Tag):
            parents.append(tag.name)

            if tag.name not in BLOCK_TAGS:
                print(f'Splitting of <{tag.name}> tags not allowed')
                cursor = len(chunk)
                return '' + build_closing_tags()

            for child in tag.children:
                if cur_len + len(str(child)) + len(build_closing_tags()) > max_len:
                    return split_tag(child, chunk, cur_len)

                elif cur_len + len(str(child)) + len(build_closing_tags()) < max_len:
                    chunk += str(child)
                    cur_len += len(str(child))
                    continue

                elif cur_len + len(str(child)) + len(build_closing_tags()) == max_len:
                    chunk += str(child)
                    cur_len += len(str(child))
                    cursor = cur_len
                    return chunk + build_closing_tags()

        if isinstance(tag, element.NavigableString):
            if FRAG_STRING:
                str_tag = str(tag)[:max_len-cur_len-len(str(tag))-len(build_closing_tags())]
                print()
                chunk += str_tag
                cur_len += len(str_tag)

            cursor = len(chunk)-len(build_closing_tags())
            return chunk + build_closing_tags()

        print(f'Unexpected Type: {type(tag)}')

    bunch = ''
    all_tags: list[element.Tag | element.NavigableString] = soup.body.children

    for tag in all_tags:
        str_tag = str(tag)
        if cursor != 0:
            prev_tag = str(tag.previous_sibling)[cursor+12:]   #TODO
            cursor = 0

            if len(prev_tag) < max_len:
                str_tag = prev_tag + str_tag
            else:   # TODO
                print("OVERSIZED PART")

        if current + len(str_tag) < max_len:
            bunch += str_tag
            current = len(bunch)

        else:
            bunch += split_tag(tag, '', current)
            yield bunch
            number += 1
            current = 0
            bunch = build_opening_tags()

    if bunch:
        yield bunch


    return f'DOCUMENT FRAG FINISHED', 0


if __name__ == '__main__':
    source_markup = open_file('source.html')
    for d in split_message(source_markup):
        print(f'>>>>>>><<<<<<<<<<\n {d}')


