import random

# Load lines from metadata
with open("datasets/tamil_speaker/metadata.csv", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Shuffle and split
random.shuffle(lines)
split_index = int(0.9 * len(lines))
train_lines = lines[:split_index]
val_lines = lines[split_index:]

# Write outputs
with open("datasets/tamil_speaker/metadata.csv", "w", encoding="utf-8") as f:
    f.writelines(train_lines)

with open("datasets/tamil_speaker/metadata_val.csv", "w", encoding="utf-8") as f:
    f.writelines(val_lines)

print(f"Train: {len(train_lines)} lines, Validation: {len(val_lines)} lines.")
