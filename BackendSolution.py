class SensorData:
    def __init__(self, id, value, criticality, data_urgency,device_priority):
        self.data = {
            "id": id,
            "value": value,
            "criticality": criticality,
            "data_urgency": data_urgency,
            "device_priority":device_priority
        }
        self.left = None
        self.right = None

    # Inserting a node
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data["value"] < self.data["value"]:
                if self.left is None:
                    self.left = SensorData(data["id"], data["value"], data["criticality"], data["data_urgency"],data["device_priority"])
                else:
                    self.left.insert(data)
            elif data["value"] > self.data["value"]:
                if self.right is None:
                    self.right = SensorData(data["id"], data["value"], data["criticality"], data["data_urgency"],data["device_priority"])
                else:
                    self.right.insert(data)


# Heap sort implementation
def heapify(arr, n, i,key):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest][key] < arr[l][key]:
        largest = l

    if r < n and arr[largest][key] < arr[r][key]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest,key)


def heapSort(arr,key):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i,key)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0,key)



sensor_data_list = [
    {"id": 1, "value": 10,"criticality": 2, "data_urgency": 3,"device_priority": 1},
    {"id": 2, "value": 5, "criticality": 1, "data_urgency": 2,"device_priority":3},
    {"id": 3, "value": 6, "criticality": 3, "data_urgency": 1,"device_priority":2},
    {"id": 1, "value": 4, "criticality": 2, "data_urgency": 3,"device_priority": 1},
    {"id": 2, "value": 8, "criticality": 1, "data_urgency": 2,"device_priority":3},
    {"id": 3, "value": 7, "criticality": 3, "data_urgency": 1,"device_priority":2}
]

# Insert data into binary tree
root = SensorData(sensor_data_list[0]["id"], sensor_data_list[0]["value"], sensor_data_list[0]["criticality"],
                  sensor_data_list[0]["data_urgency"],sensor_data_list[0]["device_priority"])

for data in sensor_data_list[1:]:
    root.insert(data)

# Print in-order traversal of binary tree
def inOrderTraversal(root):
    if root is None:
        return
    else:
        inOrderTraversal(root.left)
        print(root.data, end="\n")
        inOrderTraversal(root.right)

print("In-order traversal of binary tree:")
inOrderTraversal(root)

# Sort data using heap sort based on 'value' key
str=input("\nEnter sorting criteria (Value / Criticality / Data_Urgency / Device_Priority : ")
heapSort(sensor_data_list,str)

print("\n\nSorted Sensor Data after heap sort:")
for data in sensor_data_list:
    print(data, end="\n")

