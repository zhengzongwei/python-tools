import sys
sys.path.append('../')
import pytest

from common import logs

LOG = logs.Logger()

# import logging

# module_logger = logging.getLogger('test')


LOG._log("sdsdasTest Docker Class", level="DEBUG")

# class TestDocker():
#     def setup(self):
#         LOG.log("Test Docker Class","DEBUG")

#     def teardown(self):
#         print("docker test")

#     def test_docker(self):
#         pass


# if __name__ == '__main__':
#     pytest.main()
