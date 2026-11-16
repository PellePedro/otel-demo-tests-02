import json  # noqa: F401


def test_h01_cur_ils_0001(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ILS" in codes


def test_h01_cur_inr_0002(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "INR" in codes


def test_h01_cur_isk_0003(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "ISK" in codes


def test_h01_cur_jpy_0004(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "JPY" in codes


def test_h01_cur_krw_0005(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "KRW" in codes


def test_h01_cur_mxn_0006(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MXN" in codes


def test_h01_cur_myr_0007(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "MYR" in codes


def test_h01_cur_nok_0008(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NOK" in codes


def test_h01_cur_nzd_0009(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "NZD" in codes


def test_h01_cur_php_0010(api):
    resp = api.get("/api/currency")
    assert resp.status_code == 200
    codes = resp.json()
    assert len(codes) == 33
    assert "USD" in codes
    assert "PHP" in codes
