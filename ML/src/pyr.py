import cv2
import numpy as np
import matplotlib.pyplot as plt

def show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread("sample.png")
show("img", img)
print(img.shape)

up = cv2.pyrUp(img)
# show("up", up)
print(up.shape)

down = cv2.pyrDown(img)
# show("down", down)
print(down.shape)

down_and_up = cv2.pyrUp(down)
show("down_and_up", down_and_up)
cv2.imwrite("down_and_up.png", down_and_up)
print(down_and_up.shape)

# show(np.hstack(img, down_and_up), "difference with Laplacian pyramid")
diff = img-down_and_up
show("diff", diff)
cv2.imwrite("diff.png", diff)