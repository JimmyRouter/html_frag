import click
from msg_split import split_message  # Assuming you implemented split_message
from file_manager import open_file  # Assuming you implemented open_file


@click.command()
@click.argument('file_path', type=click.Path(exists=True))
@click.option('--max-len', default=4096, help='Maximum length of each fragment', type=int)
def split_file(file_path, max_len):
    """
    Splits the content of the HTML file at FILE_PATH into fragments
    based on the specified --max-len parameter.
    """
    try:
        content = open_file(file_path)
        fragments = list(split_message(content, max_len))

        for i, fragment in enumerate(fragments, start=1):
            click.echo(f"fragment #{i}: {len(fragment)} chars")
            click.echo(fragment)
            click.echo('-' * 40)

    except Exception as e:
        click.echo(f"Error: {e}", err=True)


if __name__ == '__main__':
    split_file()
