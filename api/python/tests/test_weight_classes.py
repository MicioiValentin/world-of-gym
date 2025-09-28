from wog.weight_classes import classify

def test_class_bounds():
    assert classify(74.0) == "74 kg"
    assert classify(74.01) == "83 kg"

def test_unclassified():
    assert classify(None) is None
