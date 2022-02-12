import cv2
import numpy as np
import mss

# with mss.mss() as sct:
#     print(sct.monitors)
#     # filename = sct.shot(mon=2, output='test.png')
#     filename = sct.shot(mon=2)
#     print(filename)

# with mss.mss() as sct:
#     im = sct.grab(sct.monitors[1])
#
#     print(im)
#     img_rgb = np.array(im)
#     # cv2.imshow("im", img_rgb)
#     # cv2.waitKey()
#     # img_bw = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#     # print(img_rgb)
#     template = cv2.imread("2022-02-11 19_32_01-Calculatrice.png", 0)
#
#     # template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
#
#
#     result = cv2.matchTemplate(image=img_rgb, templ=template, method=cv2.TM_CCOEFF)
#     print(result)
with mss.mss() as sct:
    image = sct.grab(sct.monitors[1])
    image = np.array(image)
    # print(img_rgb)

# image = cv2.imread("monitor-1.png")
# template = cv2.imread("2022-02-11 19_32_01-Calculatrice.png")
template = cv2.imread("afficheur.png")
mask = cv2.imread("afficheur_mask.png")
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template_mask = cv2.cvtColor(mask, cv2.COLOR_RGB2GRAY)
result = cv2.matchTemplate(image=image_gray, templ=template_gray, method=cv2.TM_CCOEFF_NORMED, mask=None)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
# print(minLoc, maxLoc)

if maxVal > 0.70:
    print("Score: ",maxVal)
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
