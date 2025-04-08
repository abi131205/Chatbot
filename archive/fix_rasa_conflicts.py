import yaml
import os
import re

def load_yaml(file_path):
    """Load a YAML file and return its content."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def save_yaml(file_path, data):
    """Save data to a YAML file."""
    with open(file_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True, sort_keys=False)

def fix_conflicting_rules():
    """Detect and remove conflicting rules in Rasa."""
    rules_path = "data/rules.yml"
    stories_path = "data/stories.yml"

    rules_data = load_yaml(rules_path)
    stories_data = load_yaml(stories_path)

    if not rules_data or not stories_data:
        print("⚠️ Could not find rules.yml or stories.yml")
        return

    fixed_rules = []
    fixed_stories = []
    conflicts_removed = 0

    # Extract existing rules and stories
    rules = rules_data.get("rules", [])
    stories = stories_data.get("stories", [])

    rule_intents = {}
    
    # Index rules by intent
    for rule in rules:
        steps = rule.get("steps", [])
        for step in steps:
            if "intent" in step:
                intent = step["intent"]
                rule_intents[intent] = rule["rule"]

    # Check for conflicts
    for story in stories:
        steps = story.get("steps", [])
        conflicting = False
        for step in steps:
            if "intent" in step and step["intent"] in rule_intents:
                print(f"❌ Conflict found: {story['story']} contradicts rule {rule_intents[step['intent']]}")
                conflicting = True
                conflicts_removed += 1
                break  # Stop checking this story

        if not conflicting:
            fixed_stories.append(story)

    # Save fixed stories and rules
    stories_data["stories"] = fixed_stories
    save_yaml(stories_path, stories_data)

    print(f"✅ {conflicts_removed} conflicting stories removed!")

    return conflicts_removed

if __name__ == "__main__":
    conflicts = fix_conflicting_rules()
    if conflicts > 0:
        print("🔄 Retrying Rasa training after fixing...")
        os.system("rasa train")
    else:
        print("✅ No conflicts found, ready to train Rasa!")
