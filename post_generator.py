import google.generativeai as genai
import os
import random
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class PostGenerator:
    def __init__(self):
        """Initialize the PostGenerator with Gemini API"""
        # Load environment variables from .env file
        load_dotenv()
        
        # Load API key from .env file
        self.api_key = os.getenv('GEMINI_API_KEY')
        
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found. Please create a .env file with: GEMINI_API_KEY=your_api_key")
        
        # Configure Gemini
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('gemini-1.5-flash')
    
    def load_prompt_from_file(self, filepath):
        """Load prompt content from a text file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read().strip()
        except FileNotFoundError:
            return None
        except Exception as e:
            print(f"Error reading prompt file {filepath}: {e}")
            return None
    
    def generate_linkedin_post(self, selected_date=None, system_prompt=None, user_prompt=None):
        """
        Generate a complete LinkedIn post using Gemini API
        
        Args:
            selected_date (str): Date for the post (format: YYYY-MM-DD)
            system_prompt (str): System instructions for the AI
            user_prompt (str): User's specific content request
            
        Returns:
            dict: Contains the generated post and metadata
        """
        if not selected_date:
            selected_date = datetime.now().strftime('%Y-%m-%d')
        
        # Load prompts from files if not provided
        if not system_prompt:
            system_prompt = self.load_prompt_from_file('prompts/system_prompt.txt')
            if not system_prompt:
                system_prompt = "You are a professional LinkedIn content creator. Create engaging, authentic posts."
        
        if not user_prompt:
            user_prompt = self.load_prompt_from_file('prompts/user_prompt.txt')
            if not user_prompt:
                user_prompt = "Create a LinkedIn post about a trending technology topic with expert insights and real-world examples."
        
        # Combine system and user prompts
        full_prompt = f"{system_prompt}\n\nUser Request: {user_prompt}\n\nToday's Date: {selected_date}"
        
        try:
            # Generate the post using Gemini
            response = self.model.generate_content(full_prompt)
            generated_post = response.text.strip()
            
            # Create metadata
            post_data = {
                'content': generated_post,
                'system_prompt': system_prompt,
                'user_prompt': user_prompt,
                'date': selected_date,
                'generated_at': datetime.now().isoformat(),
                'word_count': len(generated_post.split()),
                'char_count': len(generated_post)
            }
            
            return post_data
            
        except Exception as e:
            # Fallback content if API fails
            fallback_post = self._create_fallback_post(user_prompt, selected_date)
            return fallback_post
    
    def _create_fallback_post(self, user_prompt, date):
        """Create a fallback post if API fails"""
        fallback_content = f"""🔍 Today I was reflecting on current technology trends and their growing impact on our industry.

After working with several teams implementing new solutions, I've noticed one key pattern: the organizations that succeed aren't just adopting the latest technology—they're reimagining their entire workflow around it.

Here's what I learned from a recent project:
A mid-sized company increased their efficiency by 40% not because they had the most advanced tools, but because they took time to train their team properly and integrated the technology thoughtfully into their existing processes.

The takeaway? Technology is an enabler, not a magic solution. The real value comes from strategic implementation and people-first adoption.

What's been your experience with digital transformation in your organization? I'd love to hear your thoughts!

#TechTrends #Innovation #DigitalTransformation"""

        return {
            'content': fallback_content,
            'user_prompt': user_prompt,
            'system_prompt': 'Fallback system prompt',
            'date': date,
            'generated_at': datetime.now().isoformat(),
            'word_count': len(fallback_content.split()),
            'char_count': len(fallback_content),
            'is_fallback': True
        }
    
    def generate_multiple_options(self, count=3, selected_date=None, system_prompt=None, user_prompt=None):
        """Generate multiple post options for the user to choose from"""
        posts = []
        for i in range(count):
            post = self.generate_linkedin_post(selected_date, system_prompt, user_prompt)
            posts.append(post)
        return posts

# Test function for development
def test_generator():
    """Test function to verify the generator works"""
    try:
        generator = PostGenerator()
        post = generator.generate_linkedin_post()
        print("Generated Post:")
        print("-" * 50)
        print(post['content'])
        print("-" * 50)
        print(f"Topic: {post['topic']}")
        print(f"Word Count: {post['word_count']}")
        print(f"Character Count: {post['char_count']}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_generator() 