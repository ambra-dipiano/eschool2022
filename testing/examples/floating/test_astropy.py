import astropy.units as u

def test_time():
    v = 10 * u.m / u.s
    d = 1 * u.km
    assert u.isclose(d / v, 100 * u.s)

def test_time2():
    # does not check that you get the exact same unit but that they are convertible
    v = 1 * u.km / u.hour
    d = 1 * u.km
    assert u.isclose(d / v, 3600 * u.s)

def test_many():
    v = 10 * u.m / u.s
    d = [0, 1, 5] * u.km
    assert u.allclose(d / v, [0, 100, 500] * u.s)
