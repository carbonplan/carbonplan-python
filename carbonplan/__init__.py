import sys

import entrypoints

imports = {}


def __getattr__(attr):

    if attr == '__all__':
        return __dir__()
    try:
        return sys.modules[f'carbonplan.{attr}']
    except KeyError:
        raise AttributeError(attr)


def __dir__(*_, **__):
    return sorted(list(globals()) + list(imports))


def _make_imports():
    for module in entrypoints.get_group_all('carbonplan.modules'):
        imports[module.name] = module
        sys.modules[f'carbonplan.{module.name}'] = module.load()


_make_imports()
