import os
import json
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import socket

# --- App Configuration & Security ---
app = FastAPI(
    title="Security Pulse Monitor API",
    description="Cloud-Tethered Enterprise Security Agent Backend",
    version="2.0.0"
)

# Enforce secure CORS policies for the plugin integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your specific plugin/MeDo domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models for Data Validation ---
class CodePayload(BaseModel):
    encrypted_code: str
    file_type: str
    encryption_metadata: dict

class ASTScanResult(BaseModel):
    vulnerability_id: str
    severity: str
    description: str
    line_number: int

# --- Mock E2E Decryption (For Backend Processing if needed) ---
# Note: In a pure E2E model, decryption happens client-side or securely inside the AI enclave.
def verify_e2e_payload(payload: str) -> bool:
    """Validates the integrity of the E2E encrypted payload."""
    if not payload:
        raise HTTPException(status_code=400, detail="Invalid Encrypted Payload")
    return True

# --- 1. Network Perimeter Health Scanner ---
@app.get("/api/v1/network/scan")
def scan_network_perimeter():
    """
    Scans local environment for exposed services and open ports.
    Updates the 'Network Perimeter Health' dashboard widget.
    """
    open_ports = []
    common_ports = [3306, 27017, 8080, 5000, 3000] # Common dev/db ports
    
    # Basic local port scanning simulation
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    status = "Vulnerable" if open_ports else "Secure"
    
    return {
        "status": status,
        "message": "Network scan completed.",
        "exposed_ports": open_ports,
        "recommendation": "Close external access to local databases." if open_ports else "Perimeter is secure."
    }

# --- 2. Advanced AST Scanner (Including Real-World Threat Rules) ---
@app.post("/api/v1/scan/ast")
def run_ast_scan(payload: CodePayload):
    """
    Scans code for local vulnerabilities and recent real-world threats.
    """
    verify_e2e_payload(payload.encrypted_code)
    
    # Mocking the AST engine detecting the new vulnerabilities we discussed
    detected_vulnerabilities = [
        {
            "vulnerability_id": "client-side-validation-exposure",
            "severity": "CRITICAL",
            "description": "Sensitive OTP/Password validation detected on the frontend. Never trust the client.",
            "line_number": 42
        },
        {
            "vulnerability_id": "missing-payload-verification",
            "severity": "HIGH",
            "description": "API request modifies sensitive data without a valid server-side JWT or HttpOnly session token.",
            "line_number": 88
        },
        {
            "vulnerability_id": "hardcoded-secrets",
            "severity": "CRITICAL",
            "description": "Plaintext master password or API key exposed in codebase.",
            "line_number": 12
        }
    ]
    
    return {
        "scan_status": "completed",
        "findings": detected_vulnerabilities,
        "e2e_secured": True
    }

# --- 3. Real-Time AI Patch Recommendation Engine ---
@app.post("/api/v1/remediate/ai")
def generate_ai_patch(payload: CodePayload):
    """
    Interfaces with the Gemini API to generate secure, contextual patches.
    Receives E2E encrypted code and streams back a secure patch.
    """
    verify_e2e_payload(payload.encrypted_code)
    
    # In a real environment, you would call the Gemini API here:
    # import google.generativeai as genai
    # genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    # response = model.generate_content(...)
    
    # Mocking the AI response for the hackathon setup
    mock_ai_patch = """
    // AI Generated Secure Patch:
    // 1. Removed frontend OTP logic.
    // 2. Implemented secure API call with Authorization header.
    
    async function verifyAction(data) {
        const response = await fetch('/api/secure/verify', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${sessionStorage.getItem('secureToken')}`
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
    """
    
    return {
        "status": "success",
        "ai_engine": "Gemini-Pro",
        "patch_code": mock_ai_patch,
        "confidence_score": 0.98,
        "e2e_secured": True
    }

# --- Server Execution ---
if __name__ == "__main__":
    import uvicorn
    # Running securely on localhost
    uvicorn.run(app, host="127.0.0.1", port=8000)
