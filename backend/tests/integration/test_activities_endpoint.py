"""
Integration tests for activity API endpoints.
"""

import json


# ─── Helpers ──────────────────────────────────────────────────────────────────


def create_project(client, name="Test Project"):
    """Helper to create a project."""
    return client.post(
        "/api/v1/projects/",
        data=json.dumps({"name": name}),
        content_type="application/json",
    ).get_json()


def create_activity(client, project_id, overrides=None):
    """Helper to create an activity."""
    payload = {
        "name": "Foundation Work",
        "bac": "10000",
        "planned_progress": "50",
        "actual_progress": "40",
        "actual_cost": "4500",
    }
    if overrides:
        payload.update(overrides)
    return client.post(
        f"/api/v1/projects/{project_id}/activities",
        data=json.dumps(payload),
        content_type="application/json",
    )


# ─── POST /api/v1/projects/{id}/activities ────────────────────────────────────


class TestCreateActivity:
    """Tests for creating activities."""

    def test_returns_201_with_valid_payload(self, client):
        """Test successful activity creation returns 201."""
        project_id = create_project(client)["id"]
        response = create_activity(client, project_id)
        assert response.status_code == 201

    def test_response_contains_evm_indicators(self, client):
        """Test response includes EVM indicators."""
        project_id = create_project(client)["id"]
        data = create_activity(client, project_id).get_json()
        assert "evm" in data
        evm = data["evm"]
        assert evm["pv"] == "5000.00"
        assert evm["ev"] == "4000.00"
        assert "cpi" in evm
        assert "cpi_interpretation" in evm

    def test_returns_404_when_project_does_not_exist(self, client):
        """Test creating activity in nonexistent project returns 404."""
        response = create_activity(
            client, "00000000-0000-0000-0000-000000000000"
        )
        assert response.status_code == 404

    def test_returns_422_when_progress_exceeds_100(self, client):
        """Test validation error when progress exceeds 100."""
        project_id = create_project(client)["id"]
        response = create_activity(
            client, project_id, overrides={"planned_progress": "150"}
        )
        assert response.status_code == 422

    def test_returns_422_when_bac_is_negative(self, client):
        """Test validation error when BAC is negative."""
        project_id = create_project(client)["id"]
        response = create_activity(
            client, project_id, overrides={"bac": "-500"}
        )
        assert response.status_code == 422

    def test_cpi_is_null_when_actual_cost_is_zero(self, client):
        """Test CPI is None when actual cost is zero."""
        project_id = create_project(client)["id"]
        data = create_activity(
            client, project_id, overrides={"actual_cost": "0"}
        ).get_json()
        assert data["evm"]["cpi"] is None
        assert data["evm"]["cpi_interpretation"] == "insufficient_data"


# ─── GET /api/v1/projects/{id}/activities ─────────────────────────────────────


class TestListActivities:
    """Tests for listing activities."""

    def test_returns_200_with_empty_list(self, client):
        """Test listing activities returns 200 with empty list."""
        project_id = create_project(client)["id"]
        response = client.get(f"/api/v1/projects/{project_id}/activities")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_returns_created_activities(self, client):
        """Test listing returns created activities."""
        project_id = create_project(client)["id"]
        create_activity(client, project_id)
        create_activity(
            client, project_id, overrides={"name": "Second Activity"}
        )
        activities = client.get(
            f"/api/v1/projects/{project_id}/activities"
        ).get_json()
        assert len(activities) == 2

    def test_returns_404_when_project_does_not_exist(self, client):
        """Test listing activities for nonexistent project returns 404."""
        response = client.get(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000/activities"
        )
        assert response.status_code == 404


# ─── PUT /api/v1/activities/{id} ──────────────────────────────────────────────


class TestUpdateActivity:
    """Tests for updating activities."""

    def test_returns_200_with_recalculated_evm(self, client):
        """Test updating activity recalculates EVM indicators."""
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]

        response = client.put(
            f"/api/v1/activities/{activity_id}",
            data=json.dumps(
                {"actual_progress": "80", "actual_cost": "7000"}
            ),
            content_type="application/json",
        )
        assert response.status_code == 200
        evm = response.get_json()["evm"]
        assert evm["ev"] == "8000.00"

    def test_returns_404_for_nonexistent_activity(self, client):
        """Test updating nonexistent activity returns 404."""
        response = client.put(
            "/api/v1/activities/00000000-0000-0000-0000-000000000000",
            data=json.dumps({"actual_progress": "50"}),
            content_type="application/json",
        )
        assert response.status_code == 404

    def test_returns_422_when_progress_is_invalid(self, client):
        """Test validation error when progress is invalid."""
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        response = client.put(
            f"/api/v1/activities/{activity_id}",
            data=json.dumps({"actual_progress": "200"}),
            content_type="application/json",
        )
        assert response.status_code == 422


# ─── DELETE /api/v1/activities/{id} ───────────────────────────────────────────


class TestDeleteActivity:
    """Tests for deleting activities."""

    def test_returns_204_for_existing_activity(self, client):
        """Test deleting existing activity returns 204."""
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        response = client.delete(f"/api/v1/activities/{activity_id}")
        assert response.status_code == 204

    def test_activity_is_gone_after_delete(self, client):
        """Test activity is deleted after delete request."""
        project_id = create_project(client)["id"]
        activity_id = create_activity(client, project_id).get_json()["id"]
        client.delete(f"/api/v1/activities/{activity_id}")
        activities = client.get(
            f"/api/v1/projects/{project_id}/activities"
        ).get_json()
        assert len(activities) == 0

    def test_returns_404_for_nonexistent_activity(self, client):
        """Test deleting nonexistent activity returns 404."""
        response = client.delete(
            "/api/v1/activities/00000000-0000-0000-0000-000000000000"
        )
        assert response.status_code == 404
