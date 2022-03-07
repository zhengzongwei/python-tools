import pytest

from docker_api.docker_api import Docker
from docker_api.docker_api import DockerImage
from docker_api.docker_api import DockerContainer


class TestDocker():
    def setup(self):
        print("Test Docker Class")

    def teardown(self):
        print("docker test")

    def test_docker(self):
        docker = Docker()
        print(docker)


if __name__ == '__main__':
    pytest.main()
