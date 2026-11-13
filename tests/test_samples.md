
# Phishing URL Awareness Checker - Test Samples

## Test 1: Normal Example URL

URL: https://www.example.com/login

Expected Result:
- No listed warning signs found. This does NOT prove safety.

## Test 2: IP Address URL

URL: http://192.0.2.10/account

Expected Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP. HTTPS alone does not prove trust.
- Total warning signs found: 2
- REVIEW CAREFULLY before trusting this URL.

## Test 3: URL Contains @ Symbol

URL: http://example.com@sample.invalid/login

Expected Result:
- Contains an @ symbol; inspect carefully.
- Uses HTTP. HTTPS alone does not prove trust.
- Total warning signs found: 2
- REVIEW CAREFULLY before trusting this URL.

## Test 4: Multiple Hostname Labels

URL: https://a.b.c.d.e.example.invalid/path

Expected Result:
- Contains many hostname segments/subdomains.
- Total warning signs found: 1
- REVIEW CAREFULLY before trusting this URL.

## Test 5: Punycode URL

URL: https://xn--example.invalid/

Expected Result:
- Contains a punycode-style hostname.
- Total warning signs found: 1
- REVIEW CAREFULLY before trusting this URL.

## Additional Test: Invalid URL

URL: http://[bad

Expected Result:
- Invalid URL format. Please enter a valid URL.
