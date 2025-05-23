# fastapi-pypendency

Pypendency integration with FastAPI.

Based on
- [Flask-Pypendency](https://pypi.org/project/Flask-Pypendency/)
- [Pypendency](https://pypi.org/project/Pypendency/)


## Installation

```bash
pip install fastapi-pypendency
```

## Usage

Configure your FastAPI app with the `Pypendency` class:
```python
import os
from fastapi import FastAPI
from fastapi_pypendency import Pypendency


app = FastAPI()

Pypendency(
    app,
    "_dependency_injection",
    [os.path.dirname(os.path.abspath(__file__))],  # ["src"],
)
```

A sample controller:
```python
# get_user_controller.py
class GetUserController:
    def get(self) -> dict:
        return {"user": "John Doe"}
```

```yaml
# _dependency_injection/get_user_controller.yaml
GetUserController:
  fqn: get_user_controller.GetUserController
```


On your router:
```python
from fastapi import APIRouter
from fastapi import Request
from fastapi_pypendency import ContainerBuilder
from fastapi_pypendency import get_container
from get_user_controller import GetUserController


router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def get_user(request: Request):
    container: ContainerBuilder = get_container(request)
    controller: GetUserController = container.get("GetUserController")
    return {"id": controller.get()}

```
