from wog.weight_classes import classify

def test_class_bounds():
    assert classify(59.0) == "59 kg"
    assert classify(59.01) == "66 kg"
    assert classify(74.0) == "74 kg"
    assert classify(74.01) == "83 kg"
    assert classify(120.0) == "120 kg"
    assert classify(120.5) == "120+ kg"

def test_unclassified():
    assert classify(None) is None
