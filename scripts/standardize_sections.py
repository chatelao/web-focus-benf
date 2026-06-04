import os
import re
import sys

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Identify the TOC block
    toc_match = re.search(r'In this (?:chapter|appendix):\s*\n+(.*?)(?:\n\n|\n#)', content, re.DOTALL | re.IGNORECASE)
    if not toc_match:
        return False

    toc_text = toc_match.group(1)
    sections = [s.strip() for s in toc_text.split('\n') if s.strip()]
    if not sections:
        return False

    lines = content.split('\n')
    toc_end_line_idx = content[:toc_match.end()].count('\n')

    changed = False
    last_idx = toc_end_line_idx

    # Keep track of which sections we've already converted to headers in this file
    converted_sections = set()

    for section in sections:
        if section in converted_sections:
            continue

        # Search for this section title as a standalone line
        for i in range(last_idx, len(lines)):
            line_stripped = lines[i].strip()

            # If it's already a header with this title, consider it done
            if lines[i].startswith('#') and line_stripped.lstrip('#').strip() == section:
                converted_sections.add(section)
                last_idx = i + 1
                break

            if line_stripped == section:
                # Found it! Apply H2 header
                lines[i] = f"## {section}"
                converted_sections.add(section)
                last_idx = i + 1
                changed = True
                break

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        return True
    return False

def main():
    spec_root = 'specifications'
    spec_dirs = ['creating_reports', 'describing_data']
    total_files_changed = 0

    for sd in spec_dirs:
        full_sd = os.path.join(spec_root, sd)
        if os.path.isdir(full_sd):
            filenames = sorted(os.listdir(full_sd))
            for filename in filenames:
                if filename.endswith('.md') and ('chapter' in filename or 'appendix' in filename):
                    filepath = os.path.join(full_sd, filename)
                    if process_file(filepath):
                        print(f"Standardized sections in: {filepath}")
                        total_files_changed += 1

    print(f"Processed files, changed {total_files_changed}.")

if __name__ == "__main__":
    main()
