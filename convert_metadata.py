# convert_metadata.py

input_file = "datasets/tamil_speaker/metadata.txt"
output_file = "datasets/tamil_speaker/metadata.csv"
speaker_name = "tamil_female"

with open(input_file, "r", encoding="utf-8") as fin, open(output_file, "w", encoding="utf-8") as fout:
    for line in fin:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            audio_file, text = parts
            fout.write(f"{audio_file}|{speaker_name}|{text}\n")
        else:
            print(f"Skipping malformed line: {line}")
