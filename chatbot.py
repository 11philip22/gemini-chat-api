from gemini_client import Chatbot, Model

# Initialize the chatbot
try:
    chatbot = Chatbot(cookie_path="cookies.json", model=Model.G_2_5_PRO)
except Exception as e:
    print(f"Error initializing chatbot: {e}")
    exit()

# Ask a question
try:
    response = chatbot.ask("Hello, how are you today? Generate me a image of a smiley face :)")
    if response and not response.get("error"):
        print("Gemini:", response["content"])

        # Handling images in response
        if response.get("images"):
            print("\nImages found:")
            for img_data in response["images"]:
                # Note: The 'images' in the response are dicts.
                # To use the Image class features (like saving), you'd typically
                # instantiate Image objects from these dicts if needed,
                # especially if you want to use the save method directly on an Image object.
                # For generated images, you'd need to pass cookies to GeneratedImage.
                print(f"- Title: {img_data.get('title', '[Image]')}, URL: {img_data.get('url')}, Alt: {img_data.get('alt')}")

    else:
        print("Error or no content in response:", response)

except Exception as e:
    print(f"Error during ask: {e}")

# # Ask a question with an image
# try:
#     # Ensure 'image.png' exists or provide a valid path/bytes
#     response_with_image = chatbot.ask("What is in this image?", image="path/to/your/image.png")
#     if response_with_image and not response_with_image.get("error"):
#         print("\nGemini (with image):", response_with_image["content"])
#     else:
#         print("Error or no content in response with image:", response_with_image)
# except FileNotFoundError:
#     print("Image file not found. Skipping ask with image example.")
# except Exception as e:
#     print(f"Error during ask with image: {e}")