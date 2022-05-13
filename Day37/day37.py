# Day 37 - Intermediate + Habit Tracking Project: API Post Request & Headers
import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "jiwojfiowemonoianoif",
    "username": "happystep",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Creating user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a graph
# graph_endpoint = "https://pixe.la/v1/users/happystep/graphs"
# headers = {
#     "X-USER-TOKEN": "jiwojfiowemonoianoif",
# }
# graph_params = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)


# Post to graph
# today = datetime.now()
# formatted_date = today.strftime("%Y%m%d")
# headers = {
#     "X-USER-TOKEN": "jiwojfiowemonoianoif",
# }
# pixel_creation_endpoint = "https://pixe.la/v1/users/happystep/graphs/graph1/"
# pixel_data = {
#     "date": "20200513",
#     "quantity": "10.4",
# }
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Update pixel
# headers = {
#    "X-USER-TOKEN": "jiwojfiowemonoianoif",
#  }
# update_endpoint = "https://pixe.la/v1/users/happystep/graphs/graph1/20220513"
#
# new_pixel_data = {
#     "quantity": "4.5",
# }
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete pixel
# headers = {
#    "X-USER-TOKEN": "jiwojfiowemonoianoif",
#  }
# delete_endpoint = "https://pixe.la/v1/users/happystep/graphs/graph1/20220513"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
