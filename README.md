<div align="center">

<img src="./logo.png" alt="FH Development" width="220">

# FH Development CDN

### ⚡ High-performance content delivery for modern applications.

[![Status](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)
[![CDN](https://img.shields.io/badge/CDN-Operational-1677ff?style=for-the-badge\&logo=cloudflare\&logoColor=white)](#)
[![HTTPS](https://img.shields.io/badge/HTTPS-Enabled-1677ff?style=for-the-badge\&logo=letsencrypt\&logoColor=white)](#)
[![Maintained](https://img.shields.io/badge/Maintained-FH%20Development-1677ff?style=for-the-badge)](#)

<br>

**Fast delivery · Reliable infrastructure · Developer-first**

</div>

---

<div align="center">

### 🌐 Infrastructure built for the web

FH Development CDN provides a reliable, developer-friendly platform for distributing
static assets and public content across the internet.

**[Documentation](#-documentation) · [Usage](#-usage) · [Status](#-service-status) · [Security](#-security)**

</div>

---

## 📖 Overview

The **FH Development CDN** is a dedicated content delivery layer designed to make
serving public assets simple, fast, and reliable.

It can be used for:

* 🌐 Websites
* ⚡ Web applications
* 📦 JavaScript packages
* 🎨 CSS stylesheets
* 🖼️ Images
* 🔤 Fonts
* 🎬 Media
* 📄 Static files
* 🧩 Application resources
* 📥 Public downloads

The CDN is designed around a simple principle:

> **Your users should get the content they need, as quickly and reliably as possible.**

---

# 🏗️ Architecture

```text
                         ┌──────────────────────┐
                         │      End Users       │
                         │   🌍 Worldwide        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │    FH Development    │
                         │         CDN          │
                         └──────────┬───────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
              ┌──────────┐   ┌──────────┐   ┌──────────┐
              │  Static  │   │  Assets  │   │ Downloads│
              │  Content │   │  Images  │   │  Files   │
              └──────────┘   └──────────┘   └──────────┘
                    │               │               │
                    └───────────────┼───────────────┘
                                    ▼
                         ┌──────────────────────┐
                         │   Origin Storage     │
                         │ / Application Layer  │
                         └──────────────────────┘
```

---

# ⚡ Features

<table>
<tr>
<td width="50%">

### 🚀 Performance

Optimised delivery for static resources with caching and efficient HTTP delivery.

</td>
<td width="50%">

### 🌍 Global Availability

Public content can be accessed from anywhere with an internet connection.

</td>
</tr>

<tr>
<td>

### 🔒 Secure Delivery

HTTPS-enabled delivery helps protect content while it travels between users and infrastructure.

</td>
<td>

### 📦 Static Asset Support

Designed for images, scripts, stylesheets, fonts, downloads and other public resources.

</td>
</tr>

<tr>
<td>

### 📊 Monitoring

Service availability is monitored through Better Stack.

</td>
<td>

### 🛠️ Developer Friendly

Simple URLs make integration with websites and applications straightforward.

</td>
</tr>
</table>

---

# 📡 CDN Endpoint

The primary CDN endpoint is:

```text
https://cdn.fhdevelopment.co.uk/
```

## Endpoint structure

```text
https://cdn.fhdevelopment.co.uk/<path>
```

For example:

```text
https://cdn.fhdevelopment.co.uk/assets/logo.svg
```

```text
https://cdn.fhdevelopment.co.uk/css/main.css
```

```text
https://cdn.fhdevelopment.co.uk/js/application.js
```

```text
https://cdn.fhdevelopment.co.uk/images/banner.webp
```

---

# 💻 Usage

## HTML

```html
<img
  src="https://cdn.fhdevelopment.co.uk/images/example.webp"
  alt="Example"
>
```

---

## CSS

```css
.hero {
    background-image: url(
        "https://cdn.fhdevelopment.co.uk/images/hero.webp"
    );
}
```

---

## JavaScript

```html
<script
    src="https://cdn.fhdevelopment.co.uk/js/application.js">
</script>
```

---

## Stylesheets

```html
<link
    rel="stylesheet"
    href="https://cdn.fhdevelopment.co.uk/css/main.css">
```

---

## Markdown

```markdown
![FH Development](https://cdn.fhdevelopment.co.uk/images/logo.png)
```

---

# 🗂️ Recommended Asset Structure

For larger projects, we recommend keeping assets organised using predictable paths.

```text
/
├── assets/
│   ├── images/
│   ├── icons/
│   └── fonts/
│
├── css/
│   ├── main.css
│   └── components.css
│
├── js/
│   ├── application.js
│   └── components.js
│
├── media/
│   ├── video/
│   └── audio/
│
└── downloads/
    └── ...
```

This makes assets easier to discover, maintain and reference.

---

# 🧠 Caching Strategy

CDN performance depends heavily on effective caching.

For versioned assets, we recommend immutable filenames:

```text
application.8f32c1.js
```

instead of:

```text
application.js
```

### Recommended workflow

```text
Source
  │
  ▼
Build
  │
  ▼
Version / Hash Assets
  │
  ▼
Upload
  │
  ▼
FH Development CDN
  │
  ▼
Users
```

Versioning assets allows new releases to coexist with older cached resources without
requiring users to manually clear their cache.

---

# 🔐 Security

The CDN is intended for **publicly accessible content**.

### Never upload:

* ❌ Passwords
* ❌ API keys
* ❌ Authentication tokens
* ❌ Private credentials
* ❌ Database credentials
* ❌ `.env` files
* ❌ Private customer information
* ❌ Internal configuration
* ❌ Sensitive application data

A CDN asset should be treated as public once it has been published.

### Example

**❌ Do not do this:**

```text
cdn.fhdevelopment.co.uk/config/production.env
```

**✅ Prefer this:**

```text
cdn.fhdevelopment.co.uk/assets/application.js
```

---

# 📊 Service Status

Current service availability is monitored through Better Stack.

<div align="center">

[![Better Stack Badge](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

</div>

### Monitoring

| Component          | Monitoring      |
| ------------------ | --------------- |
| CDN Endpoint       | 🟢 Active       |
| HTTP Delivery      | 🟢 Active       |
| HTTPS              | 🟢 Active       |
| Asset Availability | 🟢 Active       |
| Uptime Monitoring  | 🟢 Better Stack |

> **Important:** The table above is informational. For real-time availability, use the Better Stack monitor.

---

# 🚨 Incidents

If an outage or degradation occurs, service information should be published through the
official FH Development status infrastructure.

### During an incident

```text
Incident detected
       │
       ▼
Infrastructure investigated
       │
       ▼
Impact identified
       │
       ▼
Mitigation applied
       │
       ▼
Service restored
       │
       ▼
Incident reviewed
```

Post-incident improvements should be incorporated into the infrastructure where appropriate.

---

# 📈 Performance Philosophy

FH Development CDN follows a few core principles:

### 01 — Keep content close to users

Reduce unnecessary distance between users and the content they request.

### 02 — Cache aggressively where appropriate

Static resources should be cached whenever their lifecycle allows it.

### 03 — Version your assets

Immutable asset versions make deployments safer and more predictable.

### 04 — Keep URLs predictable

A clean URL structure makes integration and debugging easier.

### 05 — Monitor continuously

Infrastructure should be monitored rather than assumed to be operational.

---

# 🧪 Testing

Before publishing an asset, verify that it can be accessed correctly.

```bash
curl -I https://cdn.fhdevelopment.co.uk/example/file.css
```

You should receive an appropriate HTTP response from the CDN.

You can also test an asset directly:

```bash
curl -L \
  https://cdn.fhdevelopment.co.uk/example/file.css
```

---

# 🔧 Developer Checklist

Before publishing an asset:

* [ ] File is intended to be public
* [ ] No credentials are included
* [ ] No private information is included
* [ ] Filename is production-ready
* [ ] Asset has been tested
* [ ] Correct MIME type is being served
* [ ] Cache behaviour is appropriate
* [ ] Versioning is used where required
* [ ] Asset URL has been verified

---

# 📚 Documentation

Documentation for individual projects can be maintained alongside their respective
repositories.

A typical integration looks like:

```text
Project
   │
   ├── Source Code
   │
   ├── Build System
   │
   └── Public Assets
          │
          ▼
    FH Development CDN
          │
          ▼
       End Users
```

---

# 🛣️ Roadmap

Potential future improvements include:

* [ ] Expanded edge infrastructure
* [ ] Improved cache controls
* [ ] Automated asset publishing
* [ ] Deployment automation
* [ ] CDN analytics
* [ ] Additional monitoring
* [ ] Automated cache invalidation
* [ ] Developer API
* [ ] Asset management tooling
* [ ] Advanced security controls

> Roadmap items are subject to change based on infrastructure requirements and project priorities.

---

# 🏢 FH Development

**FH Development** is focused on building reliable software, web infrastructure and
developer-focused services.

Our infrastructure is designed around:

```text
Reliability
     +
Performance
     +
Security
     +
Developer Experience
     │
     ▼
FH Development
```

---

# 🤝 Contributing

If this repository contains configuration, documentation or tooling related to the
FH Development CDN, contributions are welcome where appropriate.

### Suggested workflow

```bash
git clone <repository>
cd <repository>

git checkout -b feature/my-change

# Make your changes

git add .
git commit -m "feat: improve CDN configuration"

git push origin feature/my-change
```

Then open a pull request with a clear description of the changes.

---

# 📜 Licence

Unless otherwise specified, the source code, configuration and documentation in this
repository are subject to the licence provided with the project.

Content served through the CDN may have separate ownership and licensing terms.

---

<div align="center">

<img src="./logo.png" alt="FH Development" width="120">

## FH Development

**Build better. Deliver faster.**

<br>

[![Better Stack](https://uptime.betterstack.com/status-badges/v2/monitor/2wyci.svg)](https://uptime.betterstack.com/?utm_source=status_badge)

<br><br>

`© FH Development`

</div>

