# AndroCSI - Wi-Fi Signal Intelligence & Activity Analysis System (CSI-SENSOR)
<p align="center">
  <img src="assets/1.png" alt="Banner 1" width="100%">
</p>

<div align="center">

<img src="https://img.shields.io/badge/AndroCSI-WiFi%20Signal%20Intelligence-00dfff?style=for-the-badge&logo=wifi&logoColor=white">

<img src="https://img.shields.io/badge/Author-SYLHETYHACKVENGER%20(THE--ERROR808)-06131a?style=for-the-badge&logo=github&logoColor=00dfff">

<br>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">

<img src="https://img.shields.io/badge/Platform-Android%20%7C%20Termux-3DDC84?style=for-the-badge&logo=android&logoColor=white">

<img src="https://img.shields.io/badge/UI-Cinematic%20HUD-00dfff?style=for-the-badge&logo=webcomponents.org&logoColor=white">

<br>

<img src="https://img.shields.io/badge/Network-Wi--Fi%20Analysis-ff6b00?style=for-the-badge&logo=wireless&logoColor=white">

<img src="https://img.shields.io/badge/Architecture-Threaded%20Engine-8A2BE2?style=for-the-badge&logo=serverless&logoColor=white">

<img src="https://img.shields.io/badge/Status-ONLINE-00ff88?style=for-the-badge">

</div>

<div align="center">

