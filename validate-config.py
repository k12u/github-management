#!/usr/bin/env python3
"""
Validate repository configuration files
"""

import json
import yaml
import sys
from pathlib import Path

def validate_yaml_config():
    """Validate the YAML configuration file"""
    try:
        with open('repositories.yaml', 'r') as f:
            config = yaml.safe_load(f)
        
        if 'repositories' not in config:
            print("ERROR: 'repositories' key not found in YAML config")
            return False
        
        for repo in config['repositories']:
            required_fields = ['name', 'private']
            for field in required_fields:
                if field not in repo:
                    print(f"ERROR: Repository missing required field '{field}': {repo}")
                    return False
        
        print(f"✓ YAML config valid: {len(config['repositories'])} repositories defined")
        return True
    
    except FileNotFoundError:
        print("ERROR: repositories.yaml not found")
        return False
    except yaml.YAMLError as e:
        print(f"ERROR: Invalid YAML syntax: {e}")
        return False

def validate_json_config():
    """Validate the JSON configuration file"""
    try:
        with open('repositories.json', 'r') as f:
            config = json.load(f)
        
        if 'repositories' not in config:
            print("ERROR: 'repositories' key not found in JSON config")
            return False
        
        for repo in config['repositories']:
            required_fields = ['name', 'private']
            for field in required_fields:
                if field not in repo:
                    print(f"ERROR: Repository missing required field '{field}': {repo}")
                    return False
        
        print(f"✓ JSON config valid: {len(config['repositories'])} repositories defined")
        return True
    
    except FileNotFoundError:
        print("ERROR: repositories.json not found")
        return False
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON syntax: {e}")
        return False

def main():
    """Main validation function"""
    print("Validating repository configurations...")
    
    yaml_valid = validate_yaml_config()
    json_valid = validate_json_config()
    
    if yaml_valid and json_valid:
        print("\n✓ All configuration files are valid!")
        return 0
    else:
        print("\n✗ Configuration validation failed!")
        return 1

if __name__ == '__main__':
    sys.exit(main())