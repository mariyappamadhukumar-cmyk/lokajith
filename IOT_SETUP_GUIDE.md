# Sentinel Vision - IoT Camera Setup & Deployment Guide

## 🌐 Deployment URLs

- **Backend API**: https://lokajith.onrender.com
- **Frontend Dashboard**: https://national-hackthon.vercel.app/
- **API Status**: https://lokajith.onrender.com/ (Check if backend is running)

## ✅ Current Configuration Status

### Backend (Render)
- ✅ Deployed at: `https://lokajith.onrender.com`
- ✅ CORS enabled for all origins
- ✅ Supports IoT camera streams (RTSP, HTTP, IP Webcam apps)
- ✅ Real-time video processing with YOLO detection
- ✅ SQLite database for events and camera management

### Frontend (Vercel)
- ✅ Deployed at: `https://national-hackthon.vercel.app/`
- ✅ Connected to backend API via `.env.production`
- ✅ Real-time camera feed streaming
- ✅ Live alerts and detection dashboard

---

## 📱 IoT Camera Connection Options

### Option 1: Mobile Phone as IP Camera

#### Using IP Webcam (Android)
1. **Install the app**: Download "IP Webcam" from Google Play Store
2. **Configure the app**:
   - Open IP Webcam
   - Scroll down and tap "Start Server"
   - Note the IP address shown (e.g., `192.168.1.100:8080`)
3. **Add to Sentinel Vision**:
   - Open the dashboard: https://national-hackthon.vercel.app/
   - Go to "Cameras" page
   - Click "Add Camera"
   - Enter details:
     - Name: `Mobile Camera 1`
     - Camera ID: `mobile-cam-1`
     - URL: `http://192.168.1.100:8080/video`
   - Click Save

#### Using DroidCam (Android/iOS)
1. **Install the app**: Download "DroidCam" from app store
2. **Configure the app**:
   - Open DroidCam
   - Start the server
   - Note the IP address (e.g., `192.168.1.100:4747`)
3. **Add to Sentinel Vision**:
   - URL format: `http://192.168.1.100:4747/video`

### Option 2: IP/Network Cameras

#### RTSP Stream (Most IP Cameras)
Common RTSP URL formats:
- Generic: `rtsp://username:password@camera-ip:554/stream1`
- Hikvision: `rtsp://admin:password@192.168.1.64:554/Streaming/Channels/101`
- Dahua: `rtsp://admin:password@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0`
- TP-Link: `rtsp://admin:password@192.168.1.100:554/stream1`
- Reolink: `rtsp://admin:password@192.168.1.100:554/h264Preview_01_main`

Example configuration:
```
Name: Front Door Camera
Camera ID: camera-front
URL: rtsp://admin:password123@192.168.1.64:554/stream1
```

#### HTTP/MJPEG Stream
Some cameras provide HTTP streams:
- Generic: `http://camera-ip/video`
- Axis: `http://camera-ip/mjpg/video.mjpg`
- Example: `http://192.168.1.50/video.cgi`

### Option 3: USB Webcam (Local Only)
For local development/testing:
```python
# In main.py, when adding camera programmatically:
source = 0  # Primary webcam
source = 1  # Secondary USB camera
```

### Option 4: ESP32-CAM or Raspberry Pi Camera

#### ESP32-CAM
1. Flash ESP32-CAM with camera server firmware
2. Common stream URL: `http://192.168.1.150:81/stream`
3. Add to Sentinel Vision with this URL

#### Raspberry Pi Camera
1. Install camera module
2. Use `motion` or `rpicam-vid` to create RTSP stream
3. Example: `rtsp://pi-ip:8554/stream`

---

## 🔧 Adding Cameras via Dashboard

1. **Access Dashboard**: Navigate to https://national-hackthon.vercel.app/
2. **Go to Cameras Page**: Click "Cameras" in the sidebar
3. **Add New Camera**: Click the "Add Camera" button
4. **Fill in Details**:
   ```
   Camera Name: [Descriptive name]
   Camera ID: [unique-id] (use lowercase, no spaces)
   Stream URL: [Your camera stream URL]
   Type: [IP Camera / USB / Mobile]
   Format: [H.264 / MJPEG]
   ```
5. **Save**: Click "Add Camera" button
6. **Verify**: Camera feed should appear in the live view

---

## 🔍 Troubleshooting Camera Connections

### Camera Not Showing Feed
1. **Check network connectivity**:
   - Ensure camera and server are on the same network (for local IPs)
   - For public cameras, ensure firewall allows connections
