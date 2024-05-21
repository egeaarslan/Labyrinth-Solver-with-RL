import os
from PIL import Image

def combine_images_in_folder(folder_path, output_path):
    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
    
    # Sort the files to maintain a consistent order
    files.sort()
    
    # Open all images and get their sizes
    images = [Image.open(os.path.join(folder_path, f)) for f in files]
    widths, heights = zip(*(img.size for img in images))

    # Calculate the max height and total width for each row
    max_height = max(heights)
    total_width_per_row = sum(widths[:4]) if len(images) > 3 else sum(widths)

    # Calculate the number of rows needed
    num_rows = (len(images) + 3) // 4

    # Create a new image with the combined dimensions
    combined_image = Image.new('RGB', (total_width_per_row, max_height * num_rows))

    # Paste images side by side in rows
    x_offset = 0
    y_offset = 0
    for i, img in enumerate(images):
        combined_image.paste(img, (x_offset, y_offset))
        x_offset += img.size[0]
        if (i + 1) % 4 == 0:
            x_offset = 0
            y_offset += max_height

    combined_image.save(output_path)

# Example usage:
combine_images_in_folder('plots_alpha_0.1_gamma_0.95_epsilon_0.2_method_Q_learning', 'special, 0.1,0.1,0.2,q.png')
combine_images_in_folder('plots_alpha_0.1_gamma_0.95_epsilon_0.2_method_Temporal Difference Learning', 'special, 0.1,0.1,0.2,tdl.png')

# for alpha in [0.001, 0.01, 0.5, 1]:

#     combine_images_in_folder(f'plots_alpha_{alpha}_gamma_0.95_epsilon_0.2_method_Q_learning', f'combined_image, {alpha},0.1,0.2,q.png')
#     combine_images_in_folder(f'plots_alpha_{alpha}_gamma_0.95_epsilon_0.2_method_Temporal Difference Learning', f'combined_image, {alpha},0.1,0.2,tdl.png')

# for gamma in [0.10, 0.25, 0.50, 0.75]:

#     combine_images_in_folder(f'plots_alpha_0.1_gamma_{gamma}_epsilon_0.2_method_Q_learning', f'combined_image, 0.1,{gamma},0.2,q.png')
#     combine_images_in_folder(f'plots_alpha_0.1_gamma_{gamma}_epsilon_0.2_method_Temporal Difference Learning', f'combined_image, 0.1,{gamma},0.2,tdl.png')

# for epsilon in [0, 0.2, 0.5, 0.8, 1]:

#     combine_images_in_folder(f'plots_alpha_0.1_gamma_0.95_epsilon_{epsilon}_method_Q_learning', f'combined_image, 0.1,0.1,{epsilon},q.png')
#     combine_images_in_folder(f'plots_alpha_0.1_gamma_0.95_epsilon_{epsilon}_method_Temporal Difference Learning', f'combined_image, 0.1,0.1,{epsilon},tdl.png')