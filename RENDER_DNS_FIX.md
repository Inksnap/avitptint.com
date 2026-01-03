# Fix DNS for Render Custom Domain

## Current Issue
Your A record points to `84.32.84.32` (likely Hostinger parked domain IP), causing the parked page to show instead of your Render site.

## Steps to Fix

### 1. Get DNS Records from Render
- Go to Render Dashboard
- Navigate to: **Your Service** → **Settings** → **Custom Domains**
- Find `avitprint.com` in the list
- Copy the DNS records shown (they'll look like this):

**For Root Domain (@):**
- Type: A
- Value: [Render's IP address - usually something like 76.76.21.21 or similar]

**For www subdomain:**
- Type: CNAME  
- Value: [your-service-name].onrender.com

### 2. Update DNS Records

#### Update A Record (Root Domain)
1. In your DNS management panel (where you saw the screenshot)
2. Click **Edit** on the A record with:
   - Type: A
   - Name: @
   - Content: 84.32.84.32 ← **CHANGE THIS**
3. Change Content to Render's IP address (from step 1)
4. Save changes

#### Update CNAME Record (www)
1. Click **Edit** on the CNAME record with:
   - Type: CNAME
   - Name: www
   - Content: avitprint.com ← **CHANGE THIS**
2. Change Content to: `[your-render-service].onrender.com` (from step 1)
3. Save changes

### 3. Wait for DNS Propagation
- Changes can take 1-48 hours to propagate
- Check status: https://www.whatsmydns.net/#A/avitprint.com
- The TTL of 50 seconds means changes should propagate quickly

### 4. Verify on Render
- After DNS propagates, Render will automatically:
  - Issue SSL certificate
  - Activate your custom domain
- Check Render dashboard to confirm domain status is "Active"

## Important Notes
- **DO NOT** delete the CAA records - they're needed for SSL certificates
- Keep TTL values reasonable (300-3600 seconds)
- If Render shows different instructions, follow those instead

## Common Render IP Addresses
Render uses different IPs, but common ones include:
- 76.76.21.21
- 76.76.21.22
- Or check your Render dashboard for the exact IP

**Always use the IP address shown in your Render Custom Domains section!**


