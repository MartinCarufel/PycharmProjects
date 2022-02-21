import cv2
import numpy as np
import mss


image = cv2.imread("img.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
template_l = ["img_cr.png", "img_cr2.png"]

for template in template_l:
    template = cv2.imread(template)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image=image_gray, templ=template_gray, method=cv2.TM_CCOEFF_NORMED, mask=None)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
    # print(minLoc, maxLoc)

    if maxVal > 0.50:
        print("Score: ", maxVal)
        (startX, startY) = maxLoc
        endX = startX + template.shape[1]
        endY = startY + template.shape[0]
        cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
        cv2.imshow("Output", image)
        cv2.waitKey(0)
    else:
        print("Score: ", maxVal)
        print("Not found")
    # cv2.imshow("Output", image)
    # cv2.waitKey(0)


"""import cv2
import numpy as np

screenshot = cv2.imread("screenshot.png", 0)
template = cv2.imread("template.png",  0)

res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)

# threshold  = 0.1
# loc = np.where (res >= threshold)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

print(min_loc)
which gives

(389, 412)"""
