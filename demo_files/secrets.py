"""
INTENTIONALLY VULNERABLE SECURITY VALIDATION FIXTURES.

All credentials below are synthetic and non-production.
Do not replace them with real credentials.
"""

import http.client
import os
import pickle
import tempfile

import jwt
import yaml
from jinja2 import Environment
from lxml import etree


# SECRET-01: Synthetic Google API key
GOOGLE_API_KEY = "AIzaAbCdEfGhIjKlMnOpQrStUvWxYz012345678"

# SECRET-02: Synthetic Telegram bot token
TELEGRAM_BOT_TOKEN = "1234567890:AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqR"

# SECRET-03: Synthetic Mailgun API key
MAILGUN_API_KEY = "key-0123456789abcdef0123456789abcdef"

# SECRET-04: Password embedded in Redis URI
REDIS_URL = (
    "redis://default:N4xQ8mR2vT7pK5cW9yL3@redis.secureline.invalid:6379/0"
)

# SECRET-05: Hardcoded JWT signing secret
JWT_SIGNING_SECRET = "h7Qm2Vx9Lp4Tk8Nz5Wd3Rf6Yc1Ba0JsE"


# SAST-01: Path traversal through untrusted filename
def read_uploaded_file(filename: str) -> str:
    path = "/tmp/uploads/" + filename
    with open(path, "r", encoding="utf-8") as handle:
        return handle.read()


# SAST-02: Unsafe pickle deserialization
def load_pickled_payload(payload: bytes):
    return pickle.loads(payload)


# SAST-03: Unsafe YAML deserialization
def load_yaml_configuration(payload: str):
    return yaml.load(payload, Loader=yaml.Loader)


# SAST-04: Insecure temporary-file creation
def create_predictable_temp_file() -> str:
    return tempfile.mktemp(prefix="secureline_")


# SAST-05: World-writable file permissions
def make_world_writable(path: str) -> None:
    os.chmod(path, 0o777)


# SAST-06: XML external entity processing enabled
def parse_untrusted_xml(payload: bytes):
    parser = etree.XMLParser(resolve_entities=True, load_dtd=True)
    return etree.fromstring(payload, parser)


# SAST-07: Jinja auto-escaping explicitly disabled
def create_template_environment():
    return Environment(autoescape=False)


# SAST-08: Cleartext HTTP connection
def call_internal_service():
    connection = http.client.HTTPConnection("internal.secureline.invalid", 80)
    connection.request("GET", "/health")
    return connection.getresponse()


# SAST-09: JWT signature verification disabled
def decode_without_signature_verification(token: str):
    return jwt.decode(token, options={"verify_signature": False})
