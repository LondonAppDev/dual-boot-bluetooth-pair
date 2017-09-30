import codecs
import re
import argparse


def reg_file_to_str(file_path):
    """Open file at given path and convert to a string."""
    with codecs.open(file_path, 'r', 'utf-16-le') as f:
        file_str = f.read()
        return file_str


def _is_bt_entry(header_str):
    """Determin if the provided string is the bt section header."""
    # regex = re.compile('\[HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Services\\BTHPORT\\Parameters\\Keys\\[\w]{12}\\[\w]{12}]')e
    import pdb; pdb.set_trace()


def file_path_to_dict(reg_str):
    """Convert given reg file str to a python dictionary."""
    sections = reg_str.split('\r\n\r\n')
    bt_entries = []
    for section in sections:
        section_lines = section.split('\r\n')
        section_header = section_lines[0]
        print('SECTION HEADER: {}'.format(section_header))
        _is_bt_entry(section_header)

    import pdb; pdb.set_trace()


def _parse_args():
    """Parse arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument('action', help='Action to perform.')
    

def main():



reg_str = reg_file_to_str('/home/mark/Desktop/BTKeys.reg')
# file_path_to_dict(reg_str)



# Print
