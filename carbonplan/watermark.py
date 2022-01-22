import watermark.watermark as _watermark


def watermark(
    print_info=True,
    updated=True,
    iso8601=True,
    python=True,
    machine=True,
    githash=True,
    iversions=True,
    **kwargs
):
    info = _watermark(
        updated=updated,
        iso8601=iso8601,
        python=python,
        machine=machine,
        githash=githash,
        iversions=iversions,
        globals_=globals(),
        **kwargs
    )

    if print_info:
        print(info)
    else:
        return info
