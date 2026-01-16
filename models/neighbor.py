import uuid

class Neighbor:
    def __init__(self, name, solar_capacity, battery_capacity, initial_wallet=100.0, node_id=None):
        # Identity - If no ID is provided from the DB, generate a unique one
        self.node_id = node_id if node_id else str(uuid.uuid4())[:8]
        self.name = name
        
        # Hardware Specs (Static limits)
        self.solar_capacity = float(solar_capacity)    # Max possible output (kWp)
        self.battery_capacity = float(battery_capacity) # Max storage (kWh)
        
        # Dynamic States (Current values during simulation)
        self.current_solar = 0.0  # Actual gen at this specific moment
        self.current_demand = 0.0 # Actual load at this specific moment
        self.battery_level = 0.0  # Current kWh in storage
        self.wallet = float(initial_wallet)
        
        # Metadata
        self.status = "Idle" # e.g., "Selling", "Buying", "Charging"

    def to_dict(self):
        """Converts object attributes to a dictionary for JSON storage."""
        return {
            "node_id": self.node_id,
            "name": self.name,
            "solar_capacity": self.solar_capacity,
            "battery_capacity": self.battery_capacity,
            "battery_level": self.battery_level,
            "wallet": self.wallet
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Neighbor object from a dictionary (loading from JSON)."""
        return cls(
            node_id=data['node_id'],
            name=data['name'],
            solar_capacity=data['solar_capacity'],
            battery_capacity=data['battery_capacity'],
            initial_wallet=data['wallet']
        )