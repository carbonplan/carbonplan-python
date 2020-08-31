import sys

imports = {}


def __getattr__(attr):
    print(attr)
    if attr == '__all__':
        return __dir__()
    try:
        module = imports[attr].load()
        sys.modules[attr] = module
        sys.modules[f'carbonplan.{attr}'] = module
        return module
    except KeyError:
        raise AttributeError(attr)


def __dir__(*_, **__):
    print(_, __)
    return sorted(list(globals()) + list(imports))


def _make_imports():
    import entrypoints

    for module in entrypoints.get_group_all('carbonplan.modules'):
        imports[module.name] = module


_make_imports()
