<div align="center">

<img src="https://cdn.fh-development.xyz/departmental/logos/White_Logo.jpg" alt="FH Development" width="220">

# FH Development CDN

### ⚡ High-performance content delivery for modern applications.

[![Status](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)
[![CDN](https://img.shields.io/badge/CDN-Operational-1677ff?style=for-the-badge\&logo=cloudflare\&logoColor=white)](#-service-status)
[![HTTPS](https://img.shields.io/badge/HTTPS-Enabled-1677ff?style=for-the-badge\&logo=letsencrypt\&logoColor=white)](#-security)
[![Maintained](https://img.shields.io/badge/Maintained-FH%20Development-1677ff?style=for-the-badge)](#-fh-development)

<br>

**Fast delivery · Reliable infrastructure · Developer-first**

</div>

---

<div align="center">

### 🌐 Infrastructure built for the modern web

FH Development CDN provides fast, secure and reliable delivery of public
assets for websites, applications and digital services.

**[Usage](#-usage) · [Performance](#-performance) · [Security](#-security) · [Status](#-service-status)**

</div>

---

## 📖 Overview

**FH Development CDN** is a content delivery platform operated by **FH Development**,
built to provide dependable delivery of publicly accessible web assets.

The CDN is suitable for:

* 🌐 Websites
* ⚡ Web applications
* 📦 JavaScript
* 🎨 CSS
* 🖼️ Images
* 🔤 Fonts
* 🎬 Media
* 📄 Documents
* 📥 Downloads
* 🧩 Public application resources

The goal is simple:

> **Deliver the right content, quickly and reliably, wherever your users are.**

---

# 🚀 Why FH Development CDN?

<table>
<tr>
<td width="50%">

### ⚡ Performance

Optimised delivery and caching for static resources help reduce unnecessary latency and improve page load times.

</td>
<td width="50%">

### 🌍 Global Reach

Public resources can be accessed by users anywhere with an internet connection.

</td>
</tr>

<tr>
<td>

### 🔒 Secure by Default

HTTPS delivery helps protect traffic between clients and the CDN.

</td>
<td>

### 📊 Continuous Monitoring

Availability is monitored through Better Stack to help identify service interruptions quickly.

</td>
</tr>

<tr>
<td>

### 🛠️ Developer First

Simple, predictable URLs make integrating assets into applications straightforward.

</td>
<td>

### 📦 Flexible Content

Designed to support everything from small icons to larger public downloads.

</td>
</tr>
</table>

---

# 📡 CDN Endpoint

The primary FH Development CDN endpoint is:

```text
https://cdn.fh-development.xyz/
```

### Request format

```text
https://cdn.fh-development.xyz/<path-to-resource>
```

### Examples

```text
https://cdn.fh-development.xyz/assets/logo.svg
```

```text
https://cdn.fh-development.xyz/css/main.css
```

```text
https://cdn.fh-development.xyz/js/application.js
```

```text
https://cdn.fh-development.xyz/images/banner.webp
```

---

# 💻 Usage

Integrating the CDN into an application is as simple as referencing the required resource.

## HTML

```html
<img
    src="https://cdn.fh-development.xyz/images/example.webp"
    alt="Example"
>
```

---

## CSS

```css
.hero {
    background-image: url(
        "https://cdn.fh-development.xyz/images/hero.webp"
    );
}
```

---

## JavaScript

```html
<script
    src="https://cdn.fh-development.xyz/js/application.js">
</script>
```

---

## Stylesheets

```html
<link
    rel="stylesheet"
    href="https://cdn.fh-development.xyz/css/main.css"
>
```

---

## Fonts

```css
@font-face {
    font-family: "FHFont";
    src: url(
        "https://cdn.fh-development.xyz/fonts/example.woff2"
    ) format("woff2");
}
```

---

## Markdown

```markdown
![FH Development](https://cdn.fh-development.xyz/images/logo.png)
```

---

# 🌐 HTTP Support

The CDN is designed around standard HTTP delivery.

### Common methods

| Method    | Purpose                             |
| --------- | ----------------------------------- |
| `GET`     | Retrieve a resource                 |
| `HEAD`    | Inspect resource headers            |
| `OPTIONS` | Inspect supported request behaviour |

For most integrations, `GET` is all that is required.

---

# 📦 Content Types

The CDN can be used for common web content including:

| Category  | Examples                             |
| --------- | ------------------------------------ |
| Images    | PNG, JPG, JPEG, GIF, SVG, WebP, AVIF |
| Styles    | CSS                                  |
| Scripts   | JavaScript                           |
| Fonts     | WOFF, WOFF2, TTF, OTF                |
| Documents | PDF, TXT                             |
| Media     | MP4, WebM, MP3                       |
| Archives  | ZIP, TAR, GZ                         |
| Data      | JSON, XML                            |

Actual availability depends on the individual resource and server configuration.

---

# 🧠 Caching

Caching is an important part of CDN performance.

For assets that rarely change, versioned filenames are recommended.

### Recommended

```text
application.8f32c1.js
```

### Avoid where possible

```text
application.js
```

Versioned assets allow deployments to introduce new resources without relying on
users or intermediary caches to immediately discard an older version.

### Example deployment

```text
Application
     │
     ▼
Build
     │
     ▼
Version Assets
     │
     ▼
Publish
     │
     ▼
FH Development CDN
     │
     ▼
     🌍 Users
```

---

# ♻️ Asset Versioning

For frequently updated resources, use a version identifier.

### Version based

```text
https://cdn.fh-development.xyz/js/app-v2.js
```

### Hash based

```text
https://cdn.fh-development.xyz/js/app.4d92fa1.js
```

Hash-based filenames are particularly useful for automated build pipelines.

---

# ⚡ Performance

FH Development CDN is designed around efficient static-content delivery.

For the best results:

* Use modern image formats such as WebP or AVIF where appropriate.
* Compress JavaScript and CSS before publishing.
* Use WOFF2 for modern web fonts.
* Avoid unnecessarily large assets.
* Version frequently changing resources.
* Cache resources that do not change frequently.
* Avoid using the CDN for private application data.

### Example

Instead of delivering:

```text
hero-original-8mb.png
```

consider:

```text
hero.webp
```

with appropriate compression and dimensions.

---

# 🔐 Security

The CDN should be treated as **public infrastructure**.

Anything published to the CDN should be considered potentially accessible by anyone.

### 🚫 Never publish

```text
.env
```

```text
database-password.txt
```

```text
api-keys.json
```

```text
private-config.json
```

```text
credentials.json
```

Never expose:

* ❌ Passwords
* ❌ API keys
* ❌ Authentication tokens
* ❌ Database credentials
* ❌ Private configuration
* ❌ Customer information
* ❌ Personal information
* ❌ Internal secrets

### ✅ Safe examples

```text
/assets/logo.svg
/assets/icons/menu.svg
/css/application.css
/js/application.js
/images/banner.webp
/fonts/inter.woff2
```

---

# 🛡️ HTTPS

All CDN resources should be requested using HTTPS:

```text
https://cdn.fh-development.xyz/
```

Avoid embedding CDN resources using unsecured HTTP:

```text
http://cdn.fh-development.xyz/
```

HTTPS provides encrypted transport between the client and the CDN endpoint.

---

# 🧪 Testing

You can inspect a CDN resource using `curl`.

### Check headers

```bash
curl -I https://cdn.fh-development.xyz/example/file.css
```

### Download a resource

```bash
curl -L \
    https://cdn.fh-development.xyz/example/file.css
```

### Follow redirects

```bash
curl -IL \
    https://cdn.fh-development.xyz/example/file.css
```

---

# 📊 Service Status

FH Development infrastructure is monitored through Better Stack.

<div align="center">

[![Better Stack Status](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

### Real-time monitoring

**CDN availability · HTTP availability · Infrastructure monitoring**

</div>

### Service overview

| Service        | Status         |
| -------------- | -------------- |
| CDN            | 🟢 Operational |
| HTTPS          | 🟢 Operational |
| HTTP Delivery  | 🟢 Operational |
| Asset Delivery | 🟢 Operational |
| Monitoring     | 🟢 Active      |

> For the latest real-time service information, refer to the Better Stack monitor above.

---

# 🚨 Incident Management

If an incident affects CDN availability, FH Development infrastructure can be investigated
and restored using a structured incident process.

```text
┌─────────────────────┐
│   Incident Detected │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Investigate       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Identify Impact   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Apply Mitigation  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Restore Service   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Review & Improve  │
└─────────────────────┘
```

---

# 📈 Reliability

Reliable infrastructure requires more than simply serving files.

FH Development focuses on:

### 01 — Availability

Keep public resources accessible whenever users need them.

### 02 — Performance

Minimise unnecessary latency and optimise static resource delivery.

### 03 — Observability

Monitor infrastructure continuously and identify failures quickly.

### 04 — Security

Keep public infrastructure separate from sensitive application systems.

### 05 — Maintainability

Use predictable URLs, versioned resources and documented practices.

---

# 🔧 Developer Checklist

Before publishing a resource:

* [ ] Resource is intended to be public
* [ ] No credentials are present
* [ ] No secrets are present
* [ ] Resource has been tested
* [ ] MIME type is correct
* [ ] Asset is appropriately compressed
* [ ] Cache behaviour is appropriate
* [ ] Versioning is used where required
* [ ] HTTPS URL works correctly
* [ ] Resource does not contain private information

---

# 🛣️ Roadmap

Future improvements may include:

* [ ] Expanded CDN infrastructure
* [ ] Additional edge locations
* [ ] Advanced cache management
* [ ] Automated deployments
* [ ] Automated cache invalidation
* [ ] CDN analytics
* [ ] Advanced monitoring
* [ ] Developer API
* [ ] Automated asset optimisation
* [ ] Additional security controls

> Roadmap items may change as FH Development infrastructure evolves.

---

# 🏢 FH Development

**FH Development** builds software, infrastructure and developer-focused services
with an emphasis on performance, reliability and maintainability.

Our infrastructure philosophy:

```text
                 ┌───────────────┐
                 │  Performance  │
                 └───────┬───────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌─────────────┐  ┌─────────────┐  ┌─────────────┐
│ Reliability │  │   Security  │  │ Developers  │
└──────┬──────┘  └──────┬──────┘  └──────┬──────┘
       │                │                │
       └────────────────┼────────────────┘
                        ▼
                ┌───────────────┐
                │ FH Development│
                └───────────────┘
```

---

# 🤝 Contributing

Changes to documentation, configuration or supporting tooling should be made through
the normal GitHub contribution process.

```bash
git checkout -b feature/my-change

git add .
git commit -m "docs: improve CDN documentation"

git push origin feature/my-change
```

Pull requests should clearly describe:

* What changed
* Why it changed
* Any infrastructure impact
* Any potential breaking changes

---

# 📜 Licence

Unless otherwise specified, the code and documentation in this repository are provided
under the licence associated with the project.

Assets delivered through the CDN may have separate ownership or licensing requirements.

---

<div align="center">

<img src="https://cdn.fh-development.xyz/departmental/logos/White_Logo.jpg" alt="FH Development" width="130">

# FH Development

### Build better. Deliver faster.

<br>

[![Better Stack](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

<br>

**⚡ Fast · 🔒 Secure · 🌍 Reliable**

<br><br>

`© FH Development`

</div>
