"""CLI interface for datafaker."""
import argparse
import json
import sys
import csv
import io
from datafaker import generators


def cmd_name(args):
    results = []
    for _ in range(args.count):
        if args.format == "first":
            results.append(generators.first_name())
        elif args.format == "last":
            results.append(generators.last_name())
        else:
            results.append(generators.full_name())
    return results


def cmd_email(args):
    return [generators.email(domain=args.domain) for _ in range(args.count)]


def cmd_phone(args):
    return [generators.phone() for _ in range(args.count)]


def cmd_address(args):
    return [generators.address() for _ in range(args.count)]


def cmd_uuid(args):
    fn = generators.uuid_v1 if args.version == 1 else generators.uuid_v4
    return [fn() for _ in range(args.count)]


def cmd_ipv4(args):
    return [generators.ipv4() for _ in range(args.count)]


def cmd_ipv6(args):
    return [generators.ipv6() for _ in range(args.count)]


def cmd_date(args):
    return [generators.date_val(start=args.start, end=args.end) for _ in range(args.count)]


def cmd_integer(args):
    return [generators.integer(low=args.low, high=args.high) for _ in range(args.count)]


def cmd_record(args):
    fields = [f.strip() for f in args.fields.split(",")]
    return [generators.record(fields) for _ in range(args.count)]


def format_output(results, output_format):
    if output_format == "json":
        print(json.dumps(results, indent=2))
    elif output_format == "csv":
        if results and isinstance(results[0], dict):
            keys = results[0].keys()
            buf = io.StringIO()
            writer = csv.DictWriter(buf, fieldnames=keys)
            writer.writeheader()
            writer.writerows(results)
            print(buf.getvalue(), end="")
        else:
            for r in results:
                print(r)
    elif output_format == "table":
        if results and isinstance(results[0], dict):
            keys = list(results[0].keys())
            # Header
            header = " | ".join(k.ljust(15)[:15] for k in keys)
            print(header)
            print("-" * len(header))
            for row in results:
                print(" | ".join(str(row[k]).ljust(15)[:15] for k in keys))
        else:
            for r in results:
                print(r)
    else:
        for r in results:
            if isinstance(r, dict):
                print(json.dumps(r))
            else:
                print(r)


def _add_common_flags(parser):
    """Add --count and --output flags to a subparser."""
    parser.add_argument("--count", "-n", type=int, default=1,
                        help="Number of items to generate (default: 1)")
    parser.add_argument("--output", "-o", choices=["text", "json", "csv", "table"],
                        default="text", help="Output format (default: text)")


def main():
    parser = argparse.ArgumentParser(
        prog="datafaker",
        description="Generate fake data for testing and prototyping.",
    )

    sub = parser.add_subparsers(dest="command", help="Data type to generate")

    # name
    p_name = sub.add_parser("name", help="Generate names")
    p_name.add_argument("--format", "-f", choices=["full", "first", "last"],
                        default="full", help="Name format")
    _add_common_flags(p_name)

    # email
    p_email = sub.add_parser("email", help="Generate emails")
    p_email.add_argument("--domain", "-d", default=None,
                         help="Email domain (random if not set)")
    _add_common_flags(p_email)

    # phone
    p_phone = sub.add_parser("phone", help="Generate phone numbers")
    _add_common_flags(p_phone)

    # address
    p_addr = sub.add_parser("address", help="Generate addresses")
    _add_common_flags(p_addr)

    # uuid
    p_uuid = sub.add_parser("uuid", help="Generate UUIDs")
    p_uuid.add_argument("--version", "-v", type=int, choices=[1, 4],
                        default=4, help="UUID version (default: 4)")
    _add_common_flags(p_uuid)

    # ipv4
    p4 = sub.add_parser("ipv4", help="Generate IPv4 addresses")
    _add_common_flags(p4)

    # ipv6
    p6 = sub.add_parser("ipv6", help="Generate IPv6 addresses")
    _add_common_flags(p6)

    # date
    p_date = sub.add_parser("date", help="Generate dates")
    p_date.add_argument("--start", "-s", default=None,
                        help="Start date (YYYY-MM-DD, default: 2000-01-01)")
    p_date.add_argument("--end", "-e", default=None,
                        help="End date (YYYY-MM-DD, default: today)")
    _add_common_flags(p_date)

    # integer
    p_int = sub.add_parser("integer", help="Generate integers")
    p_int.add_argument("--low", type=int, default=0, help="Minimum (default: 0)")
    p_int.add_argument("--high", type=int, default=10000, help="Maximum (default: 10000)")
    _add_common_flags(p_int)

    # record
    p_rec = sub.add_parser("record", help="Generate mixed records (JSON)")
    p_rec.add_argument("--fields", "-f", default="name,email,phone,address",
                       help="Comma-separated field names (default: name,email,phone,address)")
    _add_common_flags(p_rec)

    args = parser.parse_args()

    # Set defaults for count/output when called without subcommand
    if not hasattr(args, "count") or args.count is None:
        args.count = 1
    if not hasattr(args, "output") or args.output is None:
        args.output = "text"

    if not args.command:
        parser.print_help()
        sys.exit(1)

    dispatch = {
        "name": cmd_name,
        "email": cmd_email,
        "phone": cmd_phone,
        "address": cmd_address,
        "uuid": cmd_uuid,
        "ipv4": cmd_ipv4,
        "ipv6": cmd_ipv6,
        "date": cmd_date,
        "integer": cmd_integer,
        "record": cmd_record,
    }

    results = dispatch[args.command](args)
    format_output(results, args.output)


if __name__ == "__main__":
    main()
