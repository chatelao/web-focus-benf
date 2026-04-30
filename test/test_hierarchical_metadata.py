import pytest
from metadata_registry import MetadataRegistry
from asg import MasterFile, Dimension, Hierarchy

def test_hierarchical_metadata_parsing():
    registry = MetadataRegistry(search_paths=["test/documentation_examples/project3_hierarchical_cube"])
    master_file = registry.get_master_file("NEWGL")

    assert master_file is not None
    assert isinstance(master_file, MasterFile)
    assert master_file.name == "NEWGL"

    # Check dimensions
    assert len(master_file.dimensions) == 1
    dim = master_file.dimensions[0]
    assert isinstance(dim, Dimension)
    assert dim.name == "Accnt"
    assert dim.CAPTION == "Accnt"

    # Check hierarchies
    assert len(master_file.hierarchies) == 1
    hry = master_file.hierarchies[0]
    assert isinstance(hry, Hierarchy)
    assert hry.name == "Accnt"
    assert hry.CAPTION == "Accnt"  # Note: parser strips quotes
    assert hry.HRY_DIMENSION == "Accnt"
    assert hry.HRY_STRUCTURE == "RECURSIVE"

    # Check fields for hierarchical attributes
    segment = master_file.segments[0]

    # GL_ACCOUNT
    gl_acc = next(f for f in segment.fields if f.name == "GL_ACCOUNT")
    assert gl_acc.WITHIN == "*Accnt"
    assert gl_acc.PROPERTY == "UID"
    assert gl_acc.TITLE == "Ledger,Account"

    # GL_ACCOUNT_PARENT
    gl_par = next(f for f in segment.fields if f.name == "GL_ACCOUNT_PARENT")
    assert gl_par.PROPERTY == "PARENT_OF"
    assert gl_par.REFERENCE == "GL_ACCOUNT"

    # GL_ACCOUNT_CAPTION
    gl_cap = next(f for f in segment.fields if f.name == "GL_ACCOUNT_CAPTION")
    assert gl_cap.PROPERTY == "CAPTION"
    assert gl_cap.REFERENCE == "GL_ACCOUNT"

if __name__ == "__main__":
    pytest.main([__file__])
