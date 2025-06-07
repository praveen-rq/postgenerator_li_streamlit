# 📝 LinkedIn Post Generator

An intelligent LinkedIn post generator powered by Google's Gemini AI, built with Streamlit.

## ✨ Features

- **AI-Powered Content Generation**: Uses Google Gemini AI to create authentic, professional LinkedIn posts
- **Trending Topics**: Automatically selects from a curated list of trending technology topics
- **Real-World Examples**: Includes expert insights and practical use cases
- **Multiple Options**: Generate multiple post variations to choose from
- **Date-Based Organization**: Manage posts by specific dates with an intuitive calendar interface
- **Character Count Validation**: Ensures posts meet LinkedIn's character limits
- **Live Preview**: See how your post will look on LinkedIn before publishing

## 🚀 Quick Start

### 1. Prerequisites
- Python 3.11 or higher
- Google Gemini API key

### 2. Installation

```bash
# Clone or download the project
git clone <your-repo-url>
cd postgenerator_li_streamlit

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Setup API Key

#### Option 1: Environment File (.env)
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

#### Option 2: Configuration File
1. Copy `config_template.py` to `config.py`
2. Edit `config.py` and replace the placeholder with your actual API key

### 4. Get Your Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the generated key

### 5. Run the Application

```bash
# Make sure virtual environment is activated
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## 🎯 How to Use

### Generate a New Post
1. **Select Date**: Choose a month and date from the sidebar
2. **Generate Content**: Click "🔄 Generate New Post" 
3. **Review**: Check the generated post, topic, and word count
4. **Edit**: Modify the content if needed
5. **Preview**: See how it will look on LinkedIn
6. **Publish**: Click "✅ Post" when satisfied

### Multiple Options
- Click "📋 Multiple Options" to generate 3 different post variations
- Compare different approaches and topics
- Select the best option with one click

### Post Management
- Browse previous posts by date in the sidebar
- Each date shows post status: ✅ Posted, ❌ Skipped, or 📝 Draft
- Click on any date to work on that specific post

## 🔧 Configuration

### Topics Customization
Edit `post_generator.py` to customize the trending topics list:

```python
self.trending_topics = [
    "Your custom topic 1",
    "Your custom topic 2",
    # Add more topics...
]
```

### Post Template
Modify the prompt in `post_generator.py` to change the style and structure of generated posts.

## 📁 Project Structure

```
postgenerator_li_streamlit/
├── app.py                  # Main Streamlit application
├── post_generator.py       # AI post generation logic
├── config_template.py      # Configuration template
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── venv/                  # Virtual environment
```

## 🛠️ Dependencies

- **streamlit**: Web application framework
- **google-generativeai**: Google Gemini AI SDK
- **python-dotenv**: Environment variable management
- **pandas**: Data manipulation
- **numpy**: Numerical operations

## 🔍 Troubleshooting

### Common Issues

**"GEMINI_API_KEY not found"**
- Ensure your `.env` file exists and contains the correct API key
- Check that the key is valid and active

**"No module named streamlit"**
- Make sure the virtual environment is activated
- Run `pip install -r requirements.txt`

**Post generation fails**
- Verify your internet connection
- Check API key validity
- The app includes fallback content if API calls fail

### Getting Help

1. Check the console for detailed error messages
2. Verify all requirements are installed correctly
3. Ensure your Gemini API key is valid and has sufficient quota

## 🎨 Features Overview

### Smart Content Generation
- Picks trending topics relevant to your industry
- Adds expert perspective and insights
- Includes real-world use cases and examples
- Maintains authentic, non-AI-like tone

### User-Friendly Interface
- Clean, professional design
- Intuitive navigation and controls
- Real-time feedback and validation
- Mobile-responsive layout

### Content Management
- Date-based post organization
- Multiple post options for each date
- Easy content editing and refinement
- Visual preview before posting

## 🚀 Next Steps

- Add database integration for post storage
- Implement user authentication
- Add scheduling functionality
- Include analytics and performance tracking
- Support for multiple social platforms

---

Built with ❤️ using Streamlit and Google Gemini AI 