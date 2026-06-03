import os
import re
import sys

# Define book titles to be removed
BOOK_TITLES = [
    "Creating Reports With TIBCO® WebFOCUS Language",
    "Describing Data With TIBCO WebFOCUS® Language"
]

def cleanup_content(content):
    # Normalize line endings
    content = content.replace('\r\n', '\n')

    # 1. Identify and remove Chapter X at the beginning of the file
    content = re.sub(r'^Chapter\s?\d+\s*\n+', '', content, flags=re.IGNORECASE)

    lines = content.split('\n')
    to_remove = set()

    # 2. Identify standalone chapter headers (e.g. "2. Displaying Report Data") that follow \f
    ff_header_pattern = re.compile(r'\f\s*(\d+\.\s+[^\n]+)')
    for match in ff_header_pattern.finditer(content):
        header_text = match.group(1).strip()
        # Find all occurrences of this header text as a standalone line and mark for removal
        for i in range(len(lines)):
            if lines[i].strip() == header_text:
                to_remove.add(i)

    # 3. Identify and remove book titles and nearby page numbers
    for i in range(len(lines)):
        stripped = lines[i].strip()
        if stripped in BOOK_TITLES:
            to_remove.add(i)
            # Look backwards for a page number, skipping blank lines
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0 and re.match(r'^\s*\d+\s*$', lines[j]):
                to_remove.add(j)

            # Look forwards for a page number, skipping blank lines
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and re.match(r'^\s*\d+\s*$', lines[j]):
                to_remove.add(j)

    # Build new lines skipping marked ones
    new_lines = []
    for i in range(len(lines)):
        if i not in to_remove:
            new_lines.append(lines[i])

    content = '\n'.join(new_lines)

    # 4. Remove all form-feed characters
    content = content.replace('\f', '')

    # Task 1.3: Normalize excessive blank lines (4+ newlines) to exactly three
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    return content

def cleanup_file(filepath):
    if not os.path.isfile(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = cleanup_content(content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

def main():
    spec_root = 'specifications'
    files_to_clean = []

    if len(sys.argv) > 1:
        files_to_clean = sys.argv[1:]
    else:
        spec_dirs = ['creating_reports', 'describing_data']
        for sd in spec_dirs:
            full_sd = os.path.join(spec_root, sd)
            if os.path.isdir(full_sd):
                for filename in sorted(os.listdir(full_sd)):
                    if filename.endswith('.md'):
                        files_to_clean.append(os.path.join(full_sd, filename))

    for filepath in files_to_clean:
        if cleanup_file(filepath):
            print(f"Cleaned up: {filepath}")
        else:
            print(f"No changes: {filepath}")

if __name__ == "__main__":
    main()
