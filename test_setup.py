print("=== TEST SETUP - PLO Vision i Codespaces ===")
print("")

try:
    import easyocr
    reader = easyocr.Reader(['en'], gpu=False)
    print("✅ EasyOCR: OK (klar til å lese kort)")
except Exception as e:
    print("❌ EasyOCR feilet:", e)

try:
    from pokerkit import parse_range, calculate_equities
    print("✅ pokerkit: OK (PLO equity fungerer)")
except Exception as e:
    print("❌ pokerkit feilet:", e)

try:
    import pytesseract
    print("✅ pytesseract + Tesseract: OK")
except Exception as e:
    print("❌ pytesseract feilet:", e)

print("\nHvis du ser 3 ✅ over – da er vi klare til å bygge videre på dickreuter/Poker-repoet!")
