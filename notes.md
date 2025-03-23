find . -type f -name '\*.wav' -exec bash -c 'echo "$0"' '{}' \;

ffmpeg -i "./Garland Briggs/Major Briggs Dream.wav" -c:a libvorbis -q:a 4 "./Garland Briggs/Major Briggs Dream.ogg"

```
find ./src/sounds/edited -type f -name '*.wav' -exec bash -c 'ffmpeg -i "$0" -codec:a aac "$0.aac"' '{}' \;
```
