import os
from master_file_parser import MasterFileParser
from master_file_asg_builder import MasterFileASGBuilder

class MetadataRegistry:
    """
    Manages and caches Master File ASG nodes.
    Supports searching for .mas files in multiple directories.
    """
    def __init__(self, search_paths=None):
        self.search_paths = search_paths or []
        self.cache = {}
        self.parser = MasterFileParser()
        self.builder = MasterFileASGBuilder()

    def add_search_path(self, path):
        """Adds a directory to the search paths for Master Files."""
        if path not in self.search_paths:
            self.search_paths.append(path)

    def get_master_file(self, name):
        """
        Retrieves a MasterFile ASG node by name.
        Searches in search_paths and caches the result.
        """
        name_upper = name.upper()
        if name_upper in self.cache:
            return self.cache[name_upper]

        file_path = self._find_mas_file(name)
        if not file_path:
            return None

        try:
            with open(file_path, 'r') as f:
                content = f.read()

            tree = self.parser.parse(content)
            # Reset builder state if needed, although current implementation seems safe
            # but usually it's better to use a fresh one or clear it if it has state.
            # MasterFileASGBuilder has self.master_file and self.current_segment
            self.builder.master_file = None
            self.builder.current_segment = None

            master_file = self.builder.visit(tree)
            if master_file:
                self.cache[name_upper] = master_file
            return master_file
        except Exception as e:
            # In a real system we might want to log this or raise a custom exception
            print(f"Error loading Master File {name} from {file_path}: {e}")
            return None

    def _find_mas_file(self, name):
        """Searches for <name>.mas in the configured search paths."""
        filenames = [f"{name}.mas", f"{name.lower()}.mas", f"{name.upper()}.mas"]
        for path in self.search_paths:
            for filename in filenames:
                full_path = os.path.join(path, filename)
                if os.path.isfile(full_path):
                    return full_path
        return None

    def clear_cache(self):
        """Clears the internal cache of Master Files."""
        self.cache.clear()
