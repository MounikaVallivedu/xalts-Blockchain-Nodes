"""Test data for blockchain portal automation"""

# Authentication Test Data
VALID_USER = {
    "email": "test.user@example.com",
    "password": "Test@123456"
}

INVALID_USERS = [
    {
        "email": "invalid.email",
        "password": "Test@123",
        "error": "Invalid email format"
    },
    {
        "email": "test.user@example.com",
        "password": "123",  # Too short
        "error": "Password must be at least 8 characters"
    },
    {
        "email": "",
        "password": "",
        "error": "Email and password are required"
    }
]

# Node Test Data
VALID_NODES = [
    {
        "node_id": "NodeID-123456",
        "ip": "192.168.1.1"
    },
    {
        "node_id": "NodeID-789012",
        "ip": "10.0.0.1"
    }
]

INVALID_NODES = [
    {
        "node_id": "Invalid-ID",
        "ip": "192.168.1.1",
        "error": "Invalid node ID format"
    },
    {
        "node_id": "NodeID-123456",
        "ip": "256.1.1.1",
        "error": "Invalid IP address"
    }
]

# Wallet Test Data
VALID_WALLETS = [
    {
        "address": "0x88fa61d2faA13aad8Fbd5B030372B4A159BbbDFb",
        "permission": "admin"
    }
]

INVALID_WALLETS = [
    {
        "address": "0xinvalid",
        "permission": "admin",
        "error": "Invalid wallet address format"
    }
]