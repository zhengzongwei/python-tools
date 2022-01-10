import docker

client = docker.from_env()


class Docker(object):
    def __init__(self):
        print("[__init__] docker client init")
        self.client = docker.from_env()

    def get_version(self):
        return self.client.version()

    def get_info(self):
        return self.client.info()

    def ping(self):
        return self.client.ping()

    def __del__(self):
        print("[__del__] docker client close")
        self.client.close()


class DockerImage(Docker):

    def get_image_list(self, show_all=True):
        image_info_list = []
        images = self.client.images.list(all=show_all)
        for _image in images:
            image_info_list.append(_image.attrs)
        return image_info_list


class DockerContainer(Docker):

    def get_container_list(self):
        container_info_list = []
        containers = self.client.containers.list()
        for _container in containers:
            container_info_list.append(_container.attrs)
        return container_info_list


if __name__ == '__main__':
    # docker = Docker()
    # print(docker.ping())
    image = DockerContainer()
    print(image.get_container_list())
    # container = DockerContainer()
    # print(container.get_container_list())
