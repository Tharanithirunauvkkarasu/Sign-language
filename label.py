import csv
import sys 
with open("model\keypoint_classifier\keypoint_classifier_label.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([sys.argv[1]])