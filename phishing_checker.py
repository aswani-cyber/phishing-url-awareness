
import re
from urllib.parse import urlparse


def inspect_url(raw_url):
    """Check visible URL text for selected warning signs."""
    url = raw_url.strip()
    findings = []

    if not url:
        return ["No URL entered."]

    candidate = url if "://" in url else "http://" + url

    # Handle malformed URLs
    try:
        parsed = urlparse(candidate)
        host = (parsed.hostname or "").lower()
    except ValueError:
        return ["Invalid URL format. Please enter a valid URL."]

    if not host:
        return ["Could not identify a hostname."]

    # Check for @ symbol
    if "@" in candidate:
        findings.append("Contains an @ symbol; inspect carefully.")

    # Check URL length
    if len(url) > 100:
        findings.append("Unusually long URL (over 100 characters).")

    # Check IP address
    if re.fullmatch(r"(?:\d{1,3}\.){3}\d{1,3}", host):
        findings.append(
            "Uses an IP address instead of a familiar domain."
        )

    # Check hostname labels
    labels = [part for part in host.split(".") if part]
    if len(labels) >= 5:
        findings.append(
            "Contains many hostname segments/subdomains."
        )

    # Check punycode
    if "xn--" in host:
        findings.append("Contains a punycode-style hostname.")

    # Check HTTP
    if parsed.scheme.lower() == "http":
        findings.append(
            "Uses HTTP. HTTPS alone does not prove trust."
        )

    # Warning summary
    if not findings:
        findings.append(
            "No listed warning signs found. This does NOT prove safety."
        )
    else:
        findings.append(
            f"Total warning signs found: {len(findings)}"
        )
        findings.append("REVIEW CAREFULLY before trusting this URL.")

    return findings


def main():
    print("EWB Phishing URL Awareness Checker")
    print("Text checks only - this program does not open URLs.")

    while True:
        raw_url = input(
            "\nEnter a sample URL (or type quit): "
        )

        if raw_url.lower().strip() in ("quit", "q"):
            print("Thank you for using the checker!")
            break

        print("\nResult:")

        for item in inspect_url(raw_url):
            print("- " + item)

        print("\nNever enter passwords from unexpected links.")


if __name__ == "__main__":
    main()
