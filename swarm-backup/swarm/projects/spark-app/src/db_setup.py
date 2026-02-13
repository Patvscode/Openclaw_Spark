"""Database setup for Spark App.

Creates all tables and seeds agent data for Spark, Bob, and Alpha-Hotel.
"""

from models import create_tables, insert_agent

if __name__ == "__main__":
    # Ensure tables exist
    create_tables()

    # Seed agents
    agents = [
        {"name": "Spark", "model": "gpt-4o", "workspace": "spark", "status": "idle", "last_active": None},
        {"name": "Bob", "model": "gpt-4o-mini", "workspace": "bob", "status": "idle", "last_active": None},
        {"name": "Alpha", "model": "gpt-4o-mini", "workspace": "alpha", "status": "idle", "last_active": None},
        {"name": "Beta", "model": "gpt-4o-mini", "workspace": "beta", "status": "idle", "last_active": None},
        {"name": "Gamma", "model": "gpt-4o-mini", "workspace": "gamma", "status": "idle", "last_active": None},
        {"name": "Delta", "model": "gpt-4o-mini", "workspace": "delta", "status": "idle", "last_active": None},
        {"name": "Echo", "model": "gpt-4o-mini", "workspace": "echo", "status": "idle", "last_active": None},
        {"name": "Foxtrot", "model": "gpt-4o-mini", "workspace": "foxtrot", "status": "idle", "last_active": None},
        {"name": "Golf", "model": "gpt-4o-mini", "workspace": "golf", "status": "idle", "last_active": None},
        {"name": "Hotel", "model": "gpt-4o-mini", "workspace": "hotel", "status": "idle", "last_active": None},
    ]

    for agent in agents:
        # Check if already exists to avoid duplicates
        # For simplicity, just insert
        agent_id = insert_agent(
            name=agent["name"],
            model=agent["model"],
            workspace=agent["workspace"],
            status=agent["status"],
            last_active=agent["last_active"],
        )
        print(f"Inserted agent {agent['name']} with id {agent_id}")

    print("Database setup complete.")
