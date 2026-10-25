"""Synthetic arithmetic illustration, not an XUR parser or repair utility."""

def deficit_bytes(declared_entries, required_entries):
    if declared_entries < 0 or required_entries < 0:
        raise ValueError("Entry counts must be nonnegative")
    return max(0, required_entries - declared_entries) * 12


# Invented example: an array accounted as one entry really needs four.
declared = 8
required = declared - 1 + 4
assert deficit_bytes(declared, required) == 36
assert deficit_bytes(12, required) == 0
print(f"Synthetic declared={declared}, required={required}: "
      f"{deficit_bytes(declared, required)} missing arena bytes")
print("Real validation requires a target-schema DATA walk and header-offset repair.")
