mkdir -p datasets/wavs_converted

for file in datasets/wavs/*.wav; do
    sox "$file" -r 22050 -c 1 "datasets/wavs_converted/$(basename "$file")"
done

mv datasets/wavs datasets/wavs_backup
mv datasets/wavs_converted datasets/wavs