[![AndroCSI](https://img.shields.io/badge/ANDROCSI-CYBER%20SENSOR%20INTELLIGENCE-00dfff?style=for-the-badge)]()

[![Signal](https://img.shields.io/badge/SIGNAL%20PROCESSING-REALTIME-00ff99?style=for-the-badge)]()

[![Radar](https://img.shields.io/badge/RADAR%20HUD-ACTIVE-0088ff?style=for-the-badge)]()

[![Sensor](https://img.shields.io/badge/SENSOR%20FUSION-ENABLED-ffcc00?style=for-the-badge)]()

[![License](https://img.shields.io/badge/PROJECT-GRAY%20HAT%20RESEARCH-ff0055?style=for-the-badge)]()

</div>

🚀 Overview

AndroCSI is a professional-grade Wi-Fi signal intelligence and activity analysis system designed for Android devices running Termux. It transforms your mobile device into a sophisticated signal monitoring and activity recognition platform by analyzing Wi-Fi signal fluctuations, device sensor data, and environmental patterns to detect and classify human activities and anomalies.

⚠️ Important Note: AndroCSI is a heuristic-based signal analysis system. It provides intelligent interpretations of Wi-Fi signal variations and environmental patterns, but does NOT utilize actual Channel State Information (CSI) hardware. Real CSI-based recognition requires specialized hardware and drivers.

🎯 Key Capabilities

· Real-time Signal Intelligence - Continuous monitoring and analysis of Wi-Fi signal patterns
· Activity Classification - Heuristic-based detection of walking, sitting, fast walking, and potential falls
· Environmental Mapping - Visual representation of Wi-Fi network distribution and signal strength
· Sensor Integration - Utilizes device sensors and battery data for enhanced context awareness
· Interactive Dashboard - Professional web interface with live visualization and controls
· Data Export - JSON snapshot export for offline analysis and research
· Audio Sonification - Convert Wi-Fi signal strength to auditory feedback
· Microphone Integration - Optional acoustic activity detection via device microphone

📊 Activity Classification Engine

The system employs sophisticated signal analysis algorithms to classify environmental states:

Classification Signal Pattern Confidence Score Description
POSSIBLE FALL Peak ≥ 9, Volatility ≥ 4, Spread < 4 95% Abrupt signal pattern indicating potential fall
IMPACT EVENT Peak ≥ 9, Volatility ≥ 4 88% Significant signal disturbance event
STILL / SITTING-LIKE Mean Deviation < 1, Volatility < 2 12% Stable environment with minimal signal variation
LOW ACTIVITY Mean Deviation < 2.3 30% Subtle environmental changes
WALKING-LIKE Mean Deviation < 4.3 58% Moderate signal fluctuation pattern
FAST WALKING-LIKE Mean Deviation ≥ 4.3 82% High signal variation indicative of fast movement

🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AndroCSI System Architecture            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │
│  │   Wi-Fi     │    │  Sensors    │    │ Microphone  │    │
│  │   Scanner   │    │  (Termux)   │    │   (Optional)│    │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘    │
│         │                  │                  │             │
│         └─────────┬────────┴─────────┬────────┘             │
│                   │                  │                      │
│           ┌───────▼───────┐  ┌───────▼───────┐             │
│           │  Signal      │  │  Activity     │             │
│           │  Processing  │  │  Detection    │             │
│           │  Engine      │  │  Engine       │             │
│           └───────┬───────┘  └───────┬───────┘             │
│                   │                  │                      │
│           ┌───────▼──────────────────▼───────┐             │
│           │         Data Aggregation         │             │
│           │         & Analytics Core         │             │
│           └────────┬───────────┬─────────────┘             │
│                    │           │                            │
│         ┌──────────▼───┐   ┌──▼──────────┐                │
│         │  Web Server  │   │  JSON API   │                │
│         │   (HTTP)     │   │  Endpoints  │                │
│         └──────────┬───┘   └──┬──────────┘                │
│                    │           │                            │
│         ┌──────────▼───────────▼──────────┐                │
│         │    Web-Based Dashboard (UI)     │                │
│         │  - Live Visualization          │                │
│         │  - Real-time Controls          │                │
│         │  - Activity Radar              │                │
│         │  - Event Timeline              │                │
│         └─────────────────────────────────┘                │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

🛠️ Installation & Setup

Prerequisites

· Android device with Termux installed
· Python 3.7 or higher
· Termux API packages installed

Quick Start

```bash
# 1. Install required packages
pkg update && pkg upgrade
pkg install python python-pip termux-api

# 2. Clone the repository
git clone https://github.com/sylhetyhackvenger/AndroCSI
cd AndroCSI 

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Grant necessary permissions
termux-setup-storage
# Grant Wi-Fi scanning and sensor permissions when prompted

# 5. Run AndroCSI
python androcsi.py
```

Required Permissions

The system requires the following Android permissions:

· Wi-Fi scanning
· Location services (for Wi-Fi scanning)
· Sensor access
· Storage access (for data export)
· Microphone (optional, for acoustic analysis)

📱 Web Dashboard Features

1. Command Center (Dashboard)

· Real-time signal metrics display
· Rolling average and volatility tracking
· Activity classification with confidence scores
· Live signal visualization graph

2. Activity Radar

· Visual representation of signal environment
· Animated sweep radar display
· Network radio position mapping
· Activity classification status

3. Network Environment

· Comprehensive list of discovered Wi-Fi networks
· Signal strength (RSSI) metrics
· Frequency and security information
· Estimated range calculations

4. Signal Analysis

· Signal matrix visualization
· Variance and volatility tracking
· Scan count monitoring
· Source identification

5. Waterfall Display

· Historical signal strength visualization
· Time-based signal pattern recognition
· Visual signal density mapping

6. Audio Integration

· Wi-Fi Sonification: Convert signal strength to audio frequency (120-1020 Hz)
· Microphone Analysis: Optional acoustic activity detection
· Real-time waveform visualization

7. Sensors & System

· Complete device sensor data display
· Battery status monitoring
· System uptime tracking
· JSON data export capability

🔧 Technical Specifications

Core Components

Component Technology Description
Backend Python 3.7+ Threaded HTTP server with signal processing
Frontend HTML5, CSS3, Vanilla JS Responsive, mobile-first interface
Data Storage In-memory deque Real-time data with configurable history limits
API Protocol HTTP REST JSON-based state transmission
Wi-Fi Scanning Termux API termux-wifi-scaninfo integration
Sensors Termux API termux-sensor and termux-battery-status

Data Structures

```python
# Main State Object
S = {
    "name": "AndroCSI",
    "author": "SYLHETYHACKVENGER (THE-ERROR808)",
    "boot": time.time(),
    "status": "ONLINE",
    "signal": -75,          # Current RSSI in dBm
    "average": -75,         # Rolling average
    "variance": 0.0,        # Signal variance
    "volatility": 0.0,      # Standard deviation
    "activity": "CALIBRATING",
    "activity_score": 0,
    "networks": [],         # Discovered Wi-Fi networks
    "history": deque(maxlen=360),           # Signal history
    "activity_history": deque(maxlen=360),  # Activity scores
    "events": deque(maxlen=150),            # System events
    "scan_count": 0,
    "source": "INITIALIZING",
    "csi": "CSI INPUT NOT CONNECTED",
    "sensors": {},
    "battery": {}
}
```

📊 Performance Metrics

Signal Analysis Parameters

· History Window: 360 samples (~6 minutes at 1s intervals)
· Activity Window: 32 samples (~32 seconds)
· Event Log: 150 most recent events
· Update Frequency: 1 second
· Network Scan Frequency: Real-time with fallback simulation

Classification Thresholds

Metric Formula Range
Signal Range R(dBm) = 10^((-50 - dBm)/22) 0.5 - 999 meters
Volatility σ = √(Σ(x-μ)²/n) 0 - ∞
Mean Deviation MD = Σ a[i]-a[i-1]
Peak Detection max( d
Spread max(recent) - min(recent) 0 - ∞

🔒 Security Considerations

· Network Exposure: HTTP server bound to localhost only (127.0.0.1)
· Data Privacy: All processing occurs locally on the device
· No External Communication: System operates entirely offline
· Limited API Exposure: Only /api/state endpoint available
· Permission Management: Requires explicit user permissions via Termux

🚨 Use Cases & Applications

Security & Surveillance

· Intrusion Detection: Detect unauthorized presence via Wi-Fi signal disturbances
· Perimeter Monitoring: Track movement patterns in Wi-Fi environments
· Anomaly Detection: Identify unusual signal patterns in protected areas

Healthcare & Wellness

· Fall Detection: Heuristic detection of potential falls (experimental)
· Activity Monitoring: Track walking patterns and activity levels
· Remote Care: Non-invasive activity monitoring for elderly care

Research & Development

· Signal Propagation Studies: Analyze Wi-Fi behavior in various environments
· IoT Integration: Foundation for more sophisticated CSI-based applications
· Machine Learning: Data collection and labeling for future AI models

Personal Use

· Home Automation: Trigger automations based on activity detection
· Safety Monitoring: Keep track of home occupants
· Security Awareness: Visualize Wi-Fi environment for better security posture

🤝 Contributing

We welcome contributions to improve AndroCSI!

Contribution Guidelines

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

Areas for Contribution

· Enhanced activity classification algorithms
· Additional sensor integration
· Performance optimizations
· UI/UX improvements
· Documentation and examples
· Bug fixes and stability improvements

📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments

· Termux Team for providing the amazing Android terminal environment
· Wi-Fi and Signal Processing Community for foundational research
· Open Source Community for tools and libraries used in this project

📞 Support & Contact

Author: SYLHETYHACKVENGER (THE-ERROR808)

🎓 Educational Value

AndroCSI serves as an excellent educational tool for:

· Understanding Wi-Fi signal behavior
· Learning signal processing techniques
· Exploring Android API capabilities via Termux
· Building real-time web interfaces
· Understanding activity classification algorithms

---

<p align="center">
  <strong>Made with ❤️ by SYLHETYHACKVENGER (THE-ERROR808)</strong><br>
  <em>"Transforming Wi-Fi signals into intelligence"</em>
</p>
