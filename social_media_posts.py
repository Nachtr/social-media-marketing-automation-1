# Define a list of products for our social media marketing automation
products = [
    {"image": "product1.jpg", "description": "Introducing our new wireless headphones!"},
    {"image": "product2.jpg", "description": "The perfect summer sandals are here!"}
]

# Define a list of platforms
platforms = ["Facebook", "Twitter", "Instagram"]

# Function to print product information
def print_product_info(products):
    for product in products:
        image = product["image"]
        description = product["description"]
        print(f"Product Post: Image - {image}, Description - {description}")

# Function to print social media post
def print_post_by_platform(platform, image, description):
    print(f"Platform: {platform} - Post: Image - {image}, Description - {description}")

# Loop through each product and post it on all platforms
for product in products:
    for platform in platforms:
        print_post_by_platform(platform, product["image"], product["description"])
# Didnt use zip() cause it was completely unnecessary