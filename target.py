import os
import sys
import cv2 as cv
import numpy as np

threshold = 0.8 # 0.8 is the bestest threshold
match_method = cv.TM_CCOEFF_NORMED
file_folder = '/home'

template = cv.imread(file_folder + '/target/target.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "No target file found"
w, h = template.shape[::-1]

class TargetDetector:
    def has_target(self, img):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        for scale in np.linspace(0.2, 1.0, 20)[::-1]:
            resized = cv.resize(img_gray, (int(img_gray.shape[1] * scale), int(img_gray.shape[0] * scale)))
            if resized.shape[0] < h or resized.shape[1] < w:
                break

            res = cv.matchTemplate(resized, template, match_method)

            loc = np.where(res >= threshold)
            if len(loc[0]) > 0:
                return True
        return False 


    def detect_targets(self):
        found_files = []
        files = os.listdir(file_folder + '/files')

        for filename in files:
            img = cv.imread(file_folder + '/files/' + filename)        
            if img is not None and self.has_target(img):
                found_files.append(filename)

        print(found_files)


if __name__ == "__main__":
    TargetDetector().detect_targets()
