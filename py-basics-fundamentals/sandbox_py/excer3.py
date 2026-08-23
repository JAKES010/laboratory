def deduplicate_keep_order(items: list) -> list :
    items = dict.fromkeys(items)
    return list(items)

input_data = [4, 5, 2, 4, 1, 5, 3]
output = deduplicate_keep_order(input_data)
print(output)  # Must be: [4, 5, 2, 1, 3]

# --- Tests ---
assert deduplicate_keep_order([4, 5, 2, 4, 1, 5, 3]) == [4, 5, 2, 1, 3]
assert deduplicate_keep_order(["a", "b", "a", "c"]) == ["a", "b", "c"]
assert deduplicate_keep_order([]) == []

print("All deduplication tests passed!")

def deduplicate_keep_order_explicit(items: list) -> list:
    seen = set()
    result = []
    for item in items:
        if item not in seen:  # O(1) hash check
            seen.add(item)
            result.append(item)
    return result

input_data = [4, 5, 2, 4, 1, 5, 3]
output = deduplicate_keep_order_explicit(input_data)
print(output)  # Must be: [4, 5, 2, 1, 3]