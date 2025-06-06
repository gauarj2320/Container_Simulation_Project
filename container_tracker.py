import time
import random
import csv
from datetime import datetime

# ----- Container Class -----
class Container:
    def __init__(self, container_id, weight, destination, priority="standard"):
        self.id = container_id
        self.weight = weight
        self.destination = destination
        self.priority = priority
        self.status = "Arrived at Zone A"

    def __str__(self):
        return f"{self.id} | {self.weight}kg | Dest: {self.destination} | Priority: {self.priority} | Status: {self.status}"

# ----- Movement Logic -----
def move_container(container: Container):
    log = []

    log.append(log_event(container, "Arrived at Zone A"))
    time.sleep(0.5)

    container.status = "Staging at Zone B"
    log.append(log_event(container, "Moved to Zone B"))
    time.sleep(1)

    if container.weight > 2000:
        container.status = "Heavy Route: Zone C → D"
        log.append(log_event(container, "Moved to Zone C"))
        time.sleep(1.2)
        log.append(log_event(container, "Moved to Zone D"))
        time.sleep(1)
    else:
        container.status = "Standard Route: Direct to Zone D"
        log.append(log_event(container, "Moved directly to Zone D"))
        time.sleep(1)

    log.append(log_event(container, "Final delivery complete"))

    return log

# ----- Logging Event -----
def log_event(container: Container, action: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return [timestamp, container.id, container.weight, container.priority, action]

# ----- Generate Container -----
def generate_container(i):
    return Container(
        container_id=f"C{i:03d}",
        weight=random.randint(1000, 4000),
        destination="D",
        priority=random.choice(["urgent", "standard"])
    )

# ----- Write CSV -----
def write_log_to_csv(log_data, filename="container_log.csv"):
    headers = ["Timestamp", "Container ID", "Weight", "Priority", "Action"]
    with open(filename, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(log_data)

# ----- Main -----
def main():
    print(" Maersk Container Movement Simulation with Logging\n")

    containers = [generate_container(i) for i in range(1, 6)]
    all_logs = []

    for c in containers:
        print(f"Processing {c.id}...\n")
        container_logs = move_container(c)
        all_logs.extend(container_logs)
        print(f"{c}\n")

    write_log_to_csv(all_logs)
    print(" CSV log saved as `container_log.csv`.")

if __name__ == "__main__":
    main()
