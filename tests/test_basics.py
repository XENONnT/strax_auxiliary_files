import straxauxfiles
import straxen
from warnings import warn


##
# Hard code some parameters, the KNOWN_FORMATS convert the extensions
# to the format specifier in straxen. The KNOWN_UNKNOWN_FORMATS are the
# formats we know that can safely be ignored
##
KNOWN_FORMATS = {k: k for k in ('json', 'json.gz', 'pkl', 'pkl.gz', 'csv', 'npy')}
KNOWN_FORMATS.update({'txt': 'text', 'npz': 'npy_pickle'})
KNOWN_UNKNOWN_FORMATS = ('tar.gz', 'tar',  'h5')


def parse_extension(name):
    """Get the extention from a file name. If zipped or tarred, can contain a dot"""
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
    For all files in the repo using the absolute path and straxen.get_resource
    """
    for file in straxauxfiles.list_aux_files():
        print(f'Doing {file}')
        abs_path = straxauxfiles.get_abspath(file)
        fmt = parse_extension(file)
        if fmt in KNOWN_FORMATS:
            try:
                straxen.get_resource(abs_path, fmt=KNOWN_FORMATS[fmt])
            except ValueError as e:
                if fmt == 'npy':
                    # Let's retry if it is zipped
                    fmt = 'npz'
                    straxen.get_resource(abs_path, fmt=KNOWN_FORMATS[fmt])
                    warn(f'{file} says it is .npy but it should be .npz!!')
                else:
                    raise e

        elif fmt in KNOWN_UNKNOWN_FORMATS:
            # Don't open files we cannot open
            warn(f'We are ignoring testing {file} because of fmt={fmt}')
        else:
            raise ValueError(f'{fmt} is unknown, cannot test if straxen '
                             f'can open this file')
