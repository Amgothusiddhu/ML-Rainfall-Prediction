# 🌧️ Rainfall Prediction Web App

A modern and interactive **Rainfall Prediction Web Application** built using Flask and deployed on AWS EC2.

---

## 🚀 Features

* 🌡️ Input weather parameters (Temperature, Humidity, Wind Speed)
* 🌧️ Predict rainfall amount in **centimeters (cm)**
* 📊 Smart classification:

  * ☀️ No Rain
  * 🌦️ Light Rain
  * 🌧️ Moderate Rain
  * ⛈️ Heavy Rain
  * 🌪️ Very Heavy Rain
* 🎨 Beautiful and responsive UI (Bootstrap)
* ☁️ Deployable on cloud (AWS EC2)

---

## 🧠 How It Works

```text
Rainfall (cm) = (Temperature + Humidity + Wind Speed) / 10
```

### 📊 Classification

| Rainfall (cm) | Type                |
| ------------- | ------------------- |
| < 1           | ☀️ No Rain          |
| 1 – 3         | 🌦️ Light Rain      |
| 3 – 6         | 🌧️ Moderate Rain   |
| 6 – 10        | ⛈️ Heavy Rain       |
| > 10          | 🌪️ Very Heavy Rain |

---

## 🖥️ Example

```text
Input:
10, 20, 30

Output:
🌧️ Rainfall: 6.0 cm → ⛈️ Heavy Rain
```

---

## ⚙️ Installation & Setup (Local / EC2)

### 1️⃣ Update System & Install Dependencies

```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git -y
```

---

### 2️⃣ Clone Repository

```bash
git clone https://github.com/Amgothusiddhu/ML-Rainfall-Prediction.git
cd ML-Rainfall-Prediction
```

---

### 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Required Packages

⚠️ If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

👉 If NOT (first-time setup):

```bash
pip install flask numpy pandas scikit-learn
```

---

### 5️⃣ Run Application

```bash
python app.py
```

---

## 🌐 Access the Application

* Local:

```
http://localhost:5000
```

* EC2:

```
http://<your-ec2-ip>:5000
```

---

## ☁️ Deployment on AWS EC2

1. Launch Ubuntu EC2 instance
2. Allow ports:

   * 22 (SSH)
   * 5000 (App)
3. Connect via SSH
4. Run setup commands
5. Start application

---

## 📁 Project Structure

```
ML-Rainfall-Prediction/
│── app.py
│── templates/
│    └── index.html
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🔮 Future Improvements

* 🤖 Integrate real Machine Learning model (.pkl)
* 🌦️ Live weather API integration
* 📊 Graphs and data visualization
* 🔐 Deploy with domain & HTTPS

---

## 👨‍💻 Author

GitHub: https://github.com/Amgothusiddhu


