import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
# Custom color map
from matplotlib.colors import LinearSegmentedColormap, ListedColormap
import numpy as np

# Assuming `processed_data` is the cleaned and normalized data you have
processed_data = {
    "Industry1": {"Keyword1": 0.1, "Keyword2": 0.3, "Keyword3": 0.4},
    "Industry2": {"Keyword1": 0.2, "Keyword2": 0.15, "Keyword3": 0.25},
    "Industry3": {"Keyword1": 0.3, "Keyword2": 0.05, "Keyword3": 0.1},
}

# Read the data from the input JSON file
with open("processed_word_count.json", "r") as input_file:
# with open("./wordcounts/environmental.json", "r") as input_file:
    processed_data = json.load(input_file)


# Convert the data to a Pandas DataFrame
data_frame = pd.DataFrame(processed_data)

# Create a custom colormap
main_cmap = LinearSegmentedColormap.from_list(
    "custom",
    ["yellow", "limegreen", "blue"],
    N=256
)
main_cmap = plt.get_cmap("YlGnBu")

# Generate the list of colors from the colormap
colors_list = main_cmap(np.linspace(0, 1, 256))

# Add white as the first color in the list
colors_list[0] = (0.98, 0.98, 0.98, 0.98)  # RGBA value for white
colors_list[0] = (1, 1, 1, 1)  # RGBA value for white

# Create the custom colormap with the new colors list
custom_cmap = ListedColormap(colors_list)

# Create the heatmap
plt.figure(figsize=(14, 8))

# Add margins to the left and right edges of the plot
plt.subplots_adjust(bottom=0.3, top=0.9, left=0.15, right=1.0)

# Color Mapping
# sns.heatmap(data_frame, annot=False, cmap="YlGnBu", linewidths=0.5)
heatmap = sns.heatmap(data_frame, annot=False, cmap=custom_cmap, linewidths=0.5)

# Set the title and labels
plt.title("Normalized Word Count Across All Industries")
plt.xlabel("Industry")
plt.ylabel("Keyword")

# plt.savefig(f"./wordcounts/environmental.png") # Save as PNG images
plt.savefig(f"./wordcounts/allwords.png") # Save as PNG images

# Show the heatmap
# plt.show()


