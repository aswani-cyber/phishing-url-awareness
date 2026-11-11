# Phishing URL Checker - Test Samples

## Test 1: Normal Example URL
URL: https://www.example.com/login

Expected Result:
## Test 2: IP Address URL
URL: http://192.0.2.10/account

Expected Result:
- Uses an IP address instead of a familiar domain.
- Uses HTTP.No listed warning signs found.


## Test 3: URL Contains @ Symbol
URL: http://example.com@sample.invalid/login

Expected Result:
- Contains an @ symbol.
- Uses HTTP.

## Test 4: Multiple Subdomains
URL: https://a.b.c.d.e.example.invalid/path

Expected Result:
- Contains many hostname segments/subdomains.

## Test 5: Punycode URL
URL: https://xn--example.invalid/

Expected Result:
- Contains a punycode-style hostname.
