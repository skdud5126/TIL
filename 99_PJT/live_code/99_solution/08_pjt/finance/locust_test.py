from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')

    @task
    def get_data_avg(self):
        self.client.get("test/get_data_avg/")



