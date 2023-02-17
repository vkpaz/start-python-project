import requests
from http import HTTPStatus


class Handler:
    ACTIVITY_URL: str = "https://www.boredapi.com/api/activity"

    def _get_activity(self) -> str:
        response = requests.get(self.ACTIVITY_URL)

        if response.status_code == HTTPStatus.OK:
            return response.json()["activity"]

        return f"Fail get activity, status: {response.status_code}"

    def handle(self) -> None:
        print(self._get_activity())
