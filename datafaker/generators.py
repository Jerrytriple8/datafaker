"""Core data generators."""
import random
import string
import uuid
from datetime import date, timedelta

# Data pools
FIRST_NAMES = [
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace",
    "Henry", "Iris", "Jack", "Karen", "Leo", "Mia", "Noah",
    "Olivia", "Peter", "Quinn", "Rose", "Sam", "Tina",
    "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zane",
    "Aiko", "Boris", "Carmen", "Diego", "Elena", "Faisal",
    "Giulia", "Hiroshi", "Ines", "Javier", "Keiko", "Lars",
    "Maya", "Nikolai", "Olga", "Priya", "Rashid", "Sofia",
    "Tariq", "Ursula", "Viktor", "Wen", "Xiomara", "Yuki",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez",
    "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
    "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson",
    "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis",
    "Robinson", "Walker", "Young", "Allen", "King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green",
    "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell",
    "Mitchell", "Carter", "Roberts",
]

DOMAINS = [
    "gmail.com", "yahoo.com", "outlook.com", "hotmail.com",
    "protonmail.com", "icloud.com", "fastmail.com", "zoho.com",
]

STREETS = [
    "Main St", "Oak Ave", "Elm St", "Pine Rd", "Maple Dr",
    "Cedar Ln", "Birch Blvd", "Walnut St", "Chestnut Ave",
    "Spruce Rd", "Park Ave", "First St", "Second St", "Third Ave",
    "Lake Dr", "Hill Rd", "Valley Blvd", "River St", "Forest Ln",
    "Sunset Blvd", "Broadway", "Highland Ave", "Church St",
    "Washington St", "Lincoln Ave", "Jefferson Rd", "Madison Dr",
]

CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "Austin",
    "Seattle", "Denver", "Boston", "Portland", "Miami",
    "Atlanta", "Nashville", "Las Vegas", "San Francisco", "Detroit",
    "Minneapolis", "Charlotte", "Raleigh", "Salt Lake City",
    "Orlando", "Pittsburgh", "Cincinnati", "Cleveland", "Tampa",
]

STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL",
    "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
    "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE",
    "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK",
    "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT",
    "VA", "WA", "WV", "WI", "WY",
]

PHONE_FORMATS = [
    "({area}) {prefix}-{line}",
    "{area}-{prefix}-{line}",
    "+1.{area}.{prefix}.{line}",
]


def first_name():
    return random.choice(FIRST_NAMES)

def last_name():
    return random.choice(LAST_NAMES)

def full_name():
    return f"{first_name()} {last_name()}"

def email(domain=None):
    first = first_name().lower()
    last = last_name().lower()
    dom = domain or random.choice(DOMAINS)
    sep = random.choice([".", "_", ""])
    num = random.randint(0, 99) if random.random() > 0.5 else ""
    return f"{first}{sep}{last}{num}@{dom}"

def phone():
    area = random.randint(200, 999)
    prefix = random.randint(100, 999)
    line = random.randint(1000, 9999)
    fmt = random.choice(PHONE_FORMATS)
    return fmt.format(area=area, prefix=prefix, line=line)

def street_address():
    num = random.randint(1, 9999)
    return f"{num} {random.choice(STREETS)}"

def city():
    return random.choice(CITIES)

def state():
    return random.choice(STATES)

def zipcode():
    return f"{random.randint(10000, 99999)}"

def address():
    return f"{street_address()}, {city()}, {state()} {zipcode()}"

def ipv4():
    octets = [random.randint(1, 254) for _ in range(4)]
    return ".".join(str(o) for o in octets)

def ipv6():
    segments = [format(random.randint(0, 65535), "04x") for _ in range(8)]
    return ":".join(segments)

def uuid_v4():
    return str(uuid.uuid4())

def uuid_v1():
    return str(uuid.uuid1())

def date_val(start=None, end=None):
    if start:
        start_d = date.fromisoformat(start)
    else:
        start_d = date(2000, 1, 1)
    if end:
        end_d = date.fromisoformat(end)
    else:
        end_d = date.today()
    delta = (end_d - start_d).days
    if delta <= 0:
        return str(start_d)
    random_days = random.randint(0, delta)
    return str(start_d + timedelta(days=random_days))

def integer(low=0, high=10000):
    return random.randint(low, high)

def float_val(low=0.0, high=10000.0):
    return round(random.uniform(low, high), 2)

def boolean():
    return random.choice([True, False])

def word():
    words = [
        "alpha", "beta", "gamma", "delta", "epsilon", "zeta",
        "eta", "theta", "iota", "kappa", "lambda", "mu",
        "nu", "xi", "omicron", "pi", "rho", "sigma",
        "tau", "upsilon", "phi", "chi", "psi", "omega",
    ]
    return random.choice(words)

def sentence():
    n = random.randint(5, 12)
    words_list = [word() for _ in range(n)]
    words_list[0] = words_list[0].capitalize()
    return " ".join(words_list) + "."

def record(fields=None):
    if fields is None:
        fields = ["name", "email", "phone", "address"]
    result = {}
    for f in fields:
        f = f.strip().lower()
        if f == "name":
            result["name"] = full_name()
        elif f == "first_name":
            result["first_name"] = first_name()
        elif f == "last_name":
            result["last_name"] = last_name()
        elif f == "email":
            result["email"] = email()
        elif f == "phone":
            result["phone"] = phone()
        elif f == "address":
            result["address"] = address()
        elif f == "city":
            result["city"] = city()
        elif f == "state":
            result["state"] = state()
        elif f == "zipcode":
            result["zipcode"] = zipcode()
        elif f == "ipv4":
            result["ipv4"] = ipv4()
        elif f == "ipv6":
            result["ipv6"] = ipv6()
        elif f == "uuid":
            result["uuid"] = uuid_v4()
        elif f == "date":
            result["date"] = date_val()
        elif f == "integer":
            result["integer"] = integer()
        elif f == "float":
            result["float"] = float_val()
        elif f == "boolean":
            result["boolean"] = boolean()
        elif f == "word":
            result["word"] = word()
        elif f == "sentence":
            result["sentence"] = sentence()
        else:
            result[f] = f"unknown_field: {f}"
    return result
