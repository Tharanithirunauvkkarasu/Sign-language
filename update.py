import csv
c=0

with open("model\keypoint_classifier\keypoint_classifier_label.csv", 'r') as file:
        reader = csv.reader(file)
        row_count = sum(1 for row in reader)
with open("curr.txt",'w') as f1:
    f1.write(str(row_count))
        
        

        