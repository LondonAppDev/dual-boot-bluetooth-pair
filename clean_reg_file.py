#!/usr/bin/env python
import argparse
import codecs


def _parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Path of file to convert.')
    parser.add_argument('output', help='Output location of file.')

    return parser.parse_args()


def _reg_file_to_str(file_path):
    """Open file at given path and return as a string."""
    with codecs.open(file_path, 'r', 'utf-16-le') as f:
        file_str = f.read()
        return file_str


def _clean(contents):
    """ Clean contents and return."""
    contents = contents.replace('"', '')
    lines = contents.split('\r\n')
    del lines[0]
    new_lines = []
    for line in lines:
        new_lines.append(line.strip())

    return '\n'.join(new_lines)



def _save_str_to_file(contents, file_path):
    """Save the string as a file."""
    with open(file_path, 'wb') as f:
        f.write(contents.encode('utf-8'))


def main():
    """Main entrypoint to script."""
    args = _parse_args()
    file_contents = _reg_file_to_str(args.file_path)
    file_contents = _clean(file_contents)
    _save_str_to_file(file_contents, args.output)


if __name__ == '__main__':
    main()
