# Autonomous Delivery Robot

This project simulates an **autonomous delivery robot** navigating a 15x15 grid city environment with obstacles and delivery points. The robot uses informed search algorithms like **A*** and **Recursive Best-First Search (RBFS)** to plan optimal paths for delivering packages.

---

## **Features**
- **City Grid Representation:**
  - 15x15 grid with random obstacles (buildings, vehicles).
  - Randomly generated delivery points.

- **Search Algorithms:**
  - A* search with Euclidean distance heuristic.
  - RBFS algorithm for comparison.
  - Path cost between nodes randomly set between 1 and 20.

- **Dynamic Environment:**
  - Vehicles (dynamic obstacles) are moved after each delivery.
  - Robot adapts path planning in real-time.

- **Path Execution:**
  - Robot executes planned paths to reach 5 delivery points sequentially.
  - Start position updates after each delivery.

- **Visualization:**
  - Real-time grid visualization using `matplotlib`.
  - Obstacles, delivery points, and robot paths displayed.

- **Performance Evaluation:**
  - Compares A* vs RBFS in terms of cost, time, and expanded nodes.

- **Bonus:**
  - Extendable for multi-robot coordination.

---

## **Project Structure**
```
autonomous_delivery_robot/
├── main.py                # Entry point of the project
├── environment.py         # Grid and environment representation
├── search_algorithms.py   # A* and RBFS implementations
├── heuristics.py          # Heuristic functions (Euclidean distance)
├── robot.py               # Robot logic and path execution
├── visualization.py       # Visualization using matplotlib
├── dynamic_env.py         # Dynamic updates for vehicles/obstacles
└── tests/                 # Unit tests (optional)
```

---

## **Installation & Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/autonomous-delivery-robot.git
   cd autonomous-delivery-robot
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv env
   source env/bin/activate   # For Linux/Mac
   env\Scripts\activate      # For Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**
Run the main simulation:
```bash
python main.py
```

The robot will plan and execute paths to all delivery points, with real-time visualization of movements and obstacles.

---

## **Dependencies**
- Python 3.9+
- matplotlib
- numpy
- pygame *(optional for advanced visualization)*

Install them manually if you don't have a `requirements.txt` file:
```bash
pip install matplotlib numpy pygame
```

---

## **Future Enhancements**
- Add **multi-robot coordination**.
- GUI using **Tkinter** or **PyQt** for interactive simulation.
- Save performance metrics to logs or CSV.

---

## **License**
This project is released under the MIT License.
