import glob

from fastapi import FastAPI
from fastapi import Request
from pypendency.builder import ContainerBuilder
from pypendency.loaders.py_loader import PyLoader
from pypendency.loaders.yaml_loader import YamlLoader

__all__ = ["Pypendency","get_container","ContainerBuilder"]


DEFAULT_DI_FOLDER_NAME = "_dependency_injection"


class Pypendency:
    container: ContainerBuilder = None

    def __init__(
        self,
        app: FastAPI = None,
        di_folder_name: str = DEFAULT_DI_FOLDER_NAME,
        discover_paths: list[str] = None,
    ):
        self.app = app
        if app is not None:
            self.__init_pypendency(
                app,
                di_folder_name,
                discover_paths,
            )

    def __init_pypendency(
        self,
        app: FastAPI,
        di_folder_name: str,
        discover_paths: list[str],
    ) -> None:
        # Build the container
        container = ContainerBuilder([])

        # Add the container to the app
        app.pypendency = self
        app.pypendency.container = container

        # Load dependencies
        py_loader = PyLoader(container)
        yaml_loader = YamlLoader(container)

        for registered_place in discover_paths:
            for di_folder in glob.glob(
                f"{registered_place}/**/{di_folder_name}", recursive=True
            ):
                py_loader.load_dir(di_folder)
                yaml_loader.load_dir(di_folder)


def get_container(request: Request) -> ContainerBuilder:
    return request.app.pypendency.container
