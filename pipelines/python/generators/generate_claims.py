"""Standalone wrapper for generate_claims. Use generate_all_synthetic_data.py for full referentially-integrated generation."""
from pipelines.python.generate_all_synthetic_data import generate_claims

if __name__ == "__main__":
    print("Import this generator into an orchestration script to preserve referential integrity.")
