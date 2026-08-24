# 🚀 Deployment Guide

This guide covers how to deploy the AI Data Analyst application on various platforms.

---

## 📋 Prerequisites

- Git
- GitHub account
- A deployment platform account (choose one below)

---

## 1️⃣ Streamlit Cloud (Recommended - Free)

**Advantages:**
- Free tier available
- Easy deployment
- Built for Streamlit apps
- Auto-deploys on git push

**Steps:**

1. Push your code to GitHub
   ```bash
   git add .
   git commit -m "Deploy to Streamlit Cloud"
   git push origin main
   ```

2. Go to [share.streamlit.io](https://share.streamlit.io)

3. Sign in with GitHub

4. Click "New app"
   - Select your repository
   - Select the branch: `main`
   - Select file path: `app.py`

5. Click "Deploy"

✅ Your app will be live in minutes!

---

## 2️⃣ Heroku

**Steps:**

1. Install Heroku CLI

2. Create `Procfile`:
   ```
   web: streamlit run --server.port=$PORT --server.address=0.0.0.0 app.py
   ```

3. Create `runtime.txt`:
   ```
   python-3.11.0
   ```

4. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

---

## 3️⃣ AWS (EC2)

1. Launch EC2 instance
2. SSH into instance
3. Clone repository:
   ```bash
   git clone https://github.com/eswar235/AI_Data_Analyst.git
   cd AI_Data_Analyst
   ```

4. Install Python and dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

5. Run app:
   ```bash
   streamlit run app.py
   ```

---

## 4️⃣ Docker Deployment

Create `Dockerfile`:
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

Build and run:
```bash
docker build -t ai-data-analyst .
docker run -p 8501:8501 ai-data-analyst
```

---

## 📌 Environment Variables

For deployed versions, create `.streamlit/secrets.toml`:
```toml
# Add any sensitive configuration here
```

---

## ✅ Verification

After deployment, verify:
- [ ] App loads without errors
- [ ] File upload works
- [ ] Data cleaning functions
- [ ] Analytics generate correctly
- [ ] Download feature works

---

## 🆘 Troubleshooting

### App not loading?
- Check Python version (3.8+)
- Verify all dependencies installed

### Out of memory?
- Use smaller datasets
- Increase server memory

### Slow performance?
- Optimize data processing
- Use caching

---

## 📞 Support

For deployment issues, refer to:
- [Streamlit Docs](https://docs.streamlit.io/)
- [GitHub Issues](https://github.com/eswar235/AI_Data_Analyst/issues)
