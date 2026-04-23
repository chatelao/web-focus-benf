import os
import re

def split_manual(filepath, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by form feed character
    pieces = content.split('\f')

    section_count = 0

    # We'll use a helper to get a nice filename
    def get_filename(count, title):
        title = title.lower().strip()
        title = re.sub(r'[^a-z0-9]+', '_', title)
        title = title.strip('_')
        return f"{count:02d}_{title}.md"

    # The first pieces might be front matter until we hit a Chapter or Appendix
    current_content = []
    current_title = "front_matter"

    for piece in pieces:
        # Check if this piece starts a new section
        stripped_piece = piece.strip()
        # Restrict headers to Chapter and Appendix to avoid splitting on every 'Contents' page
        match = re.match(r'^(Chapter\s*\d+|Appendix\s*[A-Z])', stripped_piece)

        if match:
            # Save previous section if it has content
            if current_content:
                with open(os.path.join(target_dir, get_filename(section_count, current_title)), 'w', encoding='utf-8') as f:
                    f.write('\f'.join(current_content))
                section_count += 1

            # Start new section
            current_title = match.group(1)
            current_content = [piece]
        else:
            current_content.append(piece)

    # Save the last section
    if current_content:
        with open(os.path.join(target_dir, get_filename(section_count, current_title)), 'w', encoding='utf-8') as f:
            f.write('\f'.join(current_content))

if __name__ == "__main__":
    # Clean up previous attempts if any
    import shutil
    for d in ['specifications/creating_reports', 'specifications/describing_data']:
        if os.path.exists(d):
            shutil.rmtree(d)
            os.makedirs(d)

    split_manual('specifications/TIB_wfwf_8207.27.0_cr_language.md', 'specifications/creating_reports')
    split_manual('specifications/TIB_wfwf_8207.27.0_dd_language.md', 'specifications/describing_data')
