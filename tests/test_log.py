import sys
sys.path.append('../')
import pytest

from common import logs

LOG = logs.Logger(__file__)



def main():

    LOG.dlog("sdsdasTest Docker Class", "DEBUG")

main()