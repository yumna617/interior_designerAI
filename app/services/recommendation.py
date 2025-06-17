import requests
from config import Config
import random

def generate_recommendations(style, colors, budget):
    """Generate design recommendations based on style, colors and budget"""
    try:
        # Get inspiration images from Unsplash
        unsplash_url = f"https://api.unsplash.com/search/photos"
        params = {
            'query': f"{style} interior design",
            'color': ','.join(colors)[:3],  # Use up to 3 colors
            'per_page': 5,
            'client_id': Config.UNSPLASH_API_KEY
        }
        
        response = requests.get(unsplash_url, params=params)
        images = [img['urls']['regular'] for img in response.json()['results']]
        
        # Get product suggestions (mock example - could use Etsy/Pinterest API)
        products = get_product_suggestions(style, budget)
        
        return {
            "success": True,
            "inspiration_images": images,
            "product_suggestions": products,
            "color_palette": generate_color_palette(colors),
            "design_tips": get_design_tips(style, budget)
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

def get_product_suggestions(style, budget):
    """Mock function - replace with actual API calls"""
    price_ranges = {
        'low': ('$50-$200', 50, 200),
        'medium': ('$200-$500', 200, 500),
        'high': ('$500+', 500, 5000)
    }
    
    products = []
    categories = ['furniture', 'lighting', 'decor', 'textiles']
    
    for category in categories:
        products.append({
            'name': f"{style.capitalize()} {category}",
            'price': f"${random.randint(*price_ranges[budget][1:])}",
            'link': "#",
            'image': f"https://placehold.co/300x200?text={style}+{category}"
        })
    
    return products

def generate_color_palette(colors):
    """Generate a color palette based on input colors"""
    # This could be enhanced with color theory algorithms
    if not colors:
        colors = ['beige', 'white', 'gray']
    
    return {
        'primary': colors[0] if colors else 'beige',
        'secondary': colors[1] if len(colors) > 1 else 'white',
        'accent': colors[2] if len(colors) > 2 else 'gray'
    }

def get_design_tips(style, budget):
    """Get design tips based on style and budget"""
    tips = {
        'modern': [
            "Keep lines clean and uncluttered",
            "Use a monochromatic color scheme with bold accents",
            "Incorporate metal and glass elements"
        ],
        'traditional': [
            "Use rich, warm colors and wood tones",
            "Incorporate classic patterns like damask or toile",
            "Choose furniture with ornate details"
        ]
    }
    
    # Default tips if style not found
    default_tips = [
        "Start with a neutral base and add color with accessories",
        "Mix textures to add visual interest",
        "Ensure proper lighting for the space"
    ]
    
    budget_tips = {
        'low': ["Shop thrift stores and flea markets", "DIY some decor pieces"],
        'medium': ["Invest in key furniture pieces", "Mix high and low items"],
        'high': ["Consider custom furniture", "Work with a professional designer"]
    }
    
    return {
        'style_tips': tips.get(style, default_tips),
        'budget_tips': budget_tips.get(budget, [])
    }