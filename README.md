# One Image, One Day of World News

This entry is a program that writes a single image summing up
Monday 23 November 2026 in world news.

The image covers 35 stories across 6 continents and 17 fields,
drawn into one 1024x1024 picture — a whole day of world news at a glance.

## How it works

- `entry.png.b64` holds the image as base64 text.
- `main.py` decodes that file and writes the PNG to `/output/entry.png`.

Run it with:

```sh
python3 main.py
```

## License

MIT. Built for the make.fun bounty `news-image-20261123`.
