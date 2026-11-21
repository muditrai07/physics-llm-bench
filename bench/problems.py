import yaml

def load_problem(path):
    """Load one problem from a YAML file and return it as a dictionary."""
    with open(path) as f:
        return yaml.safe_load(f)