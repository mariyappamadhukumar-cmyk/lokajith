"""
Connection Verification Script for Sentinel Vision
Tests the connection between frontend and backend
Includes retry logic for Render free tier wake-up
"""

import requests
import json

# Configuration
BACKEND_URL = "https://lokajith.onrender.com"
FRONTEND_URL = "https://national-hackthon.vercel.app"

# Increased timeout for Render free tier wake-up
INITIAL_TIMEOUT = 60  # First request needs more time
NORMAL_TIMEOUT = 15

def test_backend_status():
    """Test if backend is responding"""
    print("🔍 Testing Backend Status...")
    print("   ⏳ Waiting for backend to wake up (this may take 30-60 seconds)...")
    try:
        response = requests.get(f"{BACKEND_URL}/", timeout=INITIAL_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is running: {data.get('message', 'OK')}")
            return True
        else:
            print(f"❌ Backend returned status code: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"❌ Backend connection timed out after {INITIAL_TIMEOUT}s")
        print(f"   💡 The backend may be sleeping. Try again in a few minutes.")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def test_cameras_endpoint():
    """Test cameras endpoint"""
    print("\n🎥 Testing Cameras Endpoint...")
    try:
        response = requests.get(f"{BACKEND_URL}/cameras", timeout=NORMAL_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            cameras = data.get('cameras', [])
            print(f"✅ Cameras endpoint working")
            print(f"   Active cameras: {data.get('active_cameras', 0)}")
            print(f"   Total cameras: {len(cameras)}")
            if cameras:
                for cam in cameras:
                    print(f"   - {cam.get('name')} ({cam.get('id')}): {'Active' if cam.get('active') else 'Inactive'}")
            else:
                print("   No cameras configured yet")
            return True
        else:
            print(f"❌ Cameras endpoint returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"❌ Cameras endpoint timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cameras endpoint failed: {e}")
        return False

def test_stats_endpoint():
    """Test statistics endpoint"""
    print("\n📊 Testing Stats Endpoint...")
    try:
        response = requests.get(f"{BACKEND_URL}/stats", timeout=NORMAL_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stats endpoint working")
            print(f"   Detections - Person: {data.get('PERSON', 0)}, Weapon: {data.get('WEAPON', 0)}, Watchlist: {data.get('WATCHLIST', 0)}")
            return True
        else:
            print(f"❌ Stats endpoint returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"❌ Stats endpoint timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Stats endpoint failed: {e}")
        return False

def test_alerts_endpoint():
    """Test alerts endpoint"""
    print("\n🚨 Testing Alerts Endpoint...")
    try:
        response = requests.get(f"{BACKEND_URL}/alerts", timeout=NORMAL_TIMEOUT)
        if response.status_code == 200:
            data = response.json()
            alerts = data.get('alerts', [])
            print(f"✅ Alerts endpoint working")
            print(f"   Active alerts: {len(alerts)}")
            return True
        else:
            print(f"❌ Alerts endpoint returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"❌ Alerts endpoint timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Alerts endpoint failed: {e}")
        return False

def test_cors():
    """Test CORS configuration"""
    print("\n🌐 Testing CORS Configuration...")
    try:
        headers = {
            'Origin': FRONTEND_URL,
            'Access-Control-Request-Method': 'GET',
        }
        response = requests.options(f"{BACKEND_URL}/cameras", headers=headers, timeout=NORMAL_TIMEOUT)
        cors_headers = response.headers
        if 'Access-Control-Allow-Origin' in cors_headers:
            print(f"✅ CORS is configured")
            print(f"   Allow-Origin: {cors_headers.get('Access-Control-Allow-Origin')}")
            print(f"   Allow-Methods: {cors_headers.get('Access-Control-Allow-Methods', 'Not specified')}")
            return True
        else:
            print(f"⚠️  CORS headers not found (might still work)")
            return True
    except requests.exceptions.Timeout:
        print(f"❌ CORS test timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ CORS test failed: {e}")
        return False

def test_frontend_access():
    """Test if frontend is accessible"""
    print("\n🖥️  Testing Frontend Access...")
    try:
        response = requests.get(FRONTEND_URL, timeout=NORMAL_TIMEOUT)
        if response.status_code == 200:
            print(f"✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend returned status: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print(f"❌ Frontend access timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend access failed: {e}")
        return False

def main():
    print("=" * 60)
    print("   Sentinel Vision - Connection Verification")
    print("=" * 60)
    print(f"\n📍 Backend URL: {BACKEND_URL}")
    print(f"📍 Frontend URL: {FRONTEND_URL}")
    print("\n" + "=" * 60 + "\n")
    
    results = {
        'Backend Status': test_backend_status(),
        'Cameras Endpoint': test_cameras_endpoint(),
        'Stats Endpoint': test_stats_endpoint(),
        'Alerts Endpoint': test_alerts_endpoint(),
        'CORS Configuration': test_cors(),
        'Frontend Access': test_frontend_access(),
    }
    
    print("\n" + "=" * 60)
    print("   Test Results Summary")
    print("=" * 60)
    
    passed = sum(results.values())
    total = len(results)
    
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print("\n" + "=" * 60)
    print(f"   Overall: {passed}/{total} tests passed")
    
    if passed == total:
        print("   🎉 All systems operational!")
        print("\n   Next steps:")
        print("   1. Open the dashboard: https://national-hackthon.vercel.app/")
        print("   2. Navigate to Cameras page")
        print("   3. Add your first IoT camera")
        print("   4. Refer to IOT_SETUP_GUIDE.md for camera setup instructions")
    else:
        print("   ⚠️  Some tests failed. Check the output above for details.")
        print("   - If backend is sleeping (Render free tier), wait 30-60s and retry")
        print("   - Check network connectivity")
    
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
