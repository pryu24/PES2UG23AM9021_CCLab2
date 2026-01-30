from locust import HttpUser, task, between

class MyEventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_my_events(self):
        self.client.get(
            "/my-events",
            params={"user": "locust_user"},
            name="/my-events?user=<user>"
        )
