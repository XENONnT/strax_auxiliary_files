import os
from utilix.io import read_file
import pkg_resources
import straxauxfiles

export, __all__ = straxauxfiles.exporter()


@export
def list_sim_files():
    """Get a list of files we have we have in the fax files"""
    p = _package_path('sim_files')
    return _list_files(p)


@export
def list_strax_files():
    """Get a list of files we have we have in the strax files"""
    p = _package_path('strax_files')
    return _list_files(p)


@export
def list_aux_files():
    """Get a list off all the private files we have stored in this package"""
    return list_strax_files() + list_sim_files()


@export
def get_strax_file(file_name):
    """
    Get files stored under strax_files. Add "fmt = <format>" as an
    argument to read a specific format. otherwise we will assume it's in
    a text format. See straxen.get_recourse for more info.
    """
    p = _package_path('strax_files')
    return _get_file(file_name, get_from=p)


@export
def get_sim_file(file_name):
    """
    Get files stored under get_sim_file. Add "fmt = <format>" as an
    argument to read a specific format. otherwise we will assume it's in
    a text format. See straxen.get_recourse for more info.
    """
    p = _package_path('sim_files')
    return _get_file(file_name, get_from=p)


@export
def get_aux_file(file_name, **kwargs):
    if file_name in list_sim_files():
        return get_sim_file(file_name, **kwargs)
    elif file_name in list_strax_files():
        return get_strax_file(file_name, **kwargs)
    else:
        raise FileNotFoundError(f'No file {file_name} in {list_aux_files()}')


@export
def get_abspath(file_name):
    """Get the abspath of the file. Raise FileNotFoundError when not found in any subfolder"""
    for sub_dir in ('sim_files', 'strax_files'):
        p = os.path.join(_package_path(sub_dir), file_name)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(f'Cannot find {file_name}')


def _get_file(file_name, get_from):
    """Get a file from a subfolder in this package"""
    if file_name not in _list_files(get_from):
        raise FileNotFoundError(f'No file {file_name} in {get_from}')
    else:
        path = os.path.join(get_from, file_name)
        return read_file(path)


def _package_path(sub_directory):
    """Get the abs path of the requested sub folder"""
    return pkg_resources.resource_filename('straxauxfiles', f'../{sub_directory}')


def _list_files(path):
    """List the files stored under path"""
    return os.listdir(path)
