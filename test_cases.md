# Test Cases for Blockchain Portal

## 1. Authentication Test Cases

### Sign Up
#### Success Scenarios:
1. Valid email and password
   - Input: Valid email format, password >= 8 chars
   - Expected: Account created successfully

#### Failure Scenarios:
1. Invalid email format
2. Password too short
3. Empty fields
4. Already registered email

### Sign In
#### Success Scenarios:
1. Valid credentials
   - Input: Registered email and correct password
   - Expected: Successfully logged in

#### Failure Scenarios:
1. Invalid email
2. Wrong password
3. Empty fields
4. Unregistered email

### Sign Out
#### Success Scenarios:
1. User successfully logs out
   - Expected: Redirected to login page
   - Session terminated

## 2. Node Onboarding Test Cases

### Add Node
#### Success Scenarios:
1. Valid node details
   - NodeID format: "NodeID-{number}"
   - Valid IP: "X.X.X.X" (0 <= X <= 255)

#### Failure Scenarios:
1. Invalid NodeID format
2. Invalid IP address
3. Duplicate NodeID
4. Empty fields

### Add Wallet
#### Success Scenarios:
1. Valid wallet details
   - Valid wallet address format
   - Valid permission type

#### Failure Scenarios:
1. Invalid wallet address
2. Invalid permission type
3. Duplicate wallet address
4. Empty fields

## 3. Create Private Blockchain Test Cases

### Network Creation
#### Success Scenarios:
1. Valid network name and wallet
   - Unique network name
   - Valid wallet address

#### Failure Scenarios:
1. Empty network name
2. Invalid wallet address
3. Duplicate network name

### Node Addition
#### Success Scenarios:
1. Add multiple valid nodes
   - Valid NodeID and IP formats
   - Unique nodes

#### Failure Scenarios:
1. Invalid node details
2. Duplicate nodes
3. Empty fields

## 4. UI/UX Test Cases

1. Navigation flow
2. Form validation
3. Error messages
4. Loading states
5. Responsive design
6. Button states (enabled/disabled)

## 5. Security Test Cases

1. Session management
2. Input sanitization
3. Authentication token validation
4. Access control
5. Form submission security