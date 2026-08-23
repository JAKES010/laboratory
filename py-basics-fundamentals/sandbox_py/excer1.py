def process_slice(data: list) -> list:
    if len(data) < 2:
        return []
    return data[::-2]

# --- Tests ---
assert process_slice([4, 5, 6, 7, 8, 9]) == [9, 7, 5]
assert process_slice([10, 20]) == [20]
assert process_slice([1]) == []
assert process_slice([]) == []

print("All tests passed successfully.")