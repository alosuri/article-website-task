from openai import OpenAI

client = OpenAI(
    api_key="PUT_YOUR_API_KEY_HERE"
)

article = open("text.txt", "r")
prompt = 'Generate an article using this text: ' + article.read() + '. Include only the HTML body content (no <html> or <body> tags), formatted with headings, paragraphs, and an <img> tag where they are relevant to the content, such as after important points or sections, <img> tag must be in <figure> tag with matching <figcaption> tag. Set <img> src to "image_placeholder.jpg" with an alt tag containing a detailed prompt describing the image based on the section of the article it accompanies (Prompt should be entirely in English). The alt tag should provide enough detail for generating the image for that section. Article text should be entirely in Polish.'

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ]
)

html_file = open("artykul.html", "w")
html_file.write(completion.choices[0].message.content)
html_file.close()

# print(completion.choices[0].message.content) 