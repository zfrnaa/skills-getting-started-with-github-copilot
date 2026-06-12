import copy
from typing import Any, Dict, Generator

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


@pytest.fixture(scope="function")
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities() -> Generator[None, None, None]:
    original_activities: Dict[str, Dict[str, Any]] = copy.deepcopy(activities)
    yield
    activities.clear()
    activities.update(copy.deepcopy(original_activities))
