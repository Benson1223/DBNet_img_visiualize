#####single image

# import cv2

# # 設定圖片和標記檔案的路徑
# training_image_dir = './archive/ch4_training_images/'
# training_image_label_dir = './archive/ch4_training_localization_transcription_gt/'

# # 讀取圖片和標記檔案
# image = cv2.imread(training_image_dir + 'img_1.jpg')
# with open(training_image_label_dir + 'gt_img_1.txt', 'r', encoding='utf-8-sig') as file:
#     lines = file.readlines()

# # 在圖片上繪製bounding box
# for line in lines:
#     data = line.strip().split(',')
#     x1, y1, x2, y2, x3, y3, x4, y4, label = data[:9]
#     x1, y1, x2, y2, x3, y3, x4, y4 = map(int, [x1, y1, x2, y2, x3, y3, x4, y4])
#     cv2.rectangle(image, (x1, y1), (x3, y3), (0, 255, 0), 2)
#     cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# # 顯示圖片
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



#####multi image
import os
import cv2

# 設定圖片和標記檔案的路徑
training_image_dir = './archive/ch4_training_images/'
training_image_label_dir = './archive/ch4_training_localization_transcription_gt/'

# 讀取資料夾中的所有圖片檔案
image_files = os.listdir(training_image_dir)


# 對每張圖片進行處理
for image_file in image_files:
    # 讀取圖片
    image_path = os.path.join(training_image_dir, image_file)
    image = cv2.imread(image_path)

    # 讀取相對應的標記檔案
    label_file = 'gt_' + image_file.replace('.jpg', '.txt')
    label_path = os.path.join(training_image_label_dir, label_file)

    
    with open(label_path, 'r', encoding='utf-8-sig') as file:
        lines = file.readlines()
    
    # 在圖片上繪製bounding box
    for line in lines:
        data = line.strip().split(',')
        x1, y1, x2, y2, x3, y3, x4, y4, label = data[:9]
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, [x1, y1, x2, y2, x3, y3, x4, y4])
        cv2.rectangle(image, (x1, y1), (x3, y3), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 顯示圖片
    cv2.imshow('Image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
