# 🌿 AgriNova: Smart Farming Assistant

AgriNova is an AI-powered smart farming platform that supports farmers throughout their cultivation journey — from crop recommendation and task scheduling to live pest alerts and an integrated chatbot.

---

## 📁 Project Structure

```
📦 agri-nova/
├── frontend/
│   ├── landing_page.html
│   ├── main.html
│   └── server.js / new_server.js
├── shikhar/  → Chatbot backend
│   └── app.py
├── crop_recommendation/
│   └── crops.py
└── README.md
```

---

## 🚀 How to Run the Project

### 🔸 Step 1: Frontend Setup

1. Open `landing_page.html` in VS Code or any editor.
2. **Change all dataset/API/JS paths** in:
   - `landing_page.html`
   - `main.html`
3. Right-click `landing_page.html` and choose:  
   ▶️ **Open with Live Server**

---

### 🔸 Step 2: Backend Server Setup

1. In the terminal (same directory), run:

```bash
node server.js
```

2. Then, in another terminal tab:

```bash
node new_server.js
```

Make sure Node.js is installed.

---

### 🔸 Step 3: Chatbot Setup (Shikhar Folder)

1. Navigate to the `shikhar` folder:
```bash
cd shikhar
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the chatbot:
```bash
python app.py
```

This will start the AI assistant to answer farmer queries.

---

### 🔸 Step 4: Crop Recommendation Model

1. Navigate to the crop model folder:
```bash
cd crop_recommendation
```

2. Run the model:
```bash
python crops.py
```

This uses available soil, season, and location data to predict the most suitable crop.

---

## ⚠️ Dataset Notice

The original dataset used for this project has been **intentionally removed** due to **government data privacy regulations** related to geolocation-based and agri-intelligence data.

To use the system:
- Prepare your own dataset in the required format.
- Update file paths and data access points in the frontend and model scripts.

---

## 💡 Tech Stack

**Frontend**  
- React.js  
- 3D.js  
- TailwindCSS  
- HTML/CSS/JS with Live Server

**Backend**  
- JavaScript (Node.js for server)  
- Python (Flask or FastAPI for models and chatbot)  
- SQLite (for lightweight local storage)

**Other Tools**  
- Weather APIs  
- Modular rule engines  
- Voice & language support

---

## 🧠 Key Features

- 📆 Smart task scheduling per crop lifecycle
- 🌦️ Weather-integrated pest prediction
- 📊 Live graph updates and inventory tracking
- 🧪 NPK estimation using soil type + crop history
- 🗣️ Voice & regional language input
- 📴 Works offline in rural zones
- 🧠 Crop rotation, multilevel & organic farming tools
- 👨‍🌾 Farmer forums & peer-based knowledge exchange

---

## 👥 Team

**Team Name:** Synapse Squad  
**Project Name:** AgriNova — Revolutionizing Farming Through Intelligence

---

## 📜 License

MIT License — use freely, improve widely, credit always 🙌
