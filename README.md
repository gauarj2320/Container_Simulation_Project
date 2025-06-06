

# 🚢 Container Movement Simulation and Logging System

![Status](https://img.shields.io/badge/Status-Completed-blue) ![Python](https://img.shields.io/badge/Python-3.10+-yellow) ![CSV](https://img.shields.io/badge/Data-Logged%20in%20CSV-green)

## 📦 Project Overview

This project simulates the **movement of containers** through various zones in a port or logistics hub and **logs the actions and events** in a structured CSV file. It is useful for understanding container routing logic, basic logistics automation, and event tracking in real-time systems.

> Built using Python, this tool models realistic scenarios like routing based on **container weight** and **priority**, making it relevant for maritime logistics and supply chain automation.

---

## 🎯 Objectives

- Simulate real-world container routing through multiple port zones
- Handle dynamic routing based on container weight and priority
- Log timestamps and container states for monitoring and traceability
- Generate CSV logs to mimic actual operational data for analytics

---

## 🛠️ Tech Stack

| Category       | Tools Used      |
|----------------|-----------------|
| Language       | Python 3.10+     |
| File Handling  | CSV Module       |
| Timing Events  | `datetime`, `time` |
| Random Data    | `random`         |

---

## 🔄 Simulation Logic

1. **Container Initialization**  
   - Each container is randomly assigned an ID, weight (1000–4000kg), destination, and priority (standard/urgent).

2. **Routing Rules**
   - If `weight > 2000kg`: Routed via Zone C → Zone D (Heavy Route)
   - Else: Directly routed to Zone D (Standard Route)

3. **Zones & Events**
   - Zone A → Zone B (Staging) → Zone C/D → Final Delivery

4. **Event Logging**
   - Every step is logged with a timestamp, container ID, weight, priority, and event description.

---

## 📂 File Structure

```

container-simulation/
├── main.py                  # Main script to run simulation
├── container\_log.csv        # Generated log file after execution
├── README.md                # Project documentation

````

---

## 🧪 Sample Log Output (CSV)

| Timestamp           | Container ID | Weight (kg) | Priority | Action                   |
|---------------------|--------------|-------------|----------|--------------------------|
| 2025-06-06 15:30:12 | C001         | 3100        | urgent   | Arrived at Zone A        |
| 2025-06-06 15:30:13 | C001         | 3100        | urgent   | Moved to Zone B          |
| 2025-06-06 15:30:15 | C001         | 3100        | urgent   | Moved to Zone C          |
| 2025-06-06 15:30:16 | C001         | 3100        | urgent   | Moved to Zone D          |
| 2025-06-06 15:30:17 | C001         | 3100        | urgent   | Final delivery complete  |

---

## ▶️ How to Run

1. **Clone the Repository**

```bash
git clone https://github.com/<your-username>/container-simulation.git
cd container-simulation
````

2. **Run the Simulation**

```bash
python main.py
```

3. **Output**

* `container_log.csv` will be generated with all simulation logs.

---

## 📌 Real-World Relevance

This project demonstrates concepts in:

* **Logistics automation**
* **Real-time event logging**
* **Smart routing based on weight/load**
* **Digital twin simulations for container flow**

🔹 Especially useful for companies like **Maersk**, DP World, or port authorities exploring digital logistics and automation.

---

## 🔮 Future Enhancements

* Integration with **sensors and microcontrollers (ESP32)** for real-time tracking
* Real-time **dashboard (e.g., using Dash or Streamlit)**
* Incorporate **RFID/barcode data simulation**
* Add **priority queue optimization** for urgent containers

---

