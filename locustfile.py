from locust import HttpLocust, TaskSet, task, between

class MyTaskSet(TaskSet):
    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def about(self):
        self.client.post("/", {"numberInput":500, "submit":'Submit'})

class MyLocust(HttpLocust):
    task_set = MyTaskSet
    wait_time = between(5, 9)