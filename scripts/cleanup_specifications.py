import os

def cleanup_file(filepath):
    """
    Removes form-feed characters from a file.
    This is a safe cleanup step as form-feeds are typically PDF page break artifacts.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove form feed characters
    if '\f' in content:
        content = content.replace('\f', '')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    spec_dir = 'specifications'
    if not os.path.exists(spec_dir):
        print(f"Directory {spec_dir} not found.")
        return

    cleaned_count = 0
    for root, dirs, files in os.walk(spec_dir):
        for file in files:
            # Only process markdown files, excluding the ROADMAP itself
            if file.endswith('.md') and file != 'ROADMAP.md':
                filepath = os.path.join(root, file)
                if cleanup_file(filepath):
                    print(f"Cleaned up form-feeds in: {filepath}")
                    cleaned_count += 1

    print(f"Total files cleaned: {cleaned_count}")

if __name__ == "__main__":
    main()
