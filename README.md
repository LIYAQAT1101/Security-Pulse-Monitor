# 🛡️ Security Pulse Monitor (SPM)

Live MeDo App: (https://app-blvqgqf4hk3l.appmedo.com/)

Watch Demo Video: https://youtu.be/23g5CE6OtNw?si=RCRf6ACVaJtsc_dX

> **The ultimate safety net for the AI generation of developers.** > A Cloud-Tethered Enterprise Security Agent designed to intercept, analyze, and instantly patch vulnerabilities in AI-generated code before they hit production.

## 🚀 Overview

The rapid adoption of AI coding assistants (like Copilot and Gemini) has accelerated development speeds, but it has also introduced a new wave of security blind spots—from hallucinated vulnerabilities to hardcoded secrets and bypassed backend validations. 

**Security Pulse Monitor** bridges this gap. Starting as a strict local SAST tool, it has evolved into a robust, cloud-tethered security agent. It actively scans your local environment, analyzes codebase vulnerabilities, and leverages a secure AI Patch Engine to rewrite vulnerable code into enterprise-grade secure architecture in real-time.

## ✨ Core Features

* **🧠 Real-Time AI Patch Recommendation Engine**
  Integrates with the Gemini API to deeply analyze complex AST-flagged vulnerabilities. Instead of just highlighting errors, it dynamically streams contextual, custom-written patch code directly into your IDE's Inline Hint Panels.
* **🌐 Continuous Automated Network Scanner**
  Actively monitors your local environment and open ports. The real-time "Network Perimeter Health" widget instantly flags exposed databases, insecure local APIs, and unintended outward-facing services.
* **🔒 End-to-End (E2E) Encrypted Pipeline**
  Your proprietary code remains yours. All code snippets, telemetry, and AST results sent to the AI Patch Engine are symmetrically encrypted client-side. Look for the "E2E Secured" lock badge in the UI.
* **⚡ Real-World Threat Engine**
  Rules are inspired by real-world data breaches. We specifically target modern web dev blunders, including:
  * `client-side-validation-exposure`: Detects sensitive verifications (like OTPs) improperly handled on the frontend.
  * `missing-payload-verification`: Flags API requests missing secure server-validated session tokens (JWT/HttpOnly).
  * `hardcoded-secrets`: Instantly catches plaintext API keys and master passwords.

## 🛠️ Architecture

Security Pulse Monitor operates on a **Secure Cloud-Tethered Policy**. 
1. **Local Intercept:** Code is written (or AI-generated) and scanned locally using an advanced Abstract Syntax Tree (AST) engine.
2. **Encryption:** Vulnerable snippets are encrypted symmetrically on the client side.
3. **Cloud Analysis:** The encrypted payload is securely transmitted to the AI engine for remediation logic.
4. **Local Patching:** Secure, enterprise-ready code is streamed back, decrypted locally, and applied via multi-cursor auto-fixes.

## 📦 Installation & Setup

*(Ensure your MeDo workspace or local IDE supports plugin integrations before starting)*

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/security-pulse-monitor.git](https://github.com/your-username/security-pulse-monitor.git)
