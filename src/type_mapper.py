import re

def map_wf_type_to_pg(data_type):
    """
    Maps WebFOCUS types to PostgreSQL types.
    Supports detailed numeric formats (e.g., I8, F8.2, P9.2).
    """
    if not data_type:
        return 'TEXT'

    data_type = data_type.upper()

    if data_type == 'LOGICAL':
        return 'BOOLEAN'
    if data_type.startswith('A'):
        match = re.search(r'A(\d+)', data_type)
        if match:
            return f"CHAR({match.group(1)})"
        return 'TEXT'

    # Date and Date-Time mapping
    if data_type.startswith('H'):
        return 'TIMESTAMP'
    if data_type in ('YYMD', 'MDYY', 'DMYY', 'YMD', 'MDY', 'DMY'):
        return 'DATE'

    # Integer mapping
    if data_type.startswith('I'):
        if '8' in data_type:
            return 'BIGINT'
        return 'INTEGER'

    # Float/Decimal mapping
    if data_type.startswith(('F', 'D', 'P')):
        # Check for precision and scale: e.g., F8.2 or P9.2
        match = re.search(r'([FDP])(\d+)(?:\.(\d+))?', data_type)
        if match:
            type_char = match.group(1)
            precision = match.group(2)
            scale = match.group(3)

            if scale:
                return f"NUMERIC({precision}, {scale})"

            if type_char in ('F', 'D'):
                return 'DOUBLE PRECISION'

            return f"NUMERIC({precision}, 0)"

        if data_type.startswith(('F', 'D')):
            return 'DOUBLE PRECISION'
        if data_type.startswith('P'):
            return 'NUMERIC'

    return 'TEXT'
