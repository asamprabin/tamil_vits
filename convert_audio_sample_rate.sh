mkdir -p datasets/tamil_speaker/wavs_converted

for file in datasets/tamil_speaker/wavs/*.wav; do
    sox "$file" -r 22050 -c 1 "datasets/tamil_speaker/wavs_converted/$(basename "$file")"
done

mv datasets/tamil_speaker/wavs datasets/tamil_speaker/wavs_backup
mv datasets/tamil_speaker/wavs_converted datasets/tamil_speaker/wavs
