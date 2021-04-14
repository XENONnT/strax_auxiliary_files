def exporter(export_self=False):
    """
    Export utility modified from https://stackoverflow.com/a/41895194
    Returns export decorator, __all__ list
    https://github.com/AxFoundation/strax/blob/master/strax/utils.py
    """
    all_ = []
    if export_self:
        all_.append('exporter')

    def decorator(obj):
        all_.append(obj.__name__)
        return obj

    return decorator, all_


export, __all__ = exporter(export_self=True)
