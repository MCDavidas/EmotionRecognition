import pytest
import os
from PIL import Image

from ..app import analyzer


IMAGE_TESTS = [('images/test2.jpg', 'Happy'), ('images/test3.png', 'Neutral'),
               ('images/test4.jpeg', 'Fear'), ('images/test5.png', 'Neutral')]


@pytest.mark.asyncio
@pytest.mark.parametrize('path, output', IMAGE_TESTS)
async def test_analyze_image(path, output):
    try:
        img = Image.open(os.path.join(os.path.dirname(__file__), path))
    except FileNotFoundError:
        pytest.skip('File {path} not found'.format(path=path))

    result_img, emotion = await analyzer.analyze_image(img)
    assert output == emotion
