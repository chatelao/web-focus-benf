import os
import re
import sys

# Regex patterns for book titles
BOOK_TITLE_PATTERNS = [
    re.compile(r'Creating Reports With TIBCO®?\s*WebFOCUS Language', re.IGNORECASE),
    re.compile(r'Describing Data With TIBCO\s*WebFOCUS®?\s*Language', re.IGNORECASE),
    re.compile(r'Describing Data With TIBCO®?\s*WebFOCUS Language', re.IGNORECASE),
]

def cleanup_content(content):
    # Normalize line endings
    content = content.replace('\r\n', '\n')

    # 1. Identify and remove Chapter X at the beginning of the file
    content = re.sub(r'^Chapter\s?\d+\s*\n+', '', content, flags=re.IGNORECASE)

    lines = content.split('\n')
    to_remove = set()

    # 2. Identify and remove book titles and nearby page numbers
    for i in range(len(lines)):
        stripped = lines[i].strip()
        if not stripped:
            continue

        is_book_title = any(pattern.fullmatch(stripped) for pattern in BOOK_TITLE_PATTERNS)
        if not is_book_title:
             # Try partial match if full match fails, but keep it reasonably constrained
             is_book_title = any(pattern.search(stripped) and len(stripped) < 80 for pattern in BOOK_TITLE_PATTERNS)

        if is_book_title:
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

    # 3. Identify standalone chapter headers (e.g. "2. Displaying Report Data") that follow \f
    ff_header_pattern = re.compile(r'\f\s*(\d+\.\s+[^\n]+)')
    for match in ff_header_pattern.finditer(content):
        header_text = match.group(1).strip()
        for i in range(len(lines)):
            if lines[i].strip() == header_text:
                to_remove.add(i)

    # 4. Task 1.2.2: Remove isolated page numbers
    # Improved heuristic: A number is likely a page number if it's on a line by itself
    # and is near a form-feed (\f) character (before or after it, with only whitespace in between)
    # OR it's at the very end of the file.
    for i in range(len(lines)):
        if i in to_remove:
            continue

        if re.match(r'^\s*\d+\s*$', lines[i]):
            is_page_num = False

            # Check proximity to \f
            j = i - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            if j >= 0 and '\f' in lines[j]:
                is_page_num = True

            if not is_page_num:
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j < len(lines) and '\f' in lines[j]:
                    is_page_num = True

            # Check if it's the last non-empty line in the file
            if not is_page_num:
                j = i + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1
                if j == len(lines):
                    is_page_num = True

            if is_page_num:
                to_remove.add(i)

    # Build new lines skipping marked ones
    new_lines = []
    for i in range(len(lines)):
        if i not in to_remove:
            new_lines.append(lines[i])

    content = '\n'.join(new_lines)

    # 5. Remove all form-feed characters
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
