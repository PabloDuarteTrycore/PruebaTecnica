"""
Integration tests for project API endpoints.
"""

import json


# ─── Helpers ──────────────────────────────────────────────────────────────────


def create_project(client, name="Test Project", description=None):
    """Helper to create a project in tests."""
    payload = {"name": name}
    if description:
        payload["description"] = description
    return client.post(
        "/api/v1/projects/",
        data=json.dumps(payload),
        content_type="application/json",
    )


# ─── POST /api/v1/projects/ ───────────────────────────────────────────────────


class TestCreateProject:
    """Tests for creating projects."""

    def test_returns_201_with_valid_payload(self, client):
        """Test successful project creation returns 201."""
        response = create_project(client, name="Bridge Construction")
        assert response.status_code == 201

    def test_response_contains_required_fields(self, client):
        """Test response includes all required fields."""
        response = create_project(client, name="Bridge Construction")
        data = response.get_json()
        assert "id" in data
        assert "name" in data
        assert "evm" in data
        assert data["name"] == "Bridge Construction"

    def test_evm_fields_are_zero_for_new_project(self, client):
        """Test that a new project has zero EVM metrics."""
        response = create_project(client, name="Empty Project")
        evm = response.get_json()["evm"]
        assert evm["total_bac"] == "0"
        assert evm["cpi"] is None
        assert evm["cpi_interpretation"] == "insufficient_data"

    def test_returns_422_when_name_is_missing(self, client):
        """Test validation error when name is missing."""
        response = client.post(
            "/api/v1/projects/",
            data=json.dumps({"description": "No name"}),
            content_type="application/json",
        )
        assert response.status_code == 422

    def test_returns_422_when_name_is_empty_string(self, client):
        """Test validation error when name is empty."""
        response = client.post(
            "/api/v1/projects/",
            data=json.dumps({"name": ""}),
            content_type="application/json",
        )
        assert response.status_code == 422


# ─── GET /api/v1/projects/ ────────────────────────────────────────────────────


class TestListProjects:
    """Tests for listing projects."""

    def test_returns_200_with_empty_list(self, client):
        """Test listing projects returns 200 with empty list."""
        response = client.get("/api/v1/projects/")
        assert response.status_code == 200
        assert response.get_json() == []

    def test_returns_created_projects(self, client):
        """Test listing returns created projects."""
        create_project(client, name="Project Alpha")
        create_project(client, name="Project Beta")
        response = client.get("/api/v1/projects/")
        data = response.get_json()
        assert len(data) == 2

    def test_each_project_has_evm_field(self, client):
        """Test that each project includes EVM indicators."""
        create_project(client, name="Project Alpha")
        projects = client.get("/api/v1/projects/").get_json()
        assert "evm" in projects[0]


# ─── GET /api/v1/projects/{id} ────────────────────────────────────────────────


class TestGetProjectDetail:
    """Tests for getting project detail."""

    def test_returns_200_for_existing_project(self, client):
        """Test getting existing project returns 200."""
        project_id = create_project(client).get_json()["id"]
        response = client.get(f"/api/v1/projects/{project_id}")
        assert response.status_code == 200

    def test_response_includes_activities_list(self, client):
        """Test response includes activities list."""
        project_id = create_project(client).get_json()["id"]
        data = client.get(f"/api/v1/projects/{project_id}").get_json()
        assert "activities" in data
        assert isinstance(data["activities"], list)

    def test_returns_404_for_nonexistent_project(self, client):
        """Test getting nonexistent project returns 404."""
        response = client.get(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000"
        )
        assert response.status_code == 404

    def test_404_response_is_json(self, client):
        """Test 404 response includes error information."""
        response = client.get(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000"
        )
        data = response.get_json()
        assert "error" in data
        assert "message" in data


# ─── PUT /api/v1/projects/{id} ────────────────────────────────────────────────


class TestUpdateProject:
    """Tests for updating projects."""

    def test_returns_200_with_updated_name(self, client):
        """Test updating project name returns 200."""
        project_id = create_project(client, name="Original").get_json()["id"]
        response = client.put(
            f"/api/v1/projects/{project_id}",
            data=json.dumps({"name": "Updated Name"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["name"] == "Updated Name"

    def test_returns_404_for_nonexistent_project(self, client):
        """Test updating nonexistent project returns 404."""
        response = client.put(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000",
            data=json.dumps({"name": "Updated"}),
            content_type="application/json",
        )
        assert response.status_code == 404


# ─── DELETE /api/v1/projects/{id} ─────────────────────────────────────────────


class TestDeleteProject:
    """Tests for deleting projects."""

    def test_returns_204_for_existing_project(self, client):
        """Test deleting existing project returns 204."""
        project_id = create_project(client).get_json()["id"]
        response = client.delete(f"/api/v1/projects/{project_id}")
        assert response.status_code == 204

    def test_project_is_gone_after_delete(self, client):
        """Test project is deleted after delete request."""
        project_id = create_project(client).get_json()["id"]
        client.delete(f"/api/v1/projects/{project_id}")
        get_response = client.get(f"/api/v1/projects/{project_id}")
        assert get_response.status_code == 404

    def test_returns_404_for_nonexistent_project(self, client):
        """Test deleting nonexistent project returns 404."""
        response = client.delete(
            "/api/v1/projects/00000000-0000-0000-0000-000000000000"
        )
        assert response.status_code == 404
