"""Cenários adicionais que complementam os testes fornecidos, sem alterá-los."""
from helpers import run_cli


def test_more_than_200_reservations_are_processed(tmp_path):
    rows = [{"reservation_id": f"R-{i:03d}", "amount": "1.00"} for i in range(205)]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_reservations"] == 205
    assert report["summary"]["confirmed_reservations"] == 205
    assert report["summary"]["total_amount_brl"] == "205.00"
    assert report["summary"]["total_room_nights"] == 205


def test_tied_hotels_rank_by_id_ascending(tmp_path):
    rows = [
        {"reservation_id": "R-1", "hotel_id": "H09", "hotel_name": "Hotel Z", "amount": "100.00"},
        {"reservation_id": "R-2", "hotel_id": "H01", "hotel_name": "Hotel A", "amount": "100.00"},
        {"reservation_id": "R-3", "hotel_id": "H05", "hotel_name": "Hotel E", "amount": "200.00"},
    ]
    report = run_cli(tmp_path, rows, top=3)
    assert [h["hotel_id"] for h in report["top_hotels"]] == ["H05", "H01", "H09"]


def test_empty_confirmed_reservations_have_zero_amount_and_nights(tmp_path):
    rows = [
        {"reservation_id": "R-1", "status": "CANCELLED", "amount": "100.00"},
        {"reservation_id": "R-2", "status": "NO_SHOW", "amount": "100.00"},
    ]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_reservations"] == 2
    assert report["summary"]["total_room_nights"] == 0
    assert report["summary"]["total_amount_brl"] == "0.00"
    assert report["summary"]["average_nightly_rate_brl"] == "0.00"
    assert report["by_month"] == []
    assert report["top_hotels"] == []


def test_round_money_only_after_sum_half_up(tmp_path):
    rows = [
        {"reservation_id": "R-1", "amount": "0.005"},
        {"reservation_id": "R-2", "amount": "0.006"},
    ]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_amount_brl"] == "0.01"
    assert report["summary"]["average_nightly_rate_brl"] == "0.01"


def test_year_boundary_and_month_of_checkin(tmp_path):
    rows = [{
        "reservation_id": "R-1",
        "checkin_date": "2025-12-30",
        "checkout_date": "2026-01-02",
        "rooms": "2",
        "amount": "123.00",
    }]
    report = run_cli(tmp_path, rows)
    assert report["summary"]["total_room_nights"] == 6
    assert [m["month"] for m in report["by_month"]] == ["2025-12"]
    assert report["by_month"][0]["room_nights"] == 6
