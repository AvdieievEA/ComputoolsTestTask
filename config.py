import os

DATABASE_NAME = "test_database.json"
DEBUG = os.getenv('SUPERBENCHMARK_DEBUG', 'False') == 'True'
