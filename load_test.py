from locust import HttpLocust, TaskSet, task
import json

# 定义用户行为
class UserBehavior(TaskSet):

    # @task
    # def baidu_index(self):
    #     self.client.get("/")

    @task
    def iuput_job(self):
        headers = {'content-type': 'application/json', 'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwb3RhdG9JZCI6IjgwNTU2MDEiLCJpYXQiOjE1MjIwMjk3Njl9.V_NnkUi_yGhavdsgiWp-jChYRqsQ44f9-s2ARMW8Dd0'}
        payload = {"content": "echon88888ccccc", "type": "sh"}
        r = self.client.put("/automations/scripts/editor/gg12345", data=json.dumps(payload), headers=headers)
        json_response = json.loads(r.text)
        print(json_response)
        assert r.status_code is 200, "Unexpected response code: " + str(r.status_code)



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000
    host = "https://canary.pentium.network"