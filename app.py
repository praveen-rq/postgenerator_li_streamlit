import streamlit as st
import datetime
from post_generator import PostGenerator

# Set page config
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📝",
    layout="wide"
)

# Main title
st.title("📝 LinkedIn Post Generator")
st.subheader("AI-Powered Professional Content Creation")

# Initialize post generator
@st.cache_resource
def get_post_generator():
    try:
        return PostGenerator()
    except Exception as e:
        st.error(f"❌ Error initializing post generator: {e}")
        st.info("💡 Make sure your .env file contains: GEMINI_API_KEY=your_api_key")
        return None

generator = get_post_generator()

# Sidebar for user prompt editing
st.sidebar.title("🎯 Content Settings")

# User prompt editing
st.sidebar.write("### ✍️ User Prompt")
st.sidebar.write("*Edit this to change what kind of post gets generated*")

# Load default user prompt
def load_user_prompt():
    try:
        with open('prompts/user_prompt.txt', 'r', encoding='utf-8') as file:
            return file.read().strip()
    except:
        return "Create a LinkedIn post about a trending technology topic with expert insights and real-world examples."

# Initialize session state for user prompt
if 'user_prompt' not in st.session_state:
    st.session_state.user_prompt = load_user_prompt()

# User prompt text area in sidebar
user_prompt = st.sidebar.text_area(
    "Your prompt:",
    value=st.session_state.user_prompt,
    height=200,
    help="Describe what kind of LinkedIn post you want to generate"
)

# Update session state when user edits
if user_prompt != st.session_state.user_prompt:
    st.session_state.user_prompt = user_prompt

# Save prompt button
if st.sidebar.button("💾 Save Prompt", use_container_width=True):
    try:
        with open('prompts/user_prompt.txt', 'w', encoding='utf-8') as file:
            file.write(user_prompt)
        st.sidebar.success("✅ Prompt saved!")
    except Exception as e:
        st.sidebar.error(f"❌ Error saving: {e}")

# Reset to default button
if st.sidebar.button("🔄 Reset to Default", use_container_width=True):
    default_prompt = """Create a LinkedIn post about a trending technology topic that includes:

1. A specific trending aspect or recent development
2. Your expert perspective on why this matters
3. A real-world use case or example from your experience
4. Key insights or lessons learned
5. An engaging question or call-to-action for the audience

Focus on topics like:
- Artificial Intelligence and Machine Learning
- Remote work and productivity
- Digital transformation
- Cybersecurity trends
- Cloud computing developments
- Data analytics and insights
- Software development best practices
- Tech industry career advice

Make it personal, insightful, and valuable for a professional audience."""
    
    st.session_state.user_prompt = default_prompt
    st.rerun()

# Main content area
current_date = datetime.datetime.now().strftime('%Y-%m-%d')
st.info(f"📅 Generating content for: {current_date}")

# Initialize session state for post content
if 'current_post_data' not in st.session_state:
    st.session_state.current_post_data = None

if 'linkedin_post_content' not in st.session_state:
    st.session_state.linkedin_post_content = ""

# Generate new post button
if st.button("🔄 Generate New Post", type="secondary", use_container_width=True):
    if generator:
        with st.spinner("🤖 Generating LinkedIn post..."):
            try:
                # Load system prompt
                try:
                    with open('prompts/system_prompt.txt', 'r', encoding='utf-8') as file:
                        system_prompt = file.read().strip()
                except:
                    system_prompt = None
                
                post_data = generator.generate_linkedin_post(
                    selected_date=current_date,
                    system_prompt=system_prompt,
                    user_prompt=user_prompt
                )
                st.session_state.current_post_data = post_data
                st.session_state.linkedin_post_content = post_data['content']
                st.rerun()
            except Exception as e:
                st.error(f"❌ Error generating post: {e}")
    else:
        st.warning("⚠️ Post generator not available. Please check your API configuration.")

# Show post metadata if available
if st.session_state.current_post_data:
    post_data = st.session_state.current_post_data
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("📊 Word Count", post_data['word_count'])
    with col2:
        st.metric("📝 Character Count", post_data['char_count'])
    with col3:
        st.metric("⏰ Generated", post_data['generated_at'][:16])

# Large text area for LinkedIn post
initial_value = st.session_state.get('linkedin_post_content', '')
linkedin_post = st.text_area(
    "Your LinkedIn Post:",
    value=initial_value,
    placeholder="Click 'Generate New Post' to create content, or write your own post here...",
    height=300,
    key="linkedin_post_input"
)

# Update session state when user edits
if linkedin_post != st.session_state.get('linkedin_post_content', ''):
    st.session_state.linkedin_post_content = linkedin_post

st.write("")  # Add some spacing

# Action buttons
button_col1, button_col2, button_col3 = st.columns([1, 1, 2])

with button_col1:
    if st.button("✅ Post", type="primary", use_container_width=True):
        if linkedin_post.strip():
            st.success("🎉 Post scheduled successfully!")
            st.balloons()
        else:
            st.warning("⚠️ Please add some content to post!")

with button_col2:
    if st.button("❌ Discard", use_container_width=True):
        st.info("📝 Post discarded. Generate a new one!")
        st.session_state.linkedin_post_content = ""
        st.session_state.current_post_data = None
        st.rerun()

with button_col3:
    if st.button("📋 Multiple Options", use_container_width=True):
        if generator:
            with st.spinner("🎯 Generating multiple post options..."):
                try:
                    # Load system prompt
                    try:
                        with open('prompts/system_prompt.txt', 'r', encoding='utf-8') as file:
                            system_prompt = file.read().strip()
                    except:
                        system_prompt = None
                    
                    posts = generator.generate_multiple_options(
                        3, current_date, system_prompt, user_prompt
                    )
                    st.session_state.post_options = posts
                    st.info("✨ Multiple options generated! Check below.")
                except Exception as e:
                    st.error(f"❌ Error generating options: {e}")
        else:
            st.warning("⚠️ Post generator not available.")

# Show character count
if linkedin_post:
    char_count = len(linkedin_post)
    st.caption(f"Character count: {char_count}/3000")
    
    if char_count > 3000:
        st.error("⚠️ Post is too long! LinkedIn posts should be under 3000 characters.")

# Multiple options section
if 'post_options' in st.session_state and st.session_state.post_options:
    st.write("---")
    st.write("### 🎯 Multiple Post Options")
    st.write("Choose from these generated options:")
    
    for i, option in enumerate(st.session_state.post_options):
        with st.expander(f"Option {i+1}: {option['content'][:50]}..."):
            st.write(option['content'])
            col1, col2, col3 = st.columns(3)
            with col1:
                st.caption(f"Words: {option['word_count']}")
            with col2:
                st.caption(f"Characters: {option['char_count']}")
            with col3:
                if st.button(f"Use Option {i+1}", key=f"use_option_{i}"):
                    st.session_state.linkedin_post_content = option['content']
                    st.session_state.current_post_data = option
                    st.success(f"✅ Selected Option {i+1}!")
                    st.rerun()

# Preview section
if linkedin_post.strip():
    st.write("---")
    st.write("### 👀 Preview")
    with st.container():
        st.markdown(f"""
        <div style="
            border: 1px solid #ddd; 
            border-radius: 10px; 
            padding: 20px; 
            margin: 10px 0; 
            background-color: #f9f9f9;
        ">
            <strong>Your Name</strong><br>
            <small>Just now • 🌍</small><br><br>
            {linkedin_post.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit & Google Gemini AI") 