import Lab2.bmi as bmi

print("Test_bmi")

def test_bmi_normal_weight():
    # BMI within the normal weight range
    result = bmi.calculate_bmi(height=1.75, weight=70)
    assert result == 0

def test_bmi_over_weight():
    # BMI within the over weight range
    result = bmi.calculate_bmi(height=1.75, weight=90)
    assert result == 1

def test_bmi_under_weight():
    # BMI within the under weight range
    result = bmi.calculate_bmi(height=1.75, weight=50)
    assert result == -1