# main.py
from models.neighbor import Neighbor
from models.marketplace import CentralController

# 1. Setup neighbors
neighborhood = [
    Neighbor("Node_1", 8.0, 2.0, 10),
    Neighbor("Node_2", 1.0, 5.0, 10),
    # ... add the rest
]

# 2. Initialize Controller
vpp_admin = CentralController(neighborhood)

# 3. Run Simulation Step
def run_tick():
    sellers, buyers = vpp_admin.find_trade_opportunities()
    print(f"Market Open: {len(sellers)} Sellers found, {len(buyers)} Buyers found.")

if __name__ == "__main__":
    run_tick()