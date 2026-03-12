# Sentinel Vision - Quick Start Guide

## 🎯 System Overview

Your Sentinel Vision system is now **fully configured and ready** for IoT camera integration!

### Deployment Status ✅

| Component | Status | URL |
|-----------|--------|-----|
| Backend API | 🟢 Deployed | https://lokajith.onrender.com |
| Frontend Dashboard | 🟢 Deployed | https://national-hackthon.vercel.app/ |
| IoT Integration | 🟢 Ready | Cameras can be added via dashboard |

---

## 🚀 Quick Start Steps

### 1. Verify the Connection (Recommended)

Run the verification script to test all endpoints:

```bash
cd c:\Users\Madhukumar\Downloads\National_Hackthon-main
python verify_connection.py
```

### 2. Access the Dashboard

Open your browser and navigate to:
**https://national-hackthon.vercel.app/**

### 3. Add Your First Camera

#### Option A: Use Mobile Phone as Camera

1. **Install IP Webcam app** on your Android phone (from Google Play Store)
2. **Start the server** in the app
3. **Note the IP address** shown (e.g., `192.168.1.100:8080`)
4. **In the Dashboard**:
   - Go to "Cameras" page
   - Click "Add Camera"
   - Fill in:
     - Name: `Mobile Camera 1`
     - Camera ID: `mobile-cam-1`
     - URL: `http://192.168.1.100:8080/video`
5. **Click Save** and watch the live feed appear!

#### Option B: Use IP/Network Camera

If you have an IP camera with RTSP stream:
- URL format: `rtsp://username:password@camera-ip:554/stream1`
- Example: `rtsp://admin:password123@192.168.1.64:554/stream1`

---

## 📱 IoT Camera Options

Your system supports:
- ✅ Mobile phones (IP Webcam, DroidCam apps)
- ✅ IP/Network cameras (RTSP, MJPEG)
- ✅ ESP32-CAM modules
- ✅ Raspberry Pi cameras
- ✅ USB webcams (local development only)

**See detailed setup instructions in: `IOT_SETUP_GUIDE.md`**

---

## 🔧 Configuration Files

All configuration is complete:

### Frontend Configuration
- File: `ui sentinal vision/.env`
- File: `ui sentinal vision/.env.production`
- Backend URL: `https://lokajith.onrender.com`

### Backend Configuration
- File: `sentinel-vision/backend/main.py`
- CORS: Enabled for all origins
- IoT Camera Support: ✅ Active

---

## 🧪 Testing Checklist

- [ ] Backend responds at https://lokajith.onrender.com/
- [ ] Frontend loads at https://national-hackthon.vercel.app/
- [ ] Add at least one test camera
- [ ] Verify live video feed displays
- [ ] Test detection by showing objects to camera
- [ ] Check alerts panel for detections

---

## 📚 Important Files

1. **IOT_SETUP_GUIDE.md** - Comprehensive guide for setting up IoT cameras
2. **verify_connection.py** - Script to test all API endpoints
3. **sentinel-vision/README.md** - Backend documentation
4. **ui sentinal vision/README.md** - Frontend documentation

---

## 🆘 Troubleshooting

### Backend Not Responding
- **Issue**: Render free tier might sleep after inactivity
- **Solution**: First request takes 30-60 seconds to wake up. Be patient and refresh.

### Camera Feed Not Showing
1. Test camera URL in VLC Media Player first
2. Ensure camera and backend are on compatible networks
3. Check camera credentials are correct
4. For local cameras behind NAT, use port forwarding or VPN

### "Backend Stream Unavailable" Error
1. Wait 30-60 seconds for backend to wake up
2. Check backend status: https://lokajith.onrender.com/
3. Verify camera URL is accessible from internet (for cloud deployment)

---

## 🎥 API Endpoints

Quick reference for API integration:

```bash
# Check status
GET https://lokajith.onrender.com/

# List cameras
GET https://lokajith.onrender.com/cameras

# Get live feed
GET https://lokajith.onrender.com/video-feed/{camera_id}

# Get alerts
GET https://lokajith.onrender.com/alerts

# Get detection statistics
GET https://lokajith.onrender.com/stats
```

Full API documentation: https://lokajith.onrender.com/docs

---

## 🎉 You're All Set!

Your Sentinel Vision system is fully operational:

✅ Backend deployed and configured  
✅ Frontend connected to backend  
✅ CORS properly configured  
✅ IoT camera integration ready  
✅ Real-time detection active  

**Next Step**: Add your first camera and start monitoring!

---

## 📞 Quick Links

- 🌐 Dashboard: https://national-hackthon.vercel.app/
- 🔧 API: https://lokajith.onrender.com/
- 📖 API Docs: https://lokajith.onrender.com/docs
- 📊 System Stats: https://lokajith.onrender.com/stats

Happy monitoring! 🚀🔒
