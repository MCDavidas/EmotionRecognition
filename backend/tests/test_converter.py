import pytest
import json
import os
import logging
from PIL import Image, ImageChops

from ..app import converter


IMAGE2ASCII_ERROR_TESTS = ['string', 12]

ASCII2IMAGE_ERROR_TESTS = ['string', 12]

IMAGE_PATHS = ['images/test1.png', 'images/test4.png']


@pytest.mark.parametrize('input', IMAGE2ASCII_ERROR_TESTS)
def test_image2ascii_type_error(input):
    try:
        converter.image2ascii(input)
    except TypeError:
        assert True
        return
    assert False


@pytest.mark.parametrize('input', ASCII2IMAGE_ERROR_TESTS)
def test_ascii2image_type_error(input):
    try:
        converter.ascii2image(input)
    except TypeError:
        assert True
        return
    assert False


@pytest.mark.parametrize('path', IMAGE_PATHS)
def test_image2ascii2image(path):
    try:
        img = Image.open(os.path.join(os.path.dirname(__file__), path))
    except FileNotFoundError:
        pytest.skip('File {path} not found'.format(path=path))

    img_ascii_data = converter.image2ascii(img)
    result_img = converter.ascii2image(img_ascii_data)

    diff = ImageChops.difference(img, result_img)
    assert diff.getbbox() is None
