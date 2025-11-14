# 🔐 Phishing Website Detection Using Machine Learning

A Machine Learning–based web application that detects whether a given URL is **Legitimate** or **Phishing** by analyzing 30 URL-based features and using a trained Gradient Boosting Classifier.

---

## 📌 Project Overview

Phishing attacks are one of the most common cyber threats where attackers create fake websites to steal user credentials and personal information.  
This project provides an automated ML-based solution for classifying websites as:

- ✔ Legitimate  
- ⚠ Phishing  

The system uses:

- Feature extraction from URLs  
- Gradient Boosting ML model  
- Flask web app  
- Modern UI for user interaction  

---

---

## 🚀 How the System Works

### 1️⃣ Feature Extraction

The `feature.py` file extracts **30 features** from the input URL, such as:

- URL length  
- Number of dots & hyphens  
- Presence of “@” symbol  
- Use of HTTPS  
- IP address usage  
- Domain age  
- Redirections  
- Suspicious keyword patterns  

---

### 2️⃣ Machine Learning Model

The `train_model.py` script trains a **Gradient Boosting Classifier**.

Training steps:

1. Load dataset (`phishing.csv`)  
2. Split into training/testing sets  
3. Train GBC model  
4. Save trained model as `model.pkl`  

Model accuracy typically ranges between **93%–97%** depending on dataset.

---

### 3️⃣ Web Application (Flask)

The `app.py` script runs a Flask web interface where users can:

- Enter a URL  
- Run ML-based classification  
- View the result:

**✔ Legitimate Website**  
or  
**⚠ Phishing Website Detected**  

![Screenshot 1](https://github.com/user-attachments/assets/691d5090-a6a3-49dd-a8b5-ff382b9a0a71)

![Screenshot 2](https://github.com/user-attachments/assets/cd57808a-2315-4a09-988e-e761e999bfb9)

![Screenshot 3](https://github.com/user-attachments/assets/bedea758-d221-4a2f-8541-4de52c2b82b0)

---

## 🧪 How to Run the Project

### Install Dependencies

```bash
pip install flask numpy pandas scikit-learn
or
conda install flask numpy pandas scikit-learn

RUN
python app.py

## 🎨 User Interface

The UI includes:

- Clean modern design  
- Gradient background  
- Rounded card UI  
- Green (safe) / Red (phishing) indicators  
- Responsive layout  

---

## 📊 Model Details

- **Algorithm:** Gradient Boosting Classifier  
- **Features:** 30 URL + domain features  
- **Labels:**  
  - `1` → Legitimate  
  - `-1` → Phishing  

---

## 📁 Dataset Source

As described in the project report:

- Kaggle phishing URL datasets  
- UCI Phishing Website Dataset  
- Additional manually collected phishing URLs  

Combined into: **phishing.csv**

---

## 👨‍💻 Team Members

- Tejaswini Nethala  
- Pranathi Gudipally  
- Shafiya Masrath  
- Divya Rapelli  
- Akhila Rayabarapu  

---

## 💡 Future Enhancements

- Deep Learning models (CNN/LSTM)  
- Browser extension for real-time detection  
- WHOIS verification integration  
- Screenshot-based phishing recognition  
- Deployment on AWS/GCP  

---

## 📜 License

This project was developed as part of the **MDS Laboratory Course**.  
Unauthorized commercial use is not permitted.




