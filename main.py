import docker_api.docker_api as docker_api

print(docker_api.DockerImage().get_image_list())