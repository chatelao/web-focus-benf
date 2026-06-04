import os
import re
import sys

# Map of chapter numbers to titles for both books
CHAPTER_TITLES = {
    "creating_reports": {
        1: "Creating Reports Overview",
        2: "Displaying Report Data",
        3: "Sorting Tabular Reports",
        4: "Selecting Records for Your Report",
        5: "Creating Temporary Fields",
        6: "Including Totals and Subtotals",
        7: "Using Expressions",
        8: "Saving and Reusing Your Report Output",
        9: "Choosing a Display Format",
        10: "Linking a Report to Other Resources",
        11: "Navigating Within an HTML Report",
        12: "Bursting Reports Into Multiple HTML Files",
        13: "Handling Records With Missing Field Values",
        14: "Joining Data Sources",
        15: "Merging Data Sources",
        16: "Formatting Reports: An Overview",
        17: "Creating and Managing a WebFOCUS StyleSheet",
        18: "Controlling Report Formatting",
        19: "Identifying a Report Component in a WebFOCUS StyleSheet",
        20: "Using an External Cascading Style Sheet",
        21: "Laying Out the Report Page",
        22: "Using Headings, Footings, Titles, and Labels",
        23: "Formatting Report Data",
        24: "Creating a Graph",
        25: "Creating Financial Reports With Financial Modeling Language (FML)",
        26: "Creating a Free-Form Report",
        27: "Using SQL to Create Reports",
        28: "Improving Report Processing",
    },
    "describing_data": {
        1: "Understanding a Data Source Description",
        2: "Identifying a Data Source",
        3: "Describing a Group of Fields",
        4: "Describing an Individual Field",
        5: "Describing a Sequential, VSAM, or ISAM Data Source",
        6: "Describing a FOCUS Data Source",
        7: "Defining a Join in a Master File",
        8: "Creating a Business View of a Master File",
        9: "Checking and Changing a Master File: CHECK",
        10: "Providing Data Source Security: DBA",
        11: "Creating and Rebuilding a Data Source",
    }
}

def standardize_chapter_heading(filepath):
    # Detect which book it is based on filepath
    book_key = None
    if "creating_reports" in filepath:
        book_key = "creating_reports"
    elif "describing_data" in filepath:
        book_key = "describing_data"

    if not book_key:
        return False

    # Detect chapter number from filename
    match = re.search(r'chapter(\d+)', filepath)
    if not match:
        return False

    chapter_num = int(match.group(1))
    title = CHAPTER_TITLES.get(book_key, {}).get(chapter_num)

    if not title:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return False

    new_h1 = f"# Chapter {chapter_num}: {title}\n"

    # Check if first line already starts with # Chapter X:
    if lines[0].startswith(f"# Chapter {chapter_num}:"):
        return False

    # Heuristic to remove old header artifacts at the top
    # 1. Skip if it's already the same title or "ChapterX"
    changed = False

    header_indices = []
    for i in range(min(10, len(lines))):
        line_stripped = lines[i].strip()
        # Exact match of ChapterX or title
        if line_stripped == f"Chapter{chapter_num}" or line_stripped == f"Chapter {chapter_num}" or line_stripped == title:
            header_indices.append(i)
        elif line_stripped.startswith(f"Chapter{chapter_num} ") or line_stripped.startswith(f"Chapter {chapter_num} "):
            header_indices.append(i)

    if header_indices:
        # Build new content
        new_lines = [new_h1, "\n"]
        for i in range(len(lines)):
            if i not in header_indices:
                new_lines.append(lines[i])

        # Clean up leading blank lines
        while len(new_lines) > 2 and not new_lines[2].strip():
            new_lines.pop(2)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    else:
        # Just prepend if no artifacts found but it's clearly the right file
        new_lines = [new_h1, "\n"] + lines
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True

def main():
    spec_root = 'specifications'
    files_processed = 0
    files_changed = 0

    spec_dirs = ['creating_reports', 'describing_data']
    for sd in spec_dirs:
        full_sd = os.path.join(spec_root, sd)
        if os.path.isdir(full_sd):
            for filename in sorted(os.listdir(full_sd)):
                if 'chapter' in filename and filename.endswith('.md'):
                    filepath = os.path.join(full_sd, filename)
                    files_processed += 1
                    if standardize_chapter_heading(filepath):
                        files_changed += 1
                        print(f"Standardized: {filepath}")

    print(f"Processed {files_processed} files, changed {files_changed}.")

if __name__ == "__main__":
    main()
