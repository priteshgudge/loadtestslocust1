from locust import HttpLocust, TaskSet, task
base_url = "http://catalog.agrostar.in"
catalog_list_url = "/catalogservice/v2/products/?extra=remarks,+procuredBy,+alternateProducts&sortByInventory=true"
feasible_channel_url = "/catalogservice/v2/feasiblechannels?skus=AGS-CN-004,AGS-CN-036"

def get_product_list_mh(l):
    headers = {"Source": "CSRMH",
    "Content-Type": "application/json"}
    l.client.get(catalog_list_url,headers=headers)
    
def get_product_list_rj(l):
    headers = {"Source": "CSRRJ",
    "Content-Type": "application-json"}
    l.client.get(catalog_list_url,headers=headers)
    
def get_product_list_gj(l):
    headers = {"Source": "CSRGJ",
    "Content-Type": "application/json"}
    l.client.get(catalog_list_url,headers=headers)

def get_product_feasible_gj(l):
    headers = {"Source": "CSRGJ",
    "Content-Type": "application/json"}
    l.client.get(feasible_channel_url,headers=headers)


def get_product_feasible_mh(l):
    headers = {"Source": "CSRMH",
    "Content-Type": "application/json"}
    l.client.get(feasible_channel_url,headers=headers)


def get_product_feasible_rj(l):
    headers = {"Source": "CSRRJ",
    "Content-Type": "application/json"}
    l.client.get(feasible_channel_url,headers=headers)


class WebsiteTasks(TaskSet):
    tasks = {get_product_list_mh: 2, 
    get_product_list_rj:2,
    get_product_list_gj:2,
    get_product_feasible_mh:2,
    get_product_feasible_rj:2,
    get_product_feasible_gj:2
    }
    def on_start(self):
        pass
    
        
class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 1000
    max_wait = 15000
