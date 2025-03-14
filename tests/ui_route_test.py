def test_get_ui_tasks(fastapi_testclient, async_minimum):
    response = fastapi_testclient.get("/ui/tasks")
    assert response.status_code == 200
    assert response.json()["recordsTotal"] == 2
