# ReferKing

**ReferKing** is a simple Flask-based website to showcase refer-and-earn offers, built and hosted on Render.

---

## 🚀 Features

- Display offers from `offers.json`
- Responsive layout using Bootstrap
- Hosted on Render (live link: https://referking-9nsb.onrender.com/)
- Structured project with `app.py`, `static/`, `templates/`, `data/`

---

## 🗂️ Project Structure

```
referking/
├── app.py
├── data/
│   └── offers.json
├── templates/
│   ├── index.html
│   └── about.html
├── static/
│   ├── style.css
│   └── angelone.png, sahil.jpg, etc.
├── requirements.txt
└── render.yaml
```

---

## 🛠️ Technologies Used

- **Backend**: Python + Flask  
- **Frontend**: Bootstrap + custom CSS  
- **Hosting**: Render.com (free static + Flask support)  
- **Source Control**: GitHub (auto-deploy enabled)

---

## 🔧 Setup Instructions

```bash
git clone https://github.com/sahilpinjari1612/referking.git
cd referking
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000` in the browser.

---

## 📦 Deployment

- Live at: https://referking-9nsb.onrender.com/  
- Auto-deploy activated on push to `main` branch via Render  
- Build Command: `pip install -r requirements.txt`  
- Start Command: `python app.py`

---

## 🔮 Future Roadmap

- ✅ Add user login/registration  
- 🔗 Build personalized referral link generator  
- 📊 Add user dashboard and referral tracking  
- 🧩 Expand to admin panel for offers  
- 📱 Launch mobile app (Flutter/React Native)