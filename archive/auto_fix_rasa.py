import os
import yaml

# Define file paths
rules_file = "data/rules.yml"
stories_file = "data/stories.yml"

def remove_conflicting_entries():
    """Removes conflicting rules and stories automatically"""
    try:
        # Load and clean rules
        with open(rules_file, "r", encoding="utf-8") as f:
            rules = yaml.safe_load(f)
        
        if "rules" in rules:
            unique_rules = {str(rule): rule for rule in rules["rules"]}  # Remove duplicates
            rules["rules"] = list(unique_rules.values())

        with open(rules_file, "w", encoding="utf-8") as f:
            yaml.dump(rules, f, default_flow_style=False)

        # Load and clean stories
        with open(stories_file, "r", encoding="utf-8") as f:
            stories = yaml.safe_load(f)

        if "stories" in stories:
            unique_stories = {str(story): story for story in stories["stories"]}  # Remove duplicates
            stories["stories"] = list(unique_stories.values())

        with open(stories_file, "w", encoding="utf-8") as f:
            yaml.dump(stories, f, default_flow_style=False)

        print("✅ Conflicting rules and stories removed automatically!")

    except Exception as e:
        print(f"❌ Error while fixing conflicts: {e}")

# Run automated fixes
remove_conflicting_entries()

# Retrain Rasa after cleaning
os.system("rasa train")
