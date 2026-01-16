import os
import json
from models.auth import authenticate, register_user
from models.neighbor import Neighbor

def load_neighborhood():
    """Helper to load existing hardware data."""
    if os.path.exists('data/neighborhood.json'):
        with open('data/neighborhood.json', 'r') as f:
            return json.load(f)
    return []

def save_node_to_neighborhood(node_data):
    """Helper to append new hardware data to the database."""
    neighborhood = load_neighborhood()
    neighborhood.append(node_data)
    with open('data/neighborhood.json', 'w') as f:
        json.dump(neighborhood, f, indent=4)

def gateway():
    print("--- ⚡ GridNexus: Energy Portal ⚡ ---")
    email = input("Email: ")
    password = input("Password: ")

    # 1. Try to Authenticate
    node_id = authenticate(email, password)

    if node_id:
        # USER EXISTS -> GO TO DASHBOARD
        print(f"\nWelcome back, {email}!")
        run_dashboard(node_id)
    else:
        # USER NOT FOUND -> REGISTRATION FLOW
        print("\nAccount not found. Let's register your Home Node.")
        confirm = input("Would you like to register? (y/n): ")
        
        if confirm.lower() == 'y':
            # Collect Hardware Data
            name = input("Enter Home Title (e.g., Alice_Home): ")
            try:
                solar = float(input("Solar Capacity (kWp): "))
                battery = float(input("Battery Capacity (kWh): "))
            except ValueError:
                print("❌ Invalid input. Please use numbers for capacity.")
                return

            # Create Hardware Node
            new_node = Neighbor(name, solar, battery)
            
            # Save User Credentials (Hashing happens inside register_user)
            register_user(email, password, new_node.node_id)
            
            # Save Hardware Data
            save_node_to_neighborhood(new_node.to_dict())
            
            print(f"✅ Registration complete! Node ID: {new_node.node_id}")
            run_dashboard(new_node.node_id)
        else:
            print("Access Denied.")

def run_dashboard(node_id):
    """Placeholder for the Dashboard logic we will build next."""
    print(f"\n--- 📊 DASHBOARD [Node: {node_id}] ---")
    print("Connecting to the Smart Grid...")
    # This is where your GUI or main simulation loop will eventually live.
    print("Current Solar: [LINKING DATA...]")
    print("Battery Level: [LINKING DATA...]")

if __name__ == "__main__":
    gateway()