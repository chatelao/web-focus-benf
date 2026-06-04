import os
import sys

def format_title(filepath):
    if not os.path.isfile(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return False

    # Find the first non-empty line
    first_non_empty_idx = -1
    for i, line in enumerate(lines):
        if line.strip():
            first_non_empty_idx = i
            break

    if first_non_empty_idx == -1:
        return False

    first_line = lines[first_non_empty_idx]

    # If it's already an H1 header, skip
    if first_line.startswith('# '):
        return False

    # Prepend #
    lines[first_non_empty_idx] = f"# {first_line}"

    # Ensure there's a blank line after the title
    if first_non_empty_idx + 1 < len(lines):
        if lines[first_non_empty_idx + 1].strip():
            lines.insert(first_non_empty_idx + 1, '\n')
    else:
        lines.append('\n')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)

    return True

def main():
    spec_root = 'specifications'
    spec_dirs = ['creating_reports', 'describing_data']
    files_processed = 0
    files_updated = 0

    for sd in spec_dirs:
        full_sd = os.path.join(spec_root, sd)
        if os.path.isdir(full_sd):
            for filename in sorted(os.listdir(full_sd)):
                if filename.endswith('.md'):
                    filepath = os.path.join(full_sd, filename)
                    files_processed += 1
                    if format_title(filepath):
                        files_updated += 1
                        print(f"Updated: {filepath}")

    print(f"Total files processed: {files_processed}")
    print(f"Total files updated: {files_updated}")

if __name__ == "__main__":
    main()
