from core.handler import Handler
from unittest import mock


class TestHandler:
    @mock.patch("core.handler.requests")
    def test_get_activity_with_success(
        self, mock_requests, sample_handler: Handler
    ) -> None:
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "activity": "Learn how to use a french press",
        }
        mock_requests.get.return_value = mock_response

        response = sample_handler._get_activity()

        assert response == "Learn how to use a french press"
        mock_requests.get.assert_called_once()

    @mock.patch("core.handler.requests")
    def test_get_activity_with_fail(
        self, mock_requests, sample_handler: Handler
    ) -> None:
        mock_response = mock.MagicMock()
        mock_response.status_code = 500
        mock_requests.get.return_value = mock_response

        response = sample_handler._get_activity()

        assert response == "Fail get activity, status: 500"
        mock_requests.get.assert_called_once()
