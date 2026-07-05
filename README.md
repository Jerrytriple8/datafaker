# datafaker

CLI tool to generate fake data — names, emails, addresses, UUIDs, IPs, dates. Useful for testing, prototyping, and seeding databases.

## Install

```bash
pip install datafaker
```

Or run directly:

```bash
python -m datafaker name --count 5
```

## Usage

Generate names:

```bash
datafaker name --count 10
datafaker name --count 3 --format first
```

Generate emails:

```bash
datafaker email --count 5
datafaker email --count 3 --domain example.com
```

Generate addresses:

```bash
datafaker address --count 5
```

Generate UUIDs:

```bash
datafaker uuid --count 10
datafaker uuid --count 5 --version 4
```

Generate IP addresses:

```bash
datafaker ipv4 --count 10
datafaker ipv6 --count 5
```

Generate dates:

```bash
datafaker date --count 10
datafaker date --count 5 --start 2020-01-01 --end 2025-12-31
```

Generate phone numbers:

```bash
datafaker phone --count 10
```

Generate mixed records (JSON):

```bash
datafaker record --count 5 --fields name,email,phone,ipv4
```

Output formats:

```bash
datafaker name --count 5 --output json
datafaker name --count 5 --output csv
datafaker name --count 5 --output table
```

## Output

Default is plain text, one item per line. Use `--output json` for structured output:

```json
[
  {"first": "Alice", "last": "Smith"},
  {"first": "Bob", "last": "Jones"}
]
```

## License

MIT
