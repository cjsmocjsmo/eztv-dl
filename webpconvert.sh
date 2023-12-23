for f in /home/charliepi/Downloads/newposters3/*.jpg; do
cwebp -q 95 -resize 300 0 "$f" -o "${f%.jpg}.webp"
done