2. **Verify stream URL**:
   - Test URL in VLC Media Player: `Media > Open Network Stream`
   - If it works in VLC, it should work in Sentinel Vision
3. **Check backend logs**:
   - Visit: https://lokajith.onrender.com/
   - Should show `{"status": "ok", "message": "Sentinel Vision API is running"}`

### "Backend Stream Unavailable" Error
1. **Backend is sleeping** (Render free tier):
   - First request may take 30-60 seconds to wake up
   - Refresh the page after waiting
2. **Check CORS**: Already configured to allow all origins
3. **Network issues**: Check if camera URL is accessible from backend server

### Camera ID Not Found
- Ensure Camera ID matches exactly (case-sensitive)
- Check the `/cameras` endpoint: https://lokajith.onrender.com/cameras

---

## 📊 API Endpoints for IoT Integration

### Check Backend Status
```bash
GET https://lokajith.onrender.com/
```

### List All Cameras
```bash
GET https://lokajith.onrender.com/cameras
```

### Add New Camera
```bash
POST https://lokajith.onrender.com/cameras
Content-Type: application/json

{
  "name": "Security Camera 1",
  "camera_id": "sec-cam-1",
  "url": "rtsp://admin:pass@192.168.1.64:554/stream1",
  "type": "IP Camera",
  "format": "H.264"
}
```

### Get Live Video Feed
```bash
GET https://lokajith.onrender.com/video-feed/{camera_id}
```

### Get Alerts
```bash
GET https://lokajith.onrender.com/alerts
```

### Get Events
```bash
GET https://lokajith.onrender.com/events?limit=50
```

---

## 🔐 Security Considerations

1. **Camera Credentials**: Never expose camera credentials in public repositories
2. **Network Security**: 
   - Use VPN or secure network for camera connections
   - Consider using HTTPS/TLS for camera streams when available
3. **Access Control**: 
   - Currently CORS allows all origins (development mode)
   - For production, restrict CORS to your Vercel domain only

---

## 🚀 Testing the Connection

### Quick Test Steps:
1. **Verify Backend**: Visit https://lokajith.onrender.com/
   - Should return: `{"status": "ok", "message": "Sentinel Vision API is running"}`

2. **Verify Frontend**: Visit https://national-hackthon.vercel.app/
   - Dashboard should load without errors

3. **Add Test Camera**:
   - Use a mobile phone with IP Webcam app
   - Add camera with the mobile IP
   - Check if live feed appears

4. **Test Detection**:
   - Show common objects (person, backpack, etc.)
   - Check alerts panel for detections

---

## 📝 Network Requirements

### For Local Development:
- All devices (cameras, server, client) on same WiFi network
- Firewall allows connections on camera ports

### For Cloud Deployment (Current Setup):
- Backend on Render can access:
  - ✅ Public RTSP/HTTP streams
  - ✅ Cameras with public IPs
  - ❌ Local network cameras (need port forwarding or VPN)

### Solution for Local Cameras:
1. **Port Forwarding**: Configure router to forward camera port to public IP
2. **Use Ngrok/Cloudflare Tunnel**: Create tunnel to local camera
3. **VPN**: Connect backend server to your local network via VPN

---

## 💡 Best Practices

1. **Camera Naming**: Use descriptive names (e.g., "Front Entrance", "Parking Lot")
2. **Camera IDs**: Use lowercase with hyphens (e.g., "front-entrance", "parking-lot")
3. **Stream Quality**: Lower resolution for better performance (720p recommended)
4. **Multiple Cameras**: Add cameras one at a time to verify each connection
5. **Monitoring**: Regularly check the events log for any connection issues

---

## 🆘 Support & Resources

- **API Documentation**: https://lokajith.onrender.com/docs (FastAPI auto-docs)
- **Check System Status**: https://lokajith.onrender.com/stats
- **View Active Cameras**: https://lokajith.onrender.com/cameras

---

## 📦 Environment Variables

### Frontend (.env)
```env
VITE_API_URL=https://lokajith.onrender.com
```

### Backend (Render Environment Variables)
No additional environment variables required for basic setup.
Optional:
```
DATABASE_URL=<your-postgres-url>  # If using PostgreSQL instead of SQLite
```

---

## ✨ Next Steps

1. ✅ Backend deployed and running
2. ✅ Frontend deployed and connected
3. 📱 Add your first IoT camera using the guide above
4. 🔔 Configure detection rules for alerts
5. 📊 Monitor events and analytics on dashboard

Happy monitoring! 🎥🔒
