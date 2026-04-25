from locust import HttpUser, task

class MyUser(HttpUser):

    @task
    def test_add(self):
        with self.client.post(
            "/add",
            json={"a": 1, "b": 2},
            catch_response=True
        ) as response:
            # هذه الأسطر الجديدة لطباعة الرد الحقيقي في الـ Terminal
            print("-" * 30)
            print(f"Status Code: {response.status_code}")
            print(f"Response Text: {response.text}")
            print("-" * 30)
            
            if response.status_code != 200:
                response.failure(f"Status code error: {response.status_code}")
            elif "result" not in response.text:
                response.failure("No result in response")
            else:
                response.success()