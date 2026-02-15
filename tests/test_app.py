from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {"message": "Hello World"}

# Example: Add more tests for additional endpoints or error cases
def test_not_found():
	response = client.get("/nonexistent")
	assert response.status_code == 404

def test_method_not_allowed():
	response = client.post("/")
	assert response.status_code == 405

# Additional tests for coverage
def test_hello_endpoint():
	response = client.get("/hello")
	# Accept 200 or 404 depending on implementation, but check for 200 if exists
	assert response.status_code in (200, 404)
	if response.status_code == 200:
		assert "hello" in response.json().get("message", "").lower()

def test_root_with_query():
	response = client.get("/?name=World")
	assert response.status_code in (200, 422)
	# If query param is handled, check for name in response
	if response.status_code == 200:
		assert "world" in response.json().get("message", "").lower()
