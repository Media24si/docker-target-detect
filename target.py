import os
import sys
import cv2 as cv
import numpy as np

threshold = 0.7
match_method = cv.TM_CCOEFF_NORMED
file_folder = '/home'
template_name = 'target.png'

class TargetDetector:
    def load_template(self, template_name):
        template = cv.imread(file_folder + '/target/' + template_name, cv.IMREAD_GRAYSCALE)
        assert template is not None, "Target file not found"
        w, h = template.shape[::-1]
        return template, w, h

    def has_target(self, img):
        template, w, h = self.load_template(template_name)
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


def set_arguments():
    global template_name, threshold
    for arg in sys.argv:
        if (arg == '-t' or arg == '--template') and sys.argv.index(arg) + 1 < len(sys.argv):
            template_name = sys.argv[sys.argv.index(arg) + 1]
        if (arg == '-th' or arg == '--threshold') and sys.argv.index(arg) + 1 < len(sys.argv):
            threshold = float(sys.argv[sys.argv.index(arg) + 1])


if __name__ == "__main__":
    set_arguments()
    TargetDetector().detect_targets()
