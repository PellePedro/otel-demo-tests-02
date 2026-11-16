import json  # noqa: F401


def test_h02_ils_0001(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0002(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0003(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0004(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0005(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0006(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0007(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0008(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0009(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0010(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0011(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0012(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0013(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0014(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0015(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0016(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0017(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0018(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0019(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0020(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0021(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0022(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0023(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0024(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0025(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0026(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0027(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0028(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0029(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0030(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0031(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0032(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0033(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0034(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0035(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0036(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0037(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0038(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0039(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0040(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0041(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0042(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0043(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0044(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0045(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0046(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0047(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0048(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0049(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0050(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0051(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0052(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0053(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0054(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0055(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0056(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0057(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0058(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0059(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0060(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0061(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0062(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0063(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0064(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0065(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0066(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0067(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0068(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0069(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0070(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0071(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0072(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0073(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0074(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0075(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0076(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0077(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0078(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0079(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0080(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0081(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0082(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0083(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0084(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0085(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0086(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0087(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0088(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0089(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0090(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0091(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0092(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0093(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0094(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0095(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0096(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0097(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0098(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0099(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0100(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0101(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0102(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0103(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0104(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0105(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0106(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0107(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0108(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0109(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0110(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0111(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0112(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0113(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0114(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0115(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0116(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0117(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0118(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0119(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0120(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0121(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0122(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0123(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0124(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0125(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0126(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0127(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0128(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0129(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0130(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0131(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0132(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0133(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0134(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0135(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0136(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0137(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0138(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0139(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0140(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0141(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0142(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0143(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0144(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0145(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0146(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0147(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0148(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0149(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0150(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0151(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0152(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0153(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0154(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0155(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0156(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0157(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0158(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0159(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0160(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0161(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0162(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0163(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0164(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0165(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0166(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0167(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0168(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0169(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0170(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0171(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0172(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0173(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0174(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0175(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0176(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0177(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0178(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0179(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0180(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0181(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0182(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0183(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0184(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0185(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0186(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0187(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0188(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0189(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0190(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0191(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0192(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0193(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0194(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0195(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0196(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0197(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0198(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0199(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0200(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0201(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0202(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0203(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0204(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0205(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0206(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0207(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0208(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0209(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0210(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0211(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0212(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0213(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0214(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0215(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0216(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0217(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0218(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0219(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0220(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0221(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0222(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0223(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0224(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0225(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0226(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0227(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0228(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0229(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0230(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0231(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0232(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0233(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0234(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0235(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0236(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0237(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0238(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0239(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0240(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0241(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0242(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0243(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0244(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0245(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0246(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0247(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0248(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0249(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0250(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0251(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0252(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0253(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0254(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0255(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0256(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0257(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0258(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0259(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0260(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0261(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0262(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0263(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0264(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0265(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0266(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0267(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0268(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0269(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0270(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0271(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0272(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0273(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0274(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0275(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0276(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0277(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0278(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0279(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0280(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0281(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0282(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0283(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0284(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0285(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0286(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0287(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0288(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0289(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0290(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0291(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0292(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0293(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0294(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0295(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0296(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0297(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0298(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0299(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0300(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0301(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0302(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0303(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0304(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0305(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0306(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0307(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0308(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0309(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0310(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0311(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0312(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0313(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0314(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0315(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0316(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0317(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0318(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0319(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0320(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0321(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0322(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0323(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0324(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0325(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0326(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0327(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"


def test_h02_hrk_0328(api):
    resp = api.get("/api/products", params={"currencyCode": "HRK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HRK"


def test_h02_huf_0329(api):
    resp = api.get("/api/products", params={"currencyCode": "HUF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HUF"


def test_h02_idr_0330(api):
    resp = api.get("/api/products", params={"currencyCode": "IDR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "IDR"


def test_h02_ils_0331(api):
    resp = api.get("/api/products", params={"currencyCode": "ILS"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ILS"


def test_h02_inr_0332(api):
    resp = api.get("/api/products", params={"currencyCode": "INR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "INR"


def test_h02_isk_0333(api):
    resp = api.get("/api/products", params={"currencyCode": "ISK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ISK"


def test_h02_jpy_0334(api):
    resp = api.get("/api/products", params={"currencyCode": "JPY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "JPY"


def test_h02_krw_0335(api):
    resp = api.get("/api/products", params={"currencyCode": "KRW"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "KRW"


def test_h02_mxn_0336(api):
    resp = api.get("/api/products", params={"currencyCode": "MXN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MXN"


def test_h02_myr_0337(api):
    resp = api.get("/api/products", params={"currencyCode": "MYR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "MYR"


def test_h02_nok_0338(api):
    resp = api.get("/api/products", params={"currencyCode": "NOK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NOK"


def test_h02_nzd_0339(api):
    resp = api.get("/api/products", params={"currencyCode": "NZD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "NZD"


def test_h02_php_0340(api):
    resp = api.get("/api/products", params={"currencyCode": "PHP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PHP"


def test_h02_pln_0341(api):
    resp = api.get("/api/products", params={"currencyCode": "PLN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "PLN"


def test_h02_ron_0342(api):
    resp = api.get("/api/products", params={"currencyCode": "RON"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RON"


def test_h02_rub_0343(api):
    resp = api.get("/api/products", params={"currencyCode": "RUB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "RUB"


def test_h02_sek_0344(api):
    resp = api.get("/api/products", params={"currencyCode": "SEK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SEK"


def test_h02_sgd_0345(api):
    resp = api.get("/api/products", params={"currencyCode": "SGD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "SGD"


def test_h02_thb_0346(api):
    resp = api.get("/api/products", params={"currencyCode": "THB"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "THB"


def test_h02_try_0347(api):
    resp = api.get("/api/products", params={"currencyCode": "TRY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "TRY"


def test_h02_usd_0348(api):
    resp = api.get("/api/products", params={"currencyCode": "USD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "USD"


def test_h02_zar_0349(api):
    resp = api.get("/api/products", params={"currencyCode": "ZAR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "ZAR"


def test_h02_aud_0350(api):
    resp = api.get("/api/products", params={"currencyCode": "AUD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "AUD"


def test_h02_bgn_0351(api):
    resp = api.get("/api/products", params={"currencyCode": "BGN"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BGN"


def test_h02_brl_0352(api):
    resp = api.get("/api/products", params={"currencyCode": "BRL"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "BRL"


def test_h02_cad_0353(api):
    resp = api.get("/api/products", params={"currencyCode": "CAD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CAD"


def test_h02_chf_0354(api):
    resp = api.get("/api/products", params={"currencyCode": "CHF"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CHF"


def test_h02_cny_0355(api):
    resp = api.get("/api/products", params={"currencyCode": "CNY"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CNY"


def test_h02_czk_0356(api):
    resp = api.get("/api/products", params={"currencyCode": "CZK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "CZK"


def test_h02_dkk_0357(api):
    resp = api.get("/api/products", params={"currencyCode": "DKK"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "DKK"


def test_h02_eur_0358(api):
    resp = api.get("/api/products", params={"currencyCode": "EUR"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "EUR"


def test_h02_gbp_0359(api):
    resp = api.get("/api/products", params={"currencyCode": "GBP"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "GBP"


def test_h02_hkd_0360(api):
    resp = api.get("/api/products", params={"currencyCode": "HKD"})
    assert resp.status_code == 200
    products = resp.json()
    assert len(products) == 10
    for product in products:
        assert product["priceUsd"]["currencyCode"] == "HKD"
