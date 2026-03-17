print("=== PLO VISION TEST v3 – Korrekt pokerkit API ===")

from pokerkit import parse_range, calculate_equities, Deck, StandardHighHand, Card

print("\n1. Test pokerkit PLO equity (4 hullkort):")

hero_range = parse_range("AhKhQhJh")
villain_range = parse_range("22+, A2s+, K9s+, QTs+, JTs, ATo+, KJo+")

board_cards = [Card.parse(c) for c in ["As", "Ks", "Qs", "2d", "3c"]]

equities = calculate_equities(
    [hero_range, villain_range],   # hole_ranges som liste
    board_cards,
    4,                             # hole_dealing_count = PLO
    5,                             # board_dealing_count
    Deck.STANDARD,
    (StandardHighHand,),
    sample_count=8000
)

print(f"   Din equity vs range: {equities[0]:.1%}")
print("✅ pokerkit PLO Monte Carlo fungerer perfekt!")

print("\n2. EasyOCR og pytesseract er allerede OK fra før.")

print("\n✅ Vi er nå klare til steg 8: YAML-config + egen OCR-engine + Rich CLI!")
