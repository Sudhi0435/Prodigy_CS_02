from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key=50):
    # Open the image
    image = Image.open(image_path)
    image_np = np.array(image)

    # Apply pixel manipulation
    encrypted_image_np = (image_np + key) % 256

    # Optionally, swap pixels (simple row-wise swap)
    encrypted_image_np = encrypted_image_np[::-1]

    # Convert back to an image and save
    encrypted_image = Image.fromarray(encrypted_image_np.astype('uint8'))
    encrypted_image.save(output_path)

def decrypt_image(encrypted_image_path, output_path, key=50):
    # Open the encrypted image
    encrypted_image = Image.open(encrypted_image_path)
    encrypted_image_np = np.array(encrypted_image)

    # Reverse pixel swap
    encrypted_image_np = encrypted_image_np[::-1]

    # Reverse pixel manipulation
    decrypted_image_np = (encrypted_image_np - key) % 256

    # Convert back to an image and save
    decrypted_image = Image.fromarray(decrypted_image_np.astype('uint8'))
    decrypted_image.save(output_path)

# Example usage
encrypt_image('input_image.png', 'encrypted_image.png', key=50)
decrypt_image('encrypted_image.png', 'decrypted_image.png', key=50)
