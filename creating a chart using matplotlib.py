import matplotlib.pyplot as plt

# Sample data
labels = ['Math', 'English', 'Science', 'History', 'Art']
scores = [88, 75, 93, 70, 85]

# Create a bar chart
plt.bar(labels, scores, color='skyblue')

# Add title and axis labels
plt.title('Student Scores by Subject')
plt.xlabel('Subjects')
plt.ylabel('Scores')

# Display the chart
plt.show()
