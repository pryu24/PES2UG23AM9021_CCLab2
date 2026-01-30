from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def view_events(self):
        with self.client.get(
            "/events",
            params={"user": "locust_user"},
            name="/events?user=<user>",
            catch_response=True
        ) as res:
            if res.status_code != 200:
                res.failure(f"Bad status: {res.status_code}")
            elif "events" not in res.text.lower():
                res.failure("Events not found in response")
            else:
                res.success()
