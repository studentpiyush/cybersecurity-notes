# Burp Suite

Burp Suite is a web application security testing platform. Its proxy tools let you inspect and modify HTTP(S) requests and responses in an authorized test environment.

## 1. Core Components

- **Proxy:** Intercepts browser traffic so requests and responses can be inspected.
- **HTTP history:** Lists requests observed by Burp.
- **Repeater:** Lets you send a selected request again and change it manually.
- **Intruder:** Automates customized request variations for authorized testing.
- **Decoder:** Encodes or decodes supported data formats.
- **Comparer:** Compares two pieces of data.

Features vary by Burp Suite edition.

## 2. Safe Lab Setup

Use Burp against an application you own or a deliberately vulnerable training application, such as OWASP Juice Shop running locally.

1. Start Burp Suite.
2. Open **Proxy** and verify the proxy listener configuration.
3. Use Burp's built-in browser where available, or configure a separate browser to use the local proxy listener.
4. Visit the lab application.
5. Return to **Proxy → HTTP history** and inspect the captured requests.

Avoid sending credentials, session cookies, or private traffic from everyday browsing through a test proxy.

## 3. Understand an HTTP Request

A request commonly contains:

- Request line, such as `GET / HTTP/1.1`
- `Host` header
- Other headers, such as `User-Agent` or `Accept`
- Optional body, often used with POST or PUT

A response commonly contains:

- Status line, such as `HTTP/1.1 200 OK`
- Response headers
- Optional response body

Status codes are only one part of the result. Check the body, redirects, headers, and application behavior too.

## 4. Basic Proxy Exercise

In a controlled lab:

1. Open the lab site's home page in the configured browser.
2. Find the request in HTTP history.
3. Inspect the method, path, headers, status code, and response.
4. Send the request to Repeater.
5. Resend it without changing anything and compare the response.
6. Change a harmless parameter that belongs to your own test application and observe how the response changes.

Use interception carefully: if **Intercept is on**, the browser may appear to hang until the request is forwarded or dropped.

## 5. HTTPS and Certificates

For HTTPS inspection, Burp must be configured appropriately for the lab browser. Burp's CA certificate is used to intercept TLS traffic through the proxy. Install or trust certificates only in a dedicated testing browser/profile and follow the official instructions; do not weaken system-wide certificate security for convenience.

## 6. Troubleshooting

- **HTTP history is empty:** Confirm the browser is using Burp's proxy and visit a new page.
- **Browser hangs:** Check whether Proxy interception is enabled and a request is waiting to be forwarded.
- **HTTPS certificate warnings:** Review the dedicated browser's proxy CA setup; do not ignore certificate errors indiscriminately.
- **Burp does not start:** Check the installed edition, Java/runtime requirements for that release, and the official installation guide.
- **Wrong application traffic appears:** Use a dedicated lab browser/profile and verify the target URL.

## 7. Practice Checklist

- [ ] Capture a GET request and explain its headers.
- [ ] Find a POST request in HTTP history and identify its body.
- [ ] Send a request to Repeater and compare two responses.
- [ ] Identify a redirect and inspect its `Location` header.
- [ ] Compare an HTTP response status code with the actual response content.
- [ ] Document one issue you encountered and how you resolved it.

Only test applications you own or have explicit permission to assess. Avoid destructive actions and do not expose secrets in saved requests or public notes.

## References

- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [Burp Suite Documentation](https://portswigger.net/burp/documentation)
- [Burp Suite Getting Started](https://portswigger.net/burp/documentation/desktop/getting-started)
