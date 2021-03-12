import pytest
import os

from unittest import mock
from yamltopy import main
from tests.expected import EXPECTED

_DEFAULT_OUTPUT = 'tmp/output.py'
_DEFAULT_OUTPUT_MODULE = 'tmp.output'


def run(input=None, output=_DEFAULT_OUTPUT, name=None):
    argv = ['yamltopy/yamltopy.py']
    if input:
        argv.append('-i')
        argv.append(input)
    argv.append('-o')
    argv.append(output)
    if name:
        argv.append('-n')
        argv.append(name)
    if os.path.exists(output):
        os.remove(output)
    print(f'argv: {argv}')
    return mock.patch('sys.argv', argv)


def import_output(output=_DEFAULT_OUTPUT):
    assert os.path.exists(output), 'output file does not exist'
    folder = os.path.dirname(output)
    if folder:
        os.system(f'touch {folder}/__init__.py')
    output_module = output.replace('/', '.').replace('.py', '')
    print(f'output_module: {output_module}')
    return __import__(output_module, fromlist=[None])


def test_should_fail_if_input_is_not_found():
    with run(input='no-file-like-this.yaml'):
        with pytest.raises(FileNotFoundError):
            main()


def test_should_handle_json():
    output_file = 'tmp/output1.py'
    with run(input='tests/not-yaml.json', output=output_file):
        main()
        output = import_output(output_file)
        assert output.DATA is not None, 'variable name is not correct'
        assert output.DATA == {'foo': 'bar'}, 'data is not saved properly'


def test_should_handle_yaml():
    output_file = 'tmp/output2.py'
    with run(input='tests/test.yaml', output=output_file):
        main()
        output = import_output(output_file)
        assert output.DATA is not None, 'variable name is not correct'
        assert output.DATA == EXPECTED, 'data is not saved properly'

def test_should_handle_custom_name():
    output_file = 'tmp/output3.py'
    with run(input='tests/test.yaml', output=output_file, name='CUSTOM'):
        main()
        output = import_output(output_file)
        assert output.CUSTOM is not None, 'variable name is not correct'
        assert output.CUSTOM == EXPECTED, 'data is not saved properly'
