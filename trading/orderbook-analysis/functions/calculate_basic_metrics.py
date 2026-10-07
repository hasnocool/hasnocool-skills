# filename: trading/orderbook-analysis/functions/calculate_basic_metrics.py
import json
import sys


def main() -> int:
    payload = json.load(sys.stdin)
    bids = payload.get("bids", [])
    asks = payload.get("asks", [])

    if not bids or not asks:
        print(json.dumps({"ok": False, "error": "bids and asks are required"}))
        return 2

    best_bid = float(bids[0][0])
    best_ask = float(asks[0][0])
    bid_size = sum(float(price) * float(size) for price, size in bids)
    ask_size = sum(float(price) * float(size) for price, size in asks)
    total = bid_size + ask_size

    print(json.dumps({
        "ok": True,
        "best_bid": best_bid,
        "best_ask": best_ask,
        "spread": best_ask - best_bid,
        "spread_bps": ((best_ask - best_bid) / best_bid) * 10000,
        "notional_bid_depth": bid_size,
        "notional_ask_depth": ask_size,
        "depth_imbalance": ((bid_size - ask_size) / total) if total else 0.0,
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
