import base64

def png_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        return encoded_string.decode('utf-8')  # 将bytes转换为字符串


image_path = "sionna_simulate_basic_encode.png"  
base64_string = png_to_base64(image_path)
# print(base64_string)

# 
markdown_text = f"![image](data:image/png;base64,{base64_string})"

with open(image_path.replace(".png", ".md"), "w") as text_file:
    text_file.write(markdown_text)