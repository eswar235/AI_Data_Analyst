# 🧪 Usability & Testing Guide

This guide helps you test and verify the AI Data Analyst application works correctly.

---

## 🌐 Live Application Links

### Streamlit Cloud Deployment
**Status:** Check the deployment link below
- **URL:** https://share.streamlit.io/eswar235/AI_Data_Analyst/main/app.py

**Note:** If the app isn't deployed yet on Streamlit Cloud, follow the deployment steps below.

---

## 🚀 Local Testing (Your Machine)

### Run Locally
```powershell
cd AI_Data_Analyst_Original
python -m pip install -r requirements.txt
streamlit run app.py
```

**Access:** http://localhost:8501

---

## ✅ Testing Checklist

### 1. **Basic Functionality**
- [ ] App loads without errors
- [ ] Upload button appears
- [ ] Can select CSV/Excel file

### 2. **Data Upload & Loading**
- [ ] Can upload CSV file
- [ ] Can upload Excel file
- [ ] Success message appears
- [ ] Dataset overview shows metrics

### 3. **Data Cleaning**
- [ ] "Clean Dataset" button works
- [ ] Shows cleaning statistics
- [ ] Download cleaned CSV button appears
- [ ] Can download cleaned data

### 4. **Data Analysis**
- [ ] Statistical analysis displays
- [ ] Visualizations render (histograms, scatter plots)
- [ ] Categorical analysis works
- [ ] Date analysis works (if date columns present)

### 5. **AI Features**
- [ ] "Generate Business Insights" button works
- [ ] Insights text generates without errors
- [ ] AI Analyst question input accepts text
- [ ] AI provides responses to questions

### 6. **Performance**
- [ ] App responds quickly (< 5 seconds per action)
- [ ] Handles medium datasets (1000+ rows)
- [ ] No memory errors
- [ ] Smooth interactions

---

## 📊 Test Data

### Sample Files to Test With

**Option 1: Use Built-in Sample**
- The app may have a sample dataset ready
- Look for sample files in `data/` folder

**Option 2: Create Test CSV**
Create a file called `test_data.csv`:
```csv
Date,Product,Sales,Profit,Region
2024-01-01,A,1000,200,East
2024-01-02,B,1500,300,West
2024-01-03,A,1200,250,East
2024-01-04,C,800,100,North
2024-01-05,B,2000,400,South
2024-01-06,A,1100,220,East
2024-01-07,C,900,150,North
2024-01-08,B,1800,360,West
```

**Option 3: Download Test Dataset**
- Download from Kaggle: https://www.kaggle.com/datasets
- Use any CSV with 5+ columns and 100+ rows

---

## 🐛 Troubleshooting Issues

### Issue: "ModuleNotFoundError: No module named 'plotly'"
**Solution:**
```powershell
pip install plotly
```

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
```powershell
pip install -r requirements.txt
```

### Issue: App crashes when uploading file
**Check:**
1. File is CSV or Excel
2. File is not corrupted
3. File has at least 2 columns
4. Try with smaller file first

### Issue: Visualizations not showing
**Check:**
1. Data has numeric columns
2. Data has categorical columns
3. Browser cache cleared (Ctrl+Shift+Delete)
4. Try refreshing app (F5)

### Issue: AI features not working
**Check:**
1. Internet connection active
2. No API key errors (should work without key now)
3. Check browser console for errors (F12)

---

## 📱 Browser Compatibility

**Tested On:**
- ✅ Chrome (latest)
- ✅ Firefox (latest)
- ✅ Edge (latest)
- ✅ Safari (latest)

**Mobile:**
- ✅ Works on iPad/Tablet
- ⚠️ Works on mobile (small screen, better on desktop)

---

## 🔍 Performance Metrics

**Expected Performance:**
- App load time: < 3 seconds
- File upload: < 2 seconds
- Data cleaning: < 5 seconds
- Visualization render: < 2 seconds
- Business insights: < 10 seconds
- AI question response: < 5 seconds

**Dataset Size Limits:**
- Recommended: 100 - 100,000 rows
- Maximum: 1,000,000 rows (may be slow)
- Minimum: 10 rows (for meaningful analysis)

---

## 📋 Feature Testing Matrix

| Feature | Status | Notes |
|---------|--------|-------|
| CSV Upload | ✅ | Works with UTF-8 encoding |
| Excel Upload | ✅ | .xlsx format supported |
| Data Cleaning | ✅ | Removes nulls, duplicates |
| Statistics | ✅ | Mean, median, std, min, max |
| Visualizations | ✅ | Histograms, scatter, bar charts |
| Date Analysis | ✅ | If date columns detected |
| Category Analysis | ✅ | Distribution and breakdown |
| Business Insights | ✅ | Pattern-based analysis |
| AI Questions | ✅ | Smart question answering |
| Download Data | ✅ | CSV export works |

---

## 🎯 User Journey Test

**Follow this path to fully test the app:**

1. **Start:**
   - Open app at http://localhost:8501
   - See welcome screen ✅

2. **Upload:**
   - Click "Upload Your Dataset"
   - Select test CSV file
   - Verify success message ✅

3. **Overview:**
   - See dataset metrics (rows, columns)
   - Verify numbers are correct ✅

4. **Quality Check:**
   - See data quality metrics
   - Check missing values count
   - Check duplicate rows count ✅

5. **Clean:**
   - Click "Clean Dataset"
   - Verify cleaning statistics
   - Download cleaned CSV ✅

6. **Analysis:**
   - See statistical summary
   - View visualizations
   - Interact with charts ✅

7. **Insights:**
   - Click "Generate Business Insights"
   - Read AI-generated insights
   - Verify they match data ✅

8. **Q&A:**
   - Type question in "Ask the AI Analyst"
   - Get response
   - Verify answer is relevant ✅

9. **Done:**
   - All features working ✅

---

## 📞 Support & Reporting Issues

### Report Issues
- GitHub Issues: https://github.com/eswar235/AI_Data_Analyst/issues
- Email: eswarbethamsetty235@gmail.com

### Include in Report:
- What you were doing when error occurred
- Error message (exact text)
- Your operating system (Windows/Mac/Linux)
- Browser used
- Sample data or file used

---

## ✅ Sign-Off

When all tests pass, the app is ready for:
- ✅ Production use
- ✅ Sharing with others
- ✅ Portfolio showcase
- ✅ Public deployment

---

**Happy Testing! 🚀**
