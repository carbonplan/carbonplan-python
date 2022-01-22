from carbonplan.watermark import watermark


def test_watermark():

    assert isinstance(watermark(print_info=False), str)
    assert watermark(print_info=True) is None
