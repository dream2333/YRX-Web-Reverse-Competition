import base64

# Base64-encoded TTF font
base64_font = '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'
# Output file path
output_path = 'q7/font.woff'

# Decode Base64-encoded font data
font_data = base64.b64decode(base64_font)

# Write font data to file
with open(output_path, 'wb') as f:
    f.write(font_data)