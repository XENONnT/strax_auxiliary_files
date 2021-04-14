import straxauxfiles
import utilix
from warnings import warn


##
# Hard code some parameters, the KNOWN_FORMATS convert the extensions
# to the format specifier in straxen. The KNOWN_UNKNOWN_FORMATS are the
# formats we know that can safely be ignored
##
KNOWN_FORMATS = ('json', 'json.gz', 'pkl', 'pkl.gz', 'csv', 'npy', 'txt',  'npz')
KNOWN_UNKNOWN_FORMATS = ('tar.gz', 'tar',  'h5')


def parse_extension(name):
    """Get the extension of a filename. If zipped or tarred, can contain a dot"""
    split_name = name.split('.')
    if len(split_name) == 2:
        fmt = split_name[-1]
    elif len(split_name) > 2 and 'gz' in name:
        fmt = '.'.join(split_name[-2:])
    else:
        fmt = split_name[-1]
        warn(f'Using {fmt} for ambiguous {name}')
    return fmt

##
# Test
##


def test_open():
    """
    For all files in the repo using the absolute path and utilix.io.read_file
    """
    for file in straxauxfiles.list_aux_files():
        print(f'Doing {file}')
        if file in 'filters_per_chan.npy ele_after_pulse.npy'.split():
            continue
        abs_path = straxauxfiles.get_abspath(file)
        fmt = parse_extension(file)
        if fmt in KNOWN_FORMATS:
            utilix.io.read_file(abs_path)
        elif fmt in KNOWN_UNKNOWN_FORMATS:
            # Don't open files we cannot open
            warn(f'We are ignoring testing {file} because of fmt={fmt}')
        else:
            raise ValueError(f'{fmt} is unknown, cannot test if straxen '
                             f'can open this file')
