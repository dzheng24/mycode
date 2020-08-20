import astronaut_tracker
import pytest 

def test_get_results():
    with pytest.raises(RuntimeError) as ziggy:
        astronaut_tracker.get_results()

    assert "Network access not allowed" in str(ziggy.value)
