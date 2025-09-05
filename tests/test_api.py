import subprocess

def test_api_collection():
    # Run Newman on exported Postman collection
    result = subprocess.run(
        ["newman", "run", "tests/demo_api.json"],
        capture_output=True,
        text=True
    )
    print(result.stdout)  # show full newman output in pytest logs
    assert result.returncode == 0  # test fails if Newman run fails

