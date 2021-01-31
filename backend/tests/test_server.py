import pytest
import asyncio
import json

from ..app import server


MESSAGE_TEST_CASES = [('string', server.ERROR_MESSAGE),
                      (12, server.ERROR_MESSAGE),
                      (json.dumps({'string': 'string',
                                   'image': 'image'}), server.ERROR_MESSAGE),
                      (json.dumps({'type': 12,
                                   'image': 'image'}), server.ERROR_MESSAGE),
                      (json.dumps({'type': 'string',
                                   'image': 'image'}), server.ERROR_MESSAGE),
                      (json.dumps({'type': 'image',
                                   'string': 'string'}), server.ERROR_MESSAGE),
                      (json.dumps({'type': 'image',
                                   'image': 12}), server.ERROR_MESSAGE),
                      (json.dumps({'type': 'image',
                                   'image': '12'}), server.ERROR_MESSAGE)]


@pytest.mark.asyncio
@pytest.mark.parametrize('input, output', MESSAGE_TEST_CASES)
async def test_handle_input_message(input, output):
    assert await server.handle_input_message(input) == output
