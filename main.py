import cv2
import image_dehazer

if __name__ == "__main__":

    HazeImg = cv2.imread('assets/hazehouse.jpg')
    HazeCorrectedImg, haze_map = image_dehazer.remove_haze(HazeImg, showHazeTransmissionMap=False)

    cv2.imshow('haze_map', haze_map);
    cv2.waitKey(0)
    cv2.imwrite("assets/result.png", HazeCorrectedImg)