class Config:
    # Debug mode for development
    DEBUG = True
    # Path to SQLite database or other DB
    DB_PATH = "/home/pmello/.openclaw/workspace-swarm/projects/spark-app/src/spark.db"
    # Root path for swarm workspace
    SWARM_WORKSPACE = "/home/pmello/.openclaw/workspace-swarm"
    # Optional: other paths
    LOG_DIR = SWARM_WORKSPACE + "/logs"
    DATA_DIR = SWARM_WORKSPACE + "/data"
