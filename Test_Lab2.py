import Lab2 as temp
def test_calc_min_max_temperature():
    input_arr = [23.0, 14.14, 51.0, 69.41, 51.0, 216.0, 136.0, 63.0, 71.0, 13.0, 75.0, 23.32]
    test_arr = (13.0, 216.0)
    result = temp.calc_min_max_temperature(input_arr)
    assert (result == test_arr)

def test_calc_average_temperature():
    input_arr = [23.0, 14.14, 51.0, 69.41, 51.0, 216.0, 136.0, 63.0, 71.0, 13.0, 75.0, 23.32]
    test_arr = 67.15583333333333
    result = temp.calc_average_temperature(input_arr)
    assert (result == test_arr)

def test_calc_median_temperature():
    input_arr = [23.0, 14.14, 51.0, 69.41, 51.0, 216.0, 136.0, 63.0, 71.0, 13.0, 75.0, 23.32]
    test_arr = 57.0
    result = temp.calc_median_temperature(input_arr)
    assert (result == test_arr)